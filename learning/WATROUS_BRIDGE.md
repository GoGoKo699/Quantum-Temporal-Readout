# From Watrous to temporal readout

John Watrous, *The Theory of Quantum Information*, Cambridge University Press, April 2018, ISBN 978-1-107-18056-7. The locators below follow the published edition and its matching [author-hosted reading copy](https://cs.uwaterloo.ca/~watrous/TQI/). See the [publisher's contents](https://assets.cambridge.org/97811071/80567/toc/9781107180567_toc.pdf).

## Reading route

| Watrous locator | Foundation | Use in this project |
|---|---|---|
| §1.2.2, Probability theory, p. 47 | Random variables, expectation, and uncertainty | Binary signs, conditioning on the experiment record, and concentration of averages |
| §§2.1.2–2.1.3, Quantum states and their reductions, pp. 61 and 67 | Density operators, tensor factors, and reduced states | Model a fresh source probe separately from detector memory and combine scheduled inputs into a block |
| §§2.2.1–2.2.3, Quantum channels, pp. 72–95 | Trace-preserving dynamics and classical or quantum outputs | Keep each detector stage causal while allowing a quantum memory and a public bitstring |
| §§2.3.1–2.3.2, Measurements, pp. 100–112 | Measurement operators, POVMs, and outcome statistics | Represent the ideal and actual block readout and read off the effect of private Pauli averaging |
| §3.1.1, Discriminating between pairs of states, p. 125 | Distinguishability of two preparations via measured data | Understand why two separated values of the target mean imply a binary testing problem |
| §5.1.1, Classical entropic functions, p. 250 | Classical relative entropy | Read the statistical lower bound on estimating the target from the full detector transcript |

## Translation

| Object | Meaning here |
|---|---|
| Input density operator | The same unknown state $`\rho`$ is freshly prepared on each signal block. Pilots are fresh known input states. |
| Measurement outcome distribution | An ideal computational measurement returns bits. Trusted local basis rotations make a prescribed Pauli expectation the mean of the corresponding ideal parity sign. |
| Detector channel | Each invocation takes a probe and the current detector memory, emits a classical outcome, and updates the memory. |
| Block measurement | Conditioned on the record before a block, the accessible joint outcome is described by POVM effects on the scheduled inputs. The block can consist entirely of destructive reads. |
| Reduced record | Keeping just one slot marginalizes over the other outputs. A uniform marginal can coexist with a joint distribution whose parity is informative. |
| Binary discrimination | If a mean estimator works at both $`\mu=2\epsilon`$ and $`\mu=-2\epsilon`$, testing the sign of its estimate distinguishes the two transcript laws. |

## From the textbook to the proofs

The measurement sections give the quantum probability formula. The [detector model](../science/model.md) adds a history-conditioned block and private Pauli masks. A phase mask removes off-diagonal contributions when averaged, and a bit mask followed by output correction averages the classical response over translations. The result is an input-independent additive error on the **corrected joint record**. Its bits may be correlated through the detector's memory.

The [calibration argument](../science/calibration.md) selects a bounded score using the first corrected parity and the pilot outcomes. A hidden arm switch lets a signal block and an all-reference block measure the same predictable contrast, with the signal block also carrying the unknown expectation. Concentration applies to the difference of the two arms after centering by the candidate expectation. This step uses a martingale bound because the detector can drift across blocks.

The [context-cost theorem](../science/context-cost.md) applies classical testing to a detector whose unknown deterministic correction depends on a uniformly sampled context. Reference blocks learn some entries, so the constructive procedure decodes signal blocks with matching contexts. The converse bounds how many samples can land in repeated contexts, where the sign of the source mean can become identifiable. These two arguments give the attained block budget in this stationary family.

The [source-only sister result](../science/source-only-parity.md) uses the same conditional block measurement, now with two outputs from one pre-block circuit. In §§2.1–2.3, follow the tensor product through that circuit and pull the two-slot observable $`Z\otimes Z`$ back through a CNOT. Identity leaves its ideal mean at $`z^2`$ on two fresh copies, and CNOT changes it to $`z`$. The two arms therefore probe the same unknown detector contrast with two different source moments. The testing and entropy sections explain why lower bounding the copy budget requires comparing the complete two-report distributions. The martingale argument in the proof handles the drift across blocks.

Read the [worked example](WORKED_EXAMPLE.md) after §2.3 if the block probabilities are unfamiliar. The [milestones](MILESTONES.md) connect each imported concept to its point of use in the scientific story.
