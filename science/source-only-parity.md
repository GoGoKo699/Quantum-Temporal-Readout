# Source-only temporal parity

## Result

Copies of an unknown qubit can supply all inputs to a causal detector, even when each individual report is fair. If the average predictable two-report parity contrast has magnitude at least a known constant $`\kappa_*`$ during each acquisition phase, the optimal number of copies for estimating a signed Pauli expectation to additive error $`\epsilon`$ at fixed confidence is

```math
N_*(K,\epsilon)=\Theta_{\kappa_*}\!\left(\max\{\epsilon^{-2},\epsilon^{-4}/K\}\right),\qquad K\ge 2.
```

Here $`K`$ bounds the copies per block. Every block uses two physical detector calls on two scheduled outputs of a trusted pre-block unitary. For the stationary hard detector, separately rotating the two incoming copies leaves the sign ambiguous at any sample size. The general upper bound uses the full parity. The lower bound allows the full raw records and all experimenter coins.

## Access and contrast

Let $`z=\mathrm{Tr}(Z\rho)`$ be the target expectation. A trusted basis rotation handles the other Pauli axes. A block chooses $`2\le k\le K`$, acts unitarily on $`k`$ fresh independent source copies, and sends two designated output qubits to the same detector at fixed times. All other outputs are discarded. The second output may have to remain coherent until its scheduled call. The experimenter uses only classical memory between blocks. The permitted controls are pre-block unitaries on source copies and private classical randomization. All copies and both detector calls count, including those used in the pilot. The moment circuits use $`O(k)`$ gates, including the additional CNOT that encodes the desired observable into parity.

The detector may have arbitrary causal classical or quantum memory. Conditioned on the classical history before the block, the fresh input and detector memory are initially independent. The detector sees the two inputs and its own memory and outcomes. The fresh arm and local Pauli pads have no side channel to the detector. Timing and external signaling are held fixed across arms. Within the final phase, the linear moment can use a second compressor on otherwise discarded fresh copies, keeping the chosen width and schedule the same in both arms. The detector may have different history-dependent response in the pilot and estimation phases.

Let x denote the two ideal Z outcomes before pads, y the raw reports, r the private X-mask bits, and s=y⊕r. An independent private Z mask per slot makes the ideal input distribution diagonal when those coins are averaged. For the conditional four-outcome POVM F, averaging the two masks gives

```math
\Pr(s)=\sum_x p(x)\,\pi_t(s\oplus x),\qquad
\pi_t(e)=\tfrac14\sum_{u\in\{0,1\}^2}\langle u|F_{u\oplus e}|u\rangle.
```

This follows by changing variables from r to u=x⊕r. It applies to correlated or entangled scheduled outputs because the joint POVM is linear on both inputs. For the current block the conditional expectation of the corrected full parity W is κₜ times the ideal two-output Z parity, where κₜ is the parity mean under πₜ. The contrast is common to the current hidden arms conditional on the same pre-arm history. For uniform precision the model promises |κ̄|≥κ* on every acquisition phase of the estimator, almost surely over histories, where κ̄ is the average of the conditional κₜ over that phase and 0<κ*<1. The pilot phase and final interleaved phase can have different signed averages. A floor on individual |κₜ| allows cancellation and cannot substitute for this phase condition.

## Encoding and estimation

For designated target $`T`$ and a second output $`H`$, append a CNOT from $`H`$ to $`T`$. The operator identity

```math
\mathrm{CNOT}_{H\to T}^{\dagger}(Z_H Z_T)\mathrm{CNOT}_{H\to T}=Z_T
```

holds regardless of correlations between the two qubits. At width two, CNOT and identity give ideal parity means $`z`$ and $`z^2`$. For larger widths, first dephase each input independently in the target $`Z`$ basis using a private fair $`I/Z`$ choice. After averaging these coins the ideal inputs are independent diagonal qubits with sign mean $`z`$. The [reference-free sine compressor](https://github.com/GoGoKo699/Quantum-Reference-Free-Readout/blob/66e761e88e79d7a9b511f26bbecf2a3aa6d0b210/science/minimax.md#construct-two-moments-with-one-report-per-block) then produces $`f_m(z)=\mathrm{Im}[(\cos t+i z\sin t)^m]`$ from $`m+1`$ copies. Apply two compressors on disjoint groups to get $`f_m(z)^2`$ from the ideal parity of the two targets. Append the parity-encoding CNOT between the targets to obtain $`f_m(z)`$. Both arms consume $`2m+2`$ copies. The pilot uses two copies and the linear arm at width two.

In the data phase choose each arm with probability 1/2 independently on each block. Score 2W on its chosen arm and zero on the other. With r₀=fₘ(z), the two empirical means concentrate around κ̄r₀ and κ̄r₀² for the same realized predictable average κ̄. Subtracting the predictable mean term by term gives martingale differences with bounded conditional ranges. In B blocks, each error is O(√(log(1/δ)/B)) with the two bounds simultaneous. The phase length is fixed before the phase begins, conditionally on the pilot history. The pilot similarly estimates u=κ̄ₚz within its requested accuracy even when κ̄ₚ differs from κ̄.

The following fitting argument keeps its precision at z=0. For candidate pairs (U,V)=(κr,κr²) and (U′,V′)=(κ′r′,κ′r′²), the identity V−V′=r′(U−U′)+U(r−r′) and its swapped form give

```math
|U-U'|+|V-V'|\ge\kappa_*\max(|r|,|r'|)\,|r-r'|
```

when both contrast magnitudes exceed or equal κ* and r,r′ are in [−1,1]. The contrast can have either sign. Minimize the sum of absolute residuals over that compact gain range and the allowed response interval. The total distance between the fitted and true moment pairs is at most twice the total sampling error. At K=2 or 3 use r=z and moment precision of order ε², because max(|z|,|z′|)≥|z−z′|/2. This uses O(ε⁻⁴ log(1/δ)) copies and two physical calls per block.

For K≥4 take M=min(floor(K/2)−1,floor(ε⁻²)). Estimate the pilot mean to 1/(4√M) in O(M log(1/δ)) two-copy blocks. Let q=max(|û|,M⁻¹ᐟ²) and m=floor(q⁻²). On the pilot event, |z|√m≤5/(4κ*) and 1≤m≤M. For t=c/√m with c sufficiently small depending on κ*, fₘ has derivative of order √m on |z|≤min(1,2/(κ*√m)), as in the reference-free analysis. For z′ in this interval, the moment separation is at least a constant times m max(|z|,|z′|)|z−z′|.

- If q≤2/√M, then m≥M/8. Moment precision of order mε² uses O((m²ε⁴)⁻¹ log(1/δ)) blocks and O((Mε⁴)⁻¹ log(1/δ)) copies.
- If q>2/√M, then |z|≥|u|≥7q/8 and √m|z| is bounded below by a positive constant. Moment precision of order √mε uses O((mε²)⁻¹ log(1/δ)) blocks and O(ε⁻² log(1/δ)) copies.

The selected horizons respect the copy cap on all histories, including pilot failure. The union of the pilot and two moment deviation probabilities can be set to δ. The result is an upper bound on copies. It charges two calls for each block, without asserting a separately optimized detector-call law. At width two, without a contrast floor, the linear and quadratic scores also give a fixed-horizon confidence set by keeping candidates u with |V̂−uÛ| at most the martingale deviation threshold. Its width can be large when the parity contrast cancels or the source polarization is small.

## Full-record lower bound and the local-controls separation

For a hard stationary detector, measure each qubit ideally in $`Z`$. Draw a fair sign $`G`$ and an independent sign $`J`$ of mean $`\kappa`$ per block. For ideal signs $`X_1,X_2`$, report $`Y_1=X_1G`$ and $`Y_2=X_2GJ`$. The implementation is causal. Conditional on actions and experimenter coins, including the masks, the first raw report is an independent fair sign. The corrected full parity has mean $`\kappa\mathrm{Tr}(O\rho^{\otimes k})`$, with $`O=U^\dagger(Z\otimes Z\otimes I)U`$ in the output-slot ordering. The signed mask product converts corrected parity to raw parity. The second raw report follows from the first and the raw parity. Thus the KL bound applies to the full observable transcript, including masks. This exact reduction holds for the hard subfamily. General correlated detectors can provide more information in the individual reports.

Take two different κⱼ strictly between κ* and 1 and diagonal states ρⱼ=(I+zⱼZ)/2 with zⱼ=Θ(ε), κ₀z₀=κ₁z₁ and |z₀−z₁|>2ε. In the normalized Hilbert–Schmidt Pauli expansion of 2ᵏρⱼᵏ, the constant term drops out against traceless O and the linear term is matched. By orthogonality the squared difference of parity means is at most Σᵣ₌₂ᵏ binom(k,r)(κ₀z₀ʳ−κ₁z₁ʳ)². This is O(k²ε⁴) for kε²≤1. Bernoulli probabilities are bounded away from zero and one because the hard contrasts are strictly below one. For kε²>1 the relative entropy is bounded by a constant. The conditional chain rule for arbitrary between-block adaptation gives total relative entropy O(N min(ε²,Kε⁴)) for pathwise copy budget N. Binary testing gives the claimed lower bound and a log(1/δ) factor for small δ. A concrete width-two pair is (z,κ)=(3ε,1/2) and (6ε,1/4) when κ*≤1/4 and ε≤1/6. These match the linear mean and differ in the quadratic mean by 9ε²/2.

With separate single-copy rotations before the two slots, let a₁,a₂ be their readout-axis projections on Z. On the diagonal states the ideal parity mean is a₁a₂z². For the same fixed stationary hard detector the complete transcript has identical law at +z and −z, even with arbitrary previous-block adaptation and shared classical randomization. At width two the pre-block CNOT makes one arm odd in z. This is an operational distinction between product controls and a joint gate at the same source-copy and detector-call budgets. The output of that CNOT on diagonal inputs is a classically correlated mixture. The comparison does not establish an entanglement requirement or an impossibility for local many-copy processing.

## Attribution and ownership

Temporal Readout supplies the causal block POVM, private padding and a known-probe contrast estimator. Reference-Free Readout supplies the sine compressor, uniform moment inversion and matched-linear-response converse for one local report. The joint result identifies when two physical calls contain only one effective informative parity, even given the raw records and controls. It transfers the copy law to a causal detector with no known probes and gives an exact sign-identifiability separation against independently rotated source slots. Temporal Readout can own the joint proof. Reference-Free Readout can state the parity encoding and contrast this interface with its two independent physical reports, which yield two informative moments within one block.

Lin, Wallman, Hincks and Laflamme, *Phys. Rev. Research* 3, 033285 (2021), Sec. III and Eqs. (8)–(11), provide the preparation/readout separation via a CNOT moment ratio. Van den Berg, Minev and Temme, *Phys. Rev. A* 105, 032620 (2022), Protocols 1–2 and Thm. IV.2, give calibrated multiplicative parity attenuation under randomized readout. Xiao et al., arXiv:2502.11772, use multiple processes for simultaneous tomography with different informational access. Huo and Li, *Commun. Theor. Phys.* 73, 075101 (2021), address self-consistent process tomography with correlated errors. Neither the moment ratio nor the parity twirl is claimed as a new primitive here. The access comparison and copy bound concern the specific two-call, source-only experiment defined above. Timing or control leakage, within-pair feedback, trusted fresh references and additional output channels change that experiment.

The [Watrous learning bridge](../learning/WATROUS_BRIDGE.md) connects the conditional detector POVM, the pulled-back observable and binary testing to the common textbook. The [finite verification](../verification/README.md) checks the raw likelihood, blind marginals, parity encoding, sign ambiguity and conditional interleaving on explicit examples.

Pinned sources: [Temporal Readout](https://github.com/GoGoKo699/Quantum-Temporal-Readout/tree/bd79ec742cc3ff8e743e8c4b2e07a30edc2df47f), [Reference-Free Readout](https://github.com/GoGoKo699/Quantum-Reference-Free-Readout/tree/66e761e88e79d7a9b511f26bbecf2a3aa6d0b210), [Watrous](https://cs.uwaterloo.ca/~watrous/TQI/), [Lin et al.](https://arxiv.org/abs/1910.07511), [van den Berg et al.](https://arxiv.org/abs/2012.09738), [Xiao et al.](https://arxiv.org/abs/2502.11772).
