from itertools import combinations, product

import numpy as np


def random_povm(dimension, rng):
    matrices = rng.normal(size=(dimension, dimension, dimension))
    matrices = matrices + 1j * rng.normal(size=matrices.shape)
    effects = matrices.conj().transpose(0, 2, 1) @ matrices
    values, vectors = np.linalg.eigh(effects.sum(axis=0))
    inverse_root = (vectors * values**-0.5) @ vectors.conj().T
    return inverse_root @ effects @ inverse_root


def characters(mask, indices):
    return np.array([(-1)**(int(mask) & int(x)).bit_count() for x in indices])


def verify_twirl(effects, state):
    dimension = len(state)
    indices = np.arange(dimension)
    ideal = np.abs(state)**2
    noise = np.array([
        np.mean([effects[x ^ e, x, x].real for x in indices]) for e in indices
    ])
    direct = np.zeros(dimension)
    for flip, phase in product(indices, repeat=2):
        padded = (state * characters(phase, indices))[indices ^ flip]
        for y in indices:
            value = np.vdot(padded, effects[y ^ flip] @ padded).real
            direct[y] += value / dimension**2
    expected = np.array([noise[y ^ indices] @ ideal for y in indices])
    np.testing.assert_allclose(direct, expected, rtol=0, atol=1e-12)
    for support in indices[1:]:
        parity = characters(support, indices)
        np.testing.assert_allclose(direct @ parity, (noise @ parity) * (ideal @ parity),
                                   rtol=0, atol=1e-12)
    return float(np.max(np.abs(direct - expected)))


def check_twirl():
    rng = np.random.default_rng(20261126)
    errors = []
    for dimension in (2, 4, 8):
        for _ in range(10):
            state = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
            state /= np.linalg.norm(state)
            errors.append(verify_twirl(random_povm(dimension, rng), state))

    # The detector emits a fair first bit, retains the first qubit, then
    # measures XX and adjusts the second bit using the first report.
    flip = np.array([[0, 1], [1, 0]])
    xx = np.kron(flip, flip)
    causal = np.array([(np.eye(4) + (-1)**(a ^ b) * xx) / 4
                       for a, b in product((0, 1), repeat=2)])
    source = np.array([1, 1, 0, 0]) / np.sqrt(2)
    errors.append(verify_twirl(causal, source))
    print(f'Twirl and parity: 31 instances, largest probability error {max(errors):.2e}')


def check_even_masks():
    for length in range(2, 7):
        support = [e for e in product((0, 1), repeat=length) if sum(e) % 2 == 0]
        for size in range(1, length):
            for slots in combinations(range(length), size):
                counts = {}
                for error in support:
                    key = tuple(error[j] for j in slots)
                    counts[key] = counts.get(key, 0) + 1
                assert len(counts) == 2**size
                assert set(counts.values()) == {2**(length - 1 - size)}
        for signal in (0, 1):
            assert all(((signal ^ error[0]) + sum(error[1:])) % 2 == signal
                       for error in support)
    print('Even masks: every proper marginal is uniform for lengths 2 through 6')


def check_context_decoder():
    for signs in product((-1, 1), repeat=4):
        corrected = []
        for context, phase_bit in product(range(4), (0, 1)):
            mask = (-1)**phase_bit * signs[context]
            corrected.append(mask)
            for signal in (-1, 1):
                assert signal * mask * (-1)**phase_bit * signs[context] == signal
        assert sum(corrected) == 0

    for contexts, blocks in product(range(1, 5), range(1, 5)):
        sequences = list(product(range(contexts), repeat=blocks))
        repeated = sum(sum(row.count(context) > 1 for context in row) for row in sequences)
        expected = blocks * (1 - (1 - 1 / contexts)**(blocks - 1))
        np.testing.assert_allclose(repeated / len(sequences), expected, atol=1e-14)
        assert expected <= min(blocks, blocks * (blocks - 1) / contexts) + 1e-12
    print('Decoder: all four-context tables, and exact repeat counts for small block budgets')


def check_product_axes():
    rng = np.random.default_rng(126)
    for weight in range(1, 5):
        axes = rng.normal(size=(weight, 3))
        axes /= np.linalg.norm(axes, axis=1, keepdims=True)
        overlaps = [np.prod([axes[j, label] for j, label in enumerate(labels)])
                    for labels in product(range(3), repeat=weight)]
        np.testing.assert_allclose(np.sum(np.square(overlaps)), 1, atol=1e-14)
        for overlap in overlaps:
            bias = 0.3 * overlap
            alt = np.array([(1 + bias) / 2, (1 - bias) / 2])
            divergence = 0.5 * np.log(0.5 / alt).sum()
            np.testing.assert_allclose(divergence, -0.5 * np.log1p(-bias**2), atol=1e-14)
    print('Product-basis converse: axis sum and reverse divergence for weights 1 through 4')


def main():
    check_twirl()
    check_even_masks()
    check_context_decoder()
    check_product_axes()


if __name__ == '__main__':
    main()
