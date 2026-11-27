#!/usr/bin/env python3
"""Check finite identities for source-only readout with a two-slot detector."""

from fractions import Fraction
from itertools import product


SIGNS = (-1, 1)
SIGN_PAIRS = tuple(product(SIGNS, repeat=2))


def require_equal(actual, expected):
    if actual != expected:
        raise AssertionError(f"expected {expected}, observed {actual}")


def sign_probability(sign, mean):
    return (1 + sign * mean) * Fraction(1, 2)


def source_law(polarization, copies):
    for signs in product(SIGNS, repeat=copies):
        probability = Fraction(1)
        for sign in signs:
            probability *= sign_probability(sign, polarization)
        yield signs, probability


def hard_detector_record_probability(raw, pads, ideal_law, contrast):
    """The noise uses one fair shared sign and a contrast-biased parity sign."""
    probability = Fraction(0)
    for ideal, ideal_probability in ideal_law:
        first_polarity = raw[0] * pads[0] * ideal[0]
        second_polarity = raw[1] * pads[1] * ideal[1]
        joint_noise_probability = sign_probability(
            first_polarity * second_polarity, contrast
        ) / 2
        probability += ideal_probability * joint_noise_probability
    return probability


def check_full_record():
    cases = 0
    # An arbitrary ideal joint measurement distribution, possibly correlated.
    ideal_law = tuple(zip(SIGN_PAIRS, map(Fraction, ("1/10", "1/5", "3/10", "2/5"))))
    ideal_parity = sum(prob * a * b for (a, b), prob in ideal_law)
    for contrast in map(Fraction, ("-3/5", "0", "2/7", "1")):
        joint = {}
        # For this diagonal physical detector the private Z pads do not change
        # the ideal distribution. Retaining either X or Z pad gives no extra shift.
        for x_pads, z_pads in product(SIGN_PAIRS, repeat=2):
            for raw in SIGN_PAIRS:
                observed = hard_detector_record_probability(
                    raw, x_pads, ideal_law, contrast
                )
                corrected_parity = raw[0] * raw[1] * x_pads[0] * x_pads[1]
                expected = sign_probability(corrected_parity, contrast * ideal_parity) / 2
                require_equal(observed, expected)
                joint[x_pads, z_pads, raw] = observed / 16
                cases += 1
        require_equal(sum(joint.values()), 1)
        for x_pads, z_pads in product(SIGN_PAIRS, repeat=2):
            for slot, sign in product(range(2), SIGNS):
                marginal = sum(
                    joint[x_pads, z_pads, raw] for raw in SIGN_PAIRS if raw[slot] == sign
                )
                require_equal(marginal, Fraction(1, 32))
    return cases


def check_width_two():
    def cnot_outputs(signs):
        control, target = signs
        return control, control * target

    def local_law(polarization, a, b):
        return tuple(
            (
                (x, y),
                sign_probability(x, a * polarization)
                * sign_probability(y, b * polarization),
            )
            for x, y in SIGN_PAIRS
        )

    values = tuple(map(Fraction, ("-1", "-2/3", "-1/7", "0", "1/5", "3/4", "1")))
    local_z_coefficients = tuple(map(Fraction, ("-1", "-4/5", "0", "3/5", "1")))
    contrast = Fraction(3, 5)
    cases = 0
    for z in values:
        independent_law = tuple(source_law(z, 2))
        cnot_law = tuple((cnot_outputs(signs), prob) for signs, prob in independent_law)
        for law, ideal_mean in [(independent_law, z**2), (cnot_law, z)]:
            require_equal(sum(a * b * prob for (a, b), prob in law), ideal_mean)
            corrected_mean = sum(
                a * b * hard_detector_record_probability((a, b), (1, 1), law, contrast)
                for a, b in SIGN_PAIRS
            )
            require_equal(corrected_mean, contrast * ideal_mean)
            cases += 1
        for a, b in product(local_z_coefficients, repeat=2):
            # Local unitaries produce independent ideal signs with means a*z and b*z.
            positive_law = local_law(z, a, b)
            negative_law = local_law(-z, a, b)
            for raw, pads in product(SIGN_PAIRS, repeat=2):
                require_equal(
                    hard_detector_record_probability(raw, pads, positive_law, contrast),
                    hard_detector_record_probability(raw, pads, negative_law, contrast),
                )
                cases += 1

    for epsilon in map(Fraction, ("1/20", "1/50", "1/100")):
        z0, z1 = 3 * epsilon, 6 * epsilon
        kappa0, kappa1 = Fraction(1, 2), Fraction(1, 4)
        require_equal(kappa0 * z0, kappa1 * z1)
        require_equal(kappa1 * z1**2 - kappa0 * z0**2, Fraction(9, 2) * epsilon**2)
        cases += 1
    return cases


def multiply_complex_pair(left, right):
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def sin_sum(signs, cos_t, sin_t):
    pair = (Fraction(1), Fraction(0))
    for sign in signs:
        pair = multiply_complex_pair(pair, (cos_t, sign * sin_t))
    return pair[1]


def compressor_expectation(signs, cos_t, sin_t):
    target, *signals = signs
    controls = tuple(target * sign for sign in signals)
    return target * sin_sum(controls, cos_t, sin_t)


def check_compressed_parity():
    # Rational sine and cosine allow exact finite probability checks. This
    # angle choice checks the circuit identity, rather than optimizing slope.
    cos_t, sin_t = Fraction(4, 5), Fraction(3, 5)
    contrast = Fraction(4, 7)
    cases = 0
    for m, z in product(range(1, 5), map(Fraction, ("-4/5", "-2/5", "0", "1/7", "3/5"))):
        ideal_response = sin_sum((1,) * m, cos_t, z * sin_t)
        compressed_sign_law = {sign: Fraction(0) for sign in SIGNS}
        encoded_linear_law = {signs: Fraction(0) for signs in SIGN_PAIRS}
        within_compressor_law = {signs: Fraction(0) for signs in SIGN_PAIRS}
        encoded_quadratic_law = {signs: Fraction(0) for signs in SIGN_PAIRS}
        for signs, probability in source_law(z, m + 1):
            output_mean = compressor_expectation(signs, cos_t, sin_t)
            require_equal(output_mean, sin_sum(signs[1:], cos_t, sin_t))
            # The controlled target rotation preserves the control bit signs.
            # A CNOT from the first control to the target puts the target Z
            # observable in the parity of the two physical output slots.
            control = signs[0] * signs[1]
            for output in SIGNS:
                output_probability = probability * sign_probability(output, output_mean)
                compressed_sign_law[output] += output_probability
                within_compressor_law[control, control * output] += output_probability
        require_equal(
            sum(a * b * prob for (a, b), prob in within_compressor_law.items()),
            ideal_response,
        )
        for (target_a, probability_a), (target_b, probability_b) in product(
            compressed_sign_law.items(), repeat=2
        ):
            # Two disjoint compressors put their target-product observable
            # into the measured parity. A CNOT retains just target A's sign.
            probability = probability_a * probability_b
            encoded_quadratic_law[target_a, target_b] += probability
            encoded_linear_law[target_a * target_b, target_b] += probability
        for law, ideal_mean in [
            (encoded_linear_law, ideal_response),
            (encoded_quadratic_law, ideal_response**2),
        ]:
            require_equal(sum(a * b * prob for (a, b), prob in law.items()), ideal_mean)
            corrected_mean = sum(
                a * b * hard_detector_record_probability(
                    (a, b), (1, 1), law.items(), contrast
                )
                for a, b in SIGN_PAIRS
            )
            require_equal(corrected_mean, contrast * ideal_mean)
            cases += 1
    return cases


def check_drift_interleaving():
    cases = 0
    for response in map(Fraction, ("-3/7", "0", "2/5", "1")):
        histories = {(): Fraction(1)}
        realized_score = [Fraction(0), Fraction(0)]
        expected_score = [Fraction(0), Fraction(0)]
        responses = (response, response**2)
        for _ in range(4):
            next_histories = {}
            for history, history_probability in histories.items():
                # Contrast at time t may depend on past arms and outcomes.
                if not history or history[-1] == (0, 1):
                    contrast = Fraction(1, 7)
                else:
                    contrast = Fraction(4, 5)
                conditional_scores = [Fraction(0), Fraction(0)]
                for arm, parity in product(range(2), SIGNS):
                    branch_probability = sign_probability(parity, contrast * responses[arm]) / 2
                    score = 2 * parity
                    conditional_scores[arm] += branch_probability * score
                    path_probability = history_probability * branch_probability
                    next_histories[history + ((arm, parity),)] = path_probability
                    realized_score[arm] += history_probability * branch_probability * score
                for arm in range(2):
                    require_equal(conditional_scores[arm], contrast * responses[arm])
                    expected_score[arm] += history_probability * contrast * responses[arm]
                    cases += 1
            require_equal(sum(next_histories.values()), 1)
            histories = next_histories
        require_equal(realized_score, expected_score)
        # A nonzero per-round magnitude does not prevent cancellation.
        pair = Fraction(3, 4), Fraction(-3, 4)
        require_equal(sum(kappa * response for kappa in pair), 0)
        require_equal(sum(kappa * response**2 for kappa in pair), 0)
    return cases


def main():
    for name, check in (
        ("Full masked record and blind marginals", check_full_record),
        ("CNOT separation, product sign blindness and matched pair", check_width_two),
        ("Compressed linear and quadratic parity", check_compressed_parity),
        ("Conditional interleaving under drift", check_drift_interleaving),
    ):
        print(f"{name}: {check()} cases passed")


if __name__ == "__main__":
    main()
