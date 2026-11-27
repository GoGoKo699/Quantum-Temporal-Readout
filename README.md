# Quantum Temporal Readout

**Can a destructive detector recover a Pauli expectation when every individual reading is independent of its input?** Yes, if a known reference sent through the same detector reveals the error on the source probe. For example, a shared fair polarity makes both individual readings fair. Multiplying the two corrected signs cancels the polarity and recovers the ideal source sign.

The reference protocol uses trusted product rotations, private local Pauli masks and fresh reference probes. The detector may retain arbitrary classical or quantum memory and drift between blocks. Randomly interleaved all-reference blocks certify a Pauli expectation from the measured temporal contrast.

| Result | Scientific account |
|---|---|
| At any block length, every proper subset of reports can be blind while full parity recovers the ideal source sign exactly. | [Detector model and temporal order](science/model.md) |
| A confidence set remains valid under arbitrary causal drift. Its width is set by the observed contrast. Shared calibration estimates multiple product-basis Pauli targets. | [Calibration and inference](science/calibration.md) |
| Matching upper and lower bounds quantify the cost of learning a hidden sign decoder from unstructured reference contexts. | [Calibration cost](science/context-cost.md) |
| A thresholded phase model connects the contrast to the readout delay and quantifies sensitivity to control leakage. | [Phase drift and control](science/physical-model.md) |

For one target at effective block contrast at least $`\kappa>0`$, additive accuracy $`\epsilon`$ and failure probability $`\delta`$ take $`O(\kappa^{-2}\epsilon^{-2}\log(1/\delta))`$ blocks. In the unstructured stationary sign-decoder family with $`D`$ equiprobable contexts, the minimax order at fixed confidence is

```math
\Theta\!\left(\max\left\{\epsilon^{-2},\frac{\sqrt{D}}{\epsilon}\right\}\right)
```

blocks. A block of length $`L`$ costs $`L`$ detector calls, even when its pilot record fails to match the reference dictionary. The source is fixed across the run. The digital-only interface uses trusted controls and keeps the current arm, basis setting and masks private from the detector. A low or cancelling contrast gives a broad confidence set. An analogue phase-reference receiver changes the access model.

## Estimate a Pauli expectation with references

1. Choose the target Pauli string and fix the number of blocks and the timing of the calls. Draw a private fair bit for each block. In the signal arm, take one fresh copy of the fixed source and rotate the target axes to the computational basis. In the reference arm, prepare a fresh all-zero register of the same size. Put that register or the rotated copy in the first slot and use fresh all-zero references for all later slots.
2. Apply independent private local Pauli masks in every slot. Send each register to the same destructive detector at its scheduled time and undo the bit flips in the reported strings by XOR with the private X-mask bits. In a two-call block, multiply the corrected parity signs on the target support. For more calls, choose a [bounded scoring function](science/calibration.md#the-experiment) from earlier blocks before drawing the current arm. Evaluate it on the current corrected pilot record and multiply the result by the first-slot parity on the target support.
3. Keep separate classical sums for the two arms, weighting each recorded score by two. Use the clipped signal-to-reference ratio when the reference sum is nonzero. Compute the [confidence set](science/calibration.md#confidence-set-and-resource-cost) by testing which candidate means make the signal sum agree with that multiple of the reference sum. An empty set or one too broad for the requested precision can lead to abstention.

Fresh probes start independent of detector memory conditional on the earlier records. The detector may keep its memory and change its response between blocks. The precision bound uses the magnitude of the average predictable contrast, so contrasts of opposite signs can cancel. Count every source copy, reference preparation and detector call in both arms. The [worked example](learning/WORKED_EXAMPLE.md) follows the scores through a two-call experiment.

## Source-only temporal parity

The [sister result with Quantum Reference-Free Readout](https://github.com/GoGoKo699/Quantum-Reference-Free-Readout/blob/main/science/temporal-parity.md) uses only fresh copies of the unknown qubit. A trusted pre-block circuit prepares two outputs for separate scheduled detector calls and encodes two different moments in the same corrected parity. The second output may need to remain coherent until its call.

At width two, rotate two fresh copies to the target basis. In each data block use an independent private fair bit to choose between a CNOT and the identity. A CNOT from the other qubit to the target makes the ideal two-output parity equal the target's original Z sign. With the identity the ideal parity is a product of two signs, with mean equal to the square of the target expectation. Apply private Pauli masks, make both fixed-time calls and XOR away the X-mask bits before computing the full parity. Fit the two arms' means over the unknown signed contrast and the allowed target range.

For larger blocks, the [existing estimator](science/source-only-parity.md#encoding-and-estimation) uses a two-copy pilot to choose the width and runs two sine compressors on disjoint groups of fresh copies. The final arms have the same width and timing. The pilot and final phase each need a floor on the magnitude of their own average contrast. Count all pilot and data copies, both calls per block and a gate count linear in the number of copies used in the block. Between blocks the experimenter keeps only classical data.

With at most $`K\ge 2`$ source copies per block and a fixed positive floor on the magnitude of the average predictable parity contrast in each acquisition phase, the optimal copy cost at fixed confidence is

```math
\Theta\!\left(\max\left\{\epsilon^{-2},\frac{\epsilon^{-4}}{K}\right\}\right).
```

The [source-only proof](science/source-only-parity.md) includes a detector on which both reports are individually fair. Separate single-copy rotations leave the sign of the expectation unidentifiable for that detector. A joint CNOT makes the sign identifiable at width two. Both calls count in every block.

## Read or reproduce

- [Scientific account](science/README.md) for the model, theorems and resource bounds.
- [Learning guide](learning/README.md) for the Watrous bridge, worked examples and 30-milestone route.
- [Related work](references/RELATED_WORK.md) for attribution and comparisons.
- [Verification](verification/README.md) for deterministic checks. Run `python3 verification/run_all.py` from the repository root after installing `verification/requirements.txt`.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
