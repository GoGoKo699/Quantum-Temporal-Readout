"""Reproduce the thresholded phase-readout table with Python's standard library."""

from math import cos, erf, exp, fsum, isclose, sqrt, tau


QUADRATURE_POINTS = 16_384
HIGHEST_HARMONIC = 35
DIFFUSION_LAG = 1.0
AMPLITUDES = (0.25, 0.5, 1.0, 2.0)


def contrasts(amplitude):
    """Return the shared-phase, finite-lag, and locked-phase contrasts."""
    phases = tuple(tau * index / QUADRATURE_POINTS for index in range(QUADRATURE_POINTS))
    scale = amplitude / sqrt(2)
    responses = tuple(erf(scale * cos(phase)) for phase in phases)
    dc_component = fsum(responses) / QUADRATURE_POINTS
    shared = fsum(response**2 for response in responses) / QUADRATURE_POINTS

    energies = []
    lagged_energies = []
    for harmonic in range(1, HIGHEST_HARMONIC + 1, 2):
        # The response is even, so the sine coefficients vanish.
        coefficient = fsum(
            response * cos(harmonic * phase)
            for phase, response in zip(phases, responses)
        ) / QUADRATURE_POINTS
        energy = 2 * coefficient**2  # Positive and negative harmonics.
        energies.append(energy)
        lagged_energies.append(energy * exp(-harmonic**2 * DIFFUSION_LAG))

    lagged = fsum(lagged_energies)
    locked = erf(scale)
    assert isclose(dc_component, 0.0, abs_tol=1e-14)
    assert isclose(fsum(energies), shared, rel_tol=1e-12, abs_tol=1e-14)
    assert 0 <= lagged <= exp(-DIFFUSION_LAG) * shared + 1e-14
    return shared, lagged, locked


def main():
    print("a      shared      diffusing   phase-aligned")
    for amplitude in AMPLITUDES:
        shared, lagged, locked = contrasts(amplitude)
        print(f"{amplitude:4.2f}   {shared:.6f}    {lagged:.6f}    {locked:.6f}")


if __name__ == "__main__":
    main()
