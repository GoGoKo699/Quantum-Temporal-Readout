# Finite inference with interleaved references

A detector can retain quantum or classical memory between probes. The randomized protocol below guarantees a confidence set even when the detector's response changes between blocks. Its precision is determined by the temporal contrast measured by the reference blocks.

## The experiment

Choose a nonidentity Pauli observable $`P`$ and let $`\mu=\mathrm{Tr}(P\rho)`$ for the fixed source state $`\rho`$. Use $`B`$ blocks of $`L`$ detector calls each. In block $`b`$ choose a fair private bit $`A_b`$. If $`A_b=1`$, send a fresh source copy in the first slot, after applying the product basis rotation that maps $`P`$ to $`Z`$ parity on its support. If $`A_b=0`$, send $`|0\rangle^{\otimes n}`$ in that slot. The other slots always carry fresh zero-state references. Apply independent private local Pauli masks in all slots, and correct the classical readouts with the corresponding bit masks.

The next block can depend on all previous data. Let $`\mathcal F_{b-1}`$ denote this history before drawing the current arm or masks. The detector may react to the probes it receives. The current arm and trusted controls are private, and the fresh probes are initially independent of detector memory conditional on $`\mathcal F_{b-1}`$. These assumptions give a common conditional instrument for either arm.

Let $`Z_1`$ be the corrected first-slot parity, as a sign, and let $`R`$ be the corrected pilot record. Choose a score $`W_b=Z_1w_b(R)`$ with $`|w_b|\le1`$. The function $`w_b`$ can be selected using $`\mathcal F_{b-1}`$. For two calls, one choice is to let $`w_b`$ be the matching support parity on the second call. The additive-error representation yields

```math
\begin{aligned}
\mathbb E[W_b\mid\mathcal F_{b-1},A_b=1]&=\mu\kappa_b,\\
\mathbb E[W_b\mid\mathcal F_{b-1},A_b=0]&=\kappa_b.
\end{aligned}
```

Here $`\kappa_b`$ is the conditional expectation of the first-slot error sign multiplied by $`w_b(R)`$. Indeed, the source's ideal first-slot parity is independent of the joint error in the corrected-output model. Its mean is $`\mu`$ in the signal arm and one in the reference arm. The pilots expose the remaining components of the joint error.

## Confidence set and resource cost

From the same stream of blocks, compute

```math
S=\sum_{b=1}^{B}2A_bW_b,\qquad
C=\sum_{b=1}^{B}2(1-A_b)W_b.
```

The successive contributions to $`S-\mu C`$ have conditional mean zero and absolute value at most two. Azuma–Hoeffding therefore gives the following $`1-\delta`$ confidence set at the fixed horizon $`B`$:

```math
\mathcal I
=
\left\{u\in[-1,1]:
   |S-uC|\le 2\sqrt{2B\log(2/\delta)}
\right\}.
```

When $`C\ne0`$, the radius of the interval before clipping is $`2\sqrt{2B\log(2/\delta)}/|C|`$. The protocol can abstain when the set is empty or too broad for the requested precision. The bound applies without a stationarity assumption or a specified detector-memory dimension.

For a deterministic precision guarantee, suppose the magnitude of the average predictable contrast is at least $`\kappa_{\min}>0`$ on every possible history. The increments of $`C-\sum_b\kappa_b`$ have conditional mean zero and absolute value at most three. Consequently $`|C|\ge B\kappa_{\min}/2`$ with high probability once $`B`$ is of order $`\kappa_{\min}^{-2}\log(1/\delta)`$. Combining the two bounds, the clipped ratio attains additive error $`\epsilon`$ at failure probability at most $`\delta`$ using

```math
B=O\!\left(\kappa_{\min}^{-2}\epsilon^{-2}\log(1/\delta)\right)
```

blocks for $`0<\epsilon\le1`$ and $`0<\delta\le1/4`$. Both arms and all $`L`$ calls per block count. Contrasts of opposite signs can cancel over the acquisition. The data-dependent set remains valid in that case and can become broad.

If a common ideal instrument approximates the real experiment within trace distance or total variation $`\eta`$ conditional on each history, arm, and configuration, the mean of each bounded score differs by at most $`2\eta`$ per arm. For the real observations, subtracting the conditional mean of each residual increment gives a martingale with conditional range length at most four. The original concentration threshold therefore still applies to the centered residual. Widening the displayed bound by $`4B\eta`$ covers the possible residual drift. This quantifies why controlling leaks in the arm, timing and mask instructions matters.

## One stream for many Pauli observables

Fix $`M`$ nonidentity Pauli strings of weight at most $`k`$. In each signal arm for a two-call block, independently draw a uniform product basis from the three Pauli axes on every site. A basis matches the target $`P`$ on its support $`s`$ with probability $`p_P=3^{-|s|}`$. Take $`W_{b,s}`$ to be the product of the two corrected support parities. Let $`q`$ be the probability of the signal arm, and define

```math
S_P=\sum_{b=1}^{B}
     \frac{A_b\,\mathbf 1_{\{\text{basis matches }P\}}W_{b,s}}{qp_P},
\qquad
C_s=\sum_{b=1}^{B}\frac{(1-A_b)W_{b,s}}{1-q}.
```

The reference arm uses two zero-state probes, so one block provides calibration scores for every support. As in the scalar case, the conditional means of the increments of $`S_P`$ and $`C_s`$ are $`\mu_P\kappa_{b,s}`$ and $`\kappa_{b,s}`$. This shared contrast uses the privacy of the basis program as well as the arm and masks.

The residual increment $`\Delta(S_P-\mu_PC_s)`$ has mean zero conditional on history and conditional variance at most $`(qp_P)^{-1}+(1-q)^{-1}`$. Put $`p_*=3^{-k}`$ and $`q=1-p_*/2`$. The residual increment has magnitude at most $`2/p_*`$ and conditional variance at most $`4/p_*`$. The centered calibration increment $`\Delta C_s-\kappa_{b,s}`$ has magnitude at most $`3/p_*`$ and conditional variance at most $`2/p_*`$. Freedman's inequality and a union bound over the targets and their supports give a deviation bound for either sum of order

```math
\sqrt{B\,3^k\log(M/\delta)}+3^k\log(M/\delta).
```

If each required support has average predictable contrast of magnitude at least $`\kappa_{\min}`$, this gives simultaneous additive error $`\epsilon`$ with probability at least $`1-\delta`$ in

```math
O\!\left(3^k\kappa_{\min}^{-2}\epsilon^{-2}\log(M/\delta)\right)
```

pairs. The choice of $`q`$ uses an expected $`O(\kappa_{\min}^{-2}\epsilon^{-2}\log(M/\delta))`$ pairs that contain two reference probes at this block budget. Every block still uses a reference in its second slot, and the overall allocation is a worst-case cap on detector calls.

### Matching weight dependence for product bases

A hard receiver attains the same exponential dependence on the weight. In each pair choose a fresh uniform bit string $`H`$ on the $`n`$ sites and an independent mask $`J`$ that equals zero with probability $`\kappa`$ and is uniform otherwise. On the computational basis outcomes $`X_1,X_2`$, report

```math
Y_1=X_1\oplus H\oplus J,\qquad Y_2=X_2\oplus H.
```

The first outcome is uniform. Using a known ideal zero in the second slot exposes $`H`$. Any other known second probe, even if chosen using the first record, can be simulated by adding a separately sampled ideal result from that probe. The zero reference therefore suffices in the lower-bound experiment.

On a support of size $`k`$, consider all $`3^k`$ Pauli strings $`P`$ with that support. Take a null source $`I/2^n`$ and alternatives $`(I+\theta P)/2^n`$. For arbitrary product Bloch axes chosen in the first slot of a block, let $`a_P`$ be the product of their projections onto the local axes of $`P`$. The relative record $`z=Y_1\oplus Y_2`$ has probability $`2^{-n}[1+\kappa\theta a_P(-1)^{s\cdot z}]`$ under alternative $`P`$ and is uniform under the null. Hence the null-to-alternative divergence in a signal block is $`-\tfrac12\log(1-\kappa^2\theta^2 a_P^2)`$. It is at most a constant times $`\kappa^2\theta^2 a_P^2`$ for $`\theta\le1/2`$. Since each Bloch axis has unit norm, $`\sum_P a_P^2=1`$ for every block.

For a protocol allowed to adapt bases and arms to prior data, use the divergence chain rule in the null distribution and sum over all alternatives. The total divergence is bounded by a constant times $`B\kappa^2\theta^2`$. Set $`\theta=4\epsilon`$ for $`\epsilon\le1/8`$. A uniformly accurate estimator for these observables distinguishes each alternative from the null by thresholding the relevant estimate at $`2\epsilon`$. The divergence for each such binary test is at least a constant times $`\log(1/\delta)`$ for $`\delta\le1/4`$, so the number of pairs is

```math
\Omega\!\left(3^k\kappa^{-2}\epsilon^{-2}\log(1/\delta)\right).
```

This converse concerns product basis controls and one unknown source copy per pair. It matches the weight and contrast exponents of the simultaneous upper bound. The dependence on the number of targets and the bounds for other measurement architectures remain open here.
