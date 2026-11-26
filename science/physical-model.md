# Thresholded readout with a drifting phase

[Science overview](README.md) · [Detector model](model.md) · [Calibration and confidence](calibration.md)

A detector with a fixed digital threshold can lose all one-shot sensitivity when its readout phase wanders. If the phase persists over a pair of reads, the reference read can restore sensitivity to a Pauli expectation. This example separates phase correlation from ordinary readout noise.

## One quadrature, two probes

Consider a dispersive pointer model with two equal-amplitude antipodal pointer states. After the chosen Pauli basis rotation, write the ideal computational readout as a sign $`J\in\{-1,1\}`$ with mean $`\mu`$. The detector thresholds one quadrature.

```math
Q=AJ\cos\phi+N,\qquad
U=\mathrm{sgn}(Q),\qquad
N\sim\mathcal N(0,\sigma^2).
```

Here $`A>0`$ is the pointer amplitude, $`\phi`$ is the unobserved phase relative to the threshold axis, and the Gaussian readout noise $`N`$ is independent at each use. This is a synthetic assignment model for the measured pointer quadrature. The experimenter receives only $`U`$. A private $`X`$ mask flips the physical sign, and the corresponding output sign correction has the same conditional law as above by Gaussian symmetry. The diagonal model is unchanged by a $`Z`$ mask.

Define $`a=A/\sigma`$. Gaussian thresholding gives

```math
g_a(\phi)=\mathrm{erf}\!\left(\frac{a\cos\phi}{\sqrt{2}}\right),
\qquad
\mathbb E[U\mid J,\phi]=Jg_a(\phi).
```

Let the first read carry the signal and the second read carry a known $`J=+1`$ reference. For phase pair $`(\phi_1,\phi_2)`$ independent of the ideal signs, conditional detector noise factors across the reads. The product of corrected signs $`W=U_1 U_2`$ has mean $`\mu\kappa`$ on signal blocks and mean $`\kappa`$ when both probes are references, where

```math
\kappa=\mathbb E[g_a(\phi_1)g_a(\phi_2)].
```

Suppose each phase marginal is uniform on the circle. Because $`g_a(\phi+\pi)=-g_a(\phi)`$, either corrected output is a fair sign for either input sign. The two-bit signal law is $`\Pr(U_1=u,U_2=v)=(1+uv\mu\kappa)/4`$, so the product contains all the dependence on $`\mu`$ in this model. Two choices of the phase law give different experiments despite identical single-use outputs.

| Phase law within each pair | Pair contrast | Information in the two digital outputs |
| --- | --- | --- |
| Uniform common phase $`\phi_1=\phi_2`$ | $`\kappa=\mathbb E[g_a(\phi)^2]>0`$ | The product estimates $`\mu`$ with charged reference calibration. |
| Independent uniform phases | $`\kappa=0`$ | The two outputs are independent fair signs for every $`\mu`$. |

The phase may be freshly redrawn for each pair to make this particular synthetic benchmark independent across blocks. The [finite-sample certificate](calibration.md) permits memory across blocks as well.

## Predicting the effect of timing

Take $`\phi_1`$ uniform and let $`\phi_2=\phi_1+\Delta`$ modulo $`2\pi`$, with an independent Gaussian increment $`\Delta`$ of variance $`2D_\phi\tau`$ at lag $`\tau`$. Define

```math
c_m(a)=\frac{1}{2\pi}\int_0^{2\pi}g_a(\phi)e^{-im\phi}\,d\phi .
```

The conditional phase average is the convolution of $`g_a`$ with the wrapped Gaussian. Orthogonality of the Fourier modes gives

```math
\kappa(\tau)=\sum_{m\in\mathbb Z}|c_m(a)|^2e^{-m^2D_\phi\tau}.
```

Only odd $`m`$ contribute because shifting $`\phi`$ by $`\pi`$ flips the response. The first coefficient is real and positive because $`g_a(\phi)\cos\phi`$ is positive away from the zeros of $`\cos\phi`$. It follows that

```math
2|c_1(a)|^2e^{-D_\phi\tau}
\le \kappa(\tau)
\le e^{-D_\phi\tau}\kappa(0).
```

This gives a direct prediction for a delay sweep. At low amplitude, expansion of the error function yields

```math
\kappa(\tau)=\frac{a^2}{\pi}e^{-D_\phi\tau}
+O(a^4 e^{-D_\phi\tau}) .
```

The numbers below are model predictions. They come from the periodic trapezoidal average of $`g_a^2`$ and its odd Fourier coefficients on 16,384 equally spaced angles. The lag column retains odd modes through order 35. [Reproduce the calculation](../verification/phase_benchmark.py).

| Pointer amplitude to noise $`a`$ | Shared-phase pair, $`\kappa(0)`$ | Diffusing pair, $`\kappa(\tau)`$ at $`D_\phi\tau=1`$ | Phase-aligned single-use contrast $`g_a(0)`$ |
| ---: | ---: | ---: | ---: |
| 0.25 | 0.019587 | 0.007206 | 0.197413 |
| 0.50 | 0.074836 | 0.027528 | 0.382925 |
| 1.00 | 0.252025 | 0.092573 | 0.682689 |
| 2.00 | 0.587416 | 0.212575 | 0.954500 |

One controlled benchmark compares two schedules at the same $`a`$ and the same threshold. In one schedule the detector shares a uniform phase over a pair. In the other it redraws phase on every read. Alternate signal and all-reference arms by an independent private coin, and record both one-shot contrasts and the paired contrast. Keep the pulse amplitude and the spacing between reads fixed across the two schedules.

## Detector calls and the phase-reference baseline

Each paired block consumes two detector calls. It contains either one signal and one reference probe, or two reference probes. With a fair choice between these arms, $`B`$ blocks always use $`2B`$ calls and on average consume $`B/2`$ source copies and $`3B/2`$ reference preparations.

The paired method needs order $`\kappa(\tau)^{-2}\epsilon^{-2}\log(1/\delta)`$ blocks under a stable positive contrast. Thus the shared-phase pair has an $`a^{-4}`$ detector-call factor at low amplitude. The phase-aligned single-use baseline with supplied locked phase has contrast $`g_a(0)=\sqrt{2/\pi}\,a+O(a^3)`$ and an $`a^{-2}`$ factor. That baseline assumes access to a reliable phase reference. At known $`\kappa(\tau)`$ the two corrected output bits have Fisher information $`\kappa(\tau)^2`$ per signal block at $`\mu=0`$, which reflects the paired contrast penalty. Preparation, calibration, and reference hardware affect any comparison of time or engineering cost.

A receiver with analogue samples can always threshold them in software and emulate a digital receiver. It can also exploit quadrature amplitudes or a simultaneous sideband phase reference when available. In a transmon experiment, Adisa et al. recovered single-shot separation by reconstructing a multitone self-phase-referenced signal when the carrier phase wandered. The controlled digital example isolates what can be learned from two thresholded reports and an extra known probe. [Adisa et al., Fig. 3 and Supplement S2](https://arxiv.org/html/2512.03138v3).

## Imperfect references and control leakage

If the second probe is prepared with a fixed independent mean sign $`\nu`$ rather than $`+1`$, both conditional score means acquire the same factor $`\nu`$. With a trusted first-slot calibration preparation, the ratio still estimates $`\mu`$ with effective contrast $`\nu\kappa`$. The contrast falls when the pilot is unreliable. If the first-slot calibration state is also imperfect, its known mean can be included explicitly. An unknown first-slot reference mean introduces a scale ambiguity in the two score means.

The [finite-error statement](calibration.md) compares the actual arm transcripts with those from one common causal instrument. A uniform total variation error at most $`\eta`$ widens the residual threshold by $`4B\eta`$ for a fair arm coin. When the observed calibration strength is order $`B|\kappa|`$, this adds a systematic error scale of order $`\eta/|\kappa|`$. A trace-distance bound on the joint states given to one common detector implies the same assumption by data processing. For product preparations, a sum of per-probe trace-distance bounds supplies a block bound.

Unrestricted detector access to the arm can destroy the shared contrast entirely. For example, a detector could emit ideal results on calibration blocks and discard the signal on the other arm. A measured calibration contrast then says nothing about the signal. The operational requirement is agreement of the arm-dependent transcript laws with one common instrument to the needed accuracy.
