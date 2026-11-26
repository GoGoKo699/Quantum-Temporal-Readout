# Temporal readout model

A detector consumes a register and returns classical bits. If its electronics sometimes invert the reported polarity, a whole sequence can preserve information about the register even when every single result is fair. The experiment sends a known reference through the *same* detector so that its result carries information about the error on the source measurement.

## Access and resources

The source supplies independent fresh copies of one unknown $`n`$-qubit state $`\rho`$. The detector consumes one $`n`$-qubit probe at each of $`L`$ aligned slots and returns an $`n`$-bit report. It has arbitrary causal classical or quantum memory, including between blocks. Conditioned on all experimenter history before a block, the detector's retained state and the new source and reference probes are initially independent. The detector receives the masked probes and has no side channel to the current arm assignment, basis setting or mask. The experimenter uses trusted preparations and product rotations, independent private Pauli masks and a classical record. One block contains at most one unknown source copy, in its first slot. All other probes are known references. Inputs within a block are scheduled before the outputs are seen.

To estimate a Pauli expectation $`\mu=\mathrm{Tr}(P\rho)`$, rotate the nonidentity factors of $`P`$ to $`Z`$ with a product unitary. Let $`s`$ be the support of $`P`$ and let $`\chi_s(x)=(-1)^{s\cdot x}`$ denote the corresponding binary character. The ideal outcome in the first slot then has mean parity $`\mu`$. Each pilot is $`|0\rangle^{\otimes n}`$, so its ideal outcome is the all-zero string. An all-reference block uses that same state in the first slot. A length-$`L`$ block costs $`L`$ detector calls, including pilots, and the necessary reference preparations. Only classically stored data survive each call on the experimenter side.

## From a causal detector to additive error

Write $`d=2^{nL}`$ for the block input dimension. For each fixed pre-block history, causality and linearity give a POVM $`\{F_y\}`$ on the full input space, indexed by the concatenated reports $`y`$. One can obtain it by composing the instruments, contracting the initial detector state and taking the final trace, while leaving all scheduled input registers open. The resulting effects are positive and sum to identity. They can depend on the history and block index.

Apply $`X^r Z^v`$ to the inputs for independent uniform $`nL`$-bit strings $`r,v`$. Correct the output by setting $`z=y\oplus r`$. Let $`p(x)`$ be the ideal computational-basis distribution of the complete input. Averaging over $`v`$ deletes its off-diagonal entries. Conditional on $`r`$, the padded basis state corresponding to $`x`$ is $`|x\oplus r\rangle`$. Changing variables to $`u=x\oplus r`$ gives

```math
\begin{aligned}
\Pr(z)&=\sum_x p(x)\,\pi(z\oplus x),\\
\pi(e)&=\frac{1}{d}\sum_u\langle u|F_{u\oplus e}|u\rangle.
\end{aligned}
```

The numbers $`\pi(e)`$ are nonnegative and sum to one. In the corrected record averaged over the private masks, $`z=x\oplus e`$ with input-independent additive noise $`e`$. All temporal and spatial correlations of $`\pi`$ are allowed. The identity involves the corrected record. Keeping the mask as an additional statistical variable changes the experiment. With hidden arm and basis choices drawn independently of the current detector state, the same conditional $`\pi`$ applies to both arms and all settings.

## Pilot-conditioned contrast

Write $`R=e_{2:L}`$ for the concatenated pilot reports after mask correction. These reports equal the pilot errors. Let $`A=\chi_s(e_1)`$ and $`m(R)=\mathbb{E}[A\mid R]`$. For a known bounded real function $`w`$, use the block score $`w(R)\chi_s(z_1)`$. Its expectation is $`\mu\kappa`$ on a source block and $`\kappa`$ on an all-reference block, where $`\kappa=\mathbb{E}[w(R) A]`$. The function can be chosen from earlier blocks only, so both equalities hold conditionally under drift. The [calibration procedure](calibration.md) estimates the expectation without knowing the contrast in advance.

For the stationary one-Pauli family $`\rho_\mu=(I+\mu P)/2^n`$, when the chosen product setting measures $`P`$, the corrected first bitstring has conditional density $`2^{-n}[1+\mu\,m(R)\chi_s(z_1)]`$. Its support parity and the pilot record are sufficient for this family. The Fisher information of a source block is

```math
I(\mu)=\mathbb{E}\left[\frac{m(R)^2}{1-\mu^2m(R)^2}\right],\qquad |\mu|<1.
```

The formula follows by summing the two Bernoulli signs conditionally on $`R`$. In particular $`I(0)=\mathbb{E}[m(R)^2]`$. The sign-weighted score with $`w=m`$ has variance $`I(0)`$ and derivative $`I(0)`$ at zero, attaining the local information if the detector law is known. The corrected block experiment is informative precisely when $`m`$ is nonzero with positive probability. The characters of the pilot string span its functions, so a nonzero $`m`$ implies a nonzero contrast with at least one pilot parity. A single parity may be weak even when the full pilot record is informative. The [context model](context-cost.md) makes the cost of learning its decoder explicit.

## Information at an exact temporal order

Use one qubit per slot. Let the detector measure each probe in $`Z`$, then add a uniformly random $`L`$-bit error mask of even parity. The mask is independent between aligned blocks, and the detector can implement this law by keeping a running parity and a slot counter. Fixing any $`j<L`$ error bits leaves $`2^{L-j-1}`$ equally likely completions. Every proper marginal of the error mask is uniform, which also makes every proper subset of corrected reports uniform for any fixed input distribution. With zero-state pilots, the full corrected parity is exactly the ideal source bit. For $`L=2`$, the two reported bits have the same fair random flip. Independent fair flips at all slots erase the entire joint record.

The witness uses only classical detector memory. The method also accepts a detector with genuinely quantum internal memory by the conditional POVM reduction. The zero-information statement concerns the proper subsets of the specified aligned block experiment, with no analogue record or bypass measurement available.
