# Project understanding map

The **30 milestones** are divided into **12 background/preliminaries** and **18 narrative/innovation** milestones. The background builds from state and measurement to a complete experimental interface. The narrative first derives what a block record can retain, then develops the calibration and sample-cost arguments.

The map applies to any reader. Use the [Watrous bridge](WATROUS_BRIDGE.md) for the educational source and the [scientific account](../science/README.md) for full statements and proofs.

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | [M01](#m01-bits-and-signs)–[M04](#m04-product-pauli-measurements) | Ideal signs, fresh copies, and product Pauli measurements |
| Background/preliminaries | [M05](#m05-a-destructive-detector-with-memory)–[M09](#m09-known-pilot-outcomes) | Causal detectors, private controls, and useful pilot records |
| Background/preliminaries | [M10](#m10-sampling-and-a-finite-interval)–[M12](#m12-the-full-measurement-task) | Statistical uncertainty, distinguishability, and measured resources |
| Narrative/innovation | [M13](#m13-one-effect-per-block-record)–[M18](#m18-combining-pilot-records) | Additive block noise, the temporal hierarchy, and pilot-conditioned information |
| Narrative/innovation | [M19](#m19-matching-signal-and-reference-blocks)–[M23](#m23-several-pauli-expectations) | Hidden interleaving, drift-valid confidence, and multi-observable acquisition |
| Narrative/innovation | [M24](#m24-a-hidden-context-dependent-correction)–[M28](#m28-the-matching-lower-bound) | Construction and converse for the paid context decoder |
| Narrative/innovation | [M29](#m29-a-physical-source-of-temporal-contrast)–[M30](#m30-the-complete-temporal-readout-story) | Physical interpretation and synthesis |

## Background and preliminaries

### M01 Bits and signs
01
**Central question.** How does a computational outcome become a sample of an observable?

**Understanding target.** Map a bit to a sign with outcomes plus and minus one. Relate its mean to the probability of the positive sign.

**Prerequisites.** None.

**Conceptual connection.** Multiplying signs takes parity of the underlying bits, so a product of readout signs can estimate a single observable.

**Sources.** [Detector model and temporal information](../science/model.md#access-and-resources).

### M02 States and fresh copies
02
**Central question.** Where is the unknown information at the start of each signal block?

**Understanding target.** Treat the probe as a density operator prepared independently of earlier experiment records and detector memory. Identify the known pilot as a separate preparation.

**Prerequisites.** [M01](#m01-bits-and-signs).

**Conceptual connection.** Fresh copies allow the same expectation to appear in every block even when the detector changes.

**Sources.** [Detector model and temporal information](../science/model.md#access-and-resources). See the [relevant Watrous foundations](WATROUS_BRIDGE.md#reading-route).

### M03 Ideal outcome probabilities
03
**Central question.** What defines the ideal outcome distribution for a fixed preparation?

**Understanding target.** Use the Born rule to obtain probabilities from state and measurement effects. Distinguish the target distribution from the corrected and uncorrected detector records.

**Prerequisites.** [M01](#m01-bits-and-signs), [M02](#m02-states-and-fresh-copies).

**Conceptual connection.** The project estimates a feature of the ideal distribution using records from a different measurement.

**Sources.** [Detector model and temporal information](../science/model.md#from-a-causal-detector-to-additive-error). See the [relevant Watrous foundations](WATROUS_BRIDGE.md#reading-route).

### M04 Product Pauli measurements
04
**Central question.** How does a chosen product basis expose a Pauli expectation?

**Understanding target.** Rotate each nonidentity local Pauli to the computational measurement basis and take parity on its support. Interpret weight as the number of nonidentity factors.

**Prerequisites.** [M01](#m01-bits-and-signs), [M03](#m03-ideal-outcome-probabilities).

**Conceptual connection.** A support selects a parity function. Different local axes on that support measure different expectations.

**Sources.** [Detector model and temporal information](../science/model.md#access-and-resources).

### M05 A destructive detector with memory
05
**Central question.** How can a destructive read leave information for a later call?

**Understanding target.** Model a single detector call as an operation that consumes a probe, outputs a bitstring, and updates internal memory that may be quantum.

**Prerequisites.** [M02](#m02-states-and-fresh-copies), [M03](#m03-ideal-outcome-probabilities).

**Conceptual connection.** The next call can depend on an internal state even if the experimenter receives only digital output.

**Sources.** [Detector model and temporal information](../science/model.md#access-and-resources). See the [relevant Watrous foundations](WATROUS_BRIDGE.md#reading-route).

### M06 Causal order and history
06
**Central question.** Which variables may influence the detector in a block?

**Understanding target.** Separate the known past from the current hidden arm, basis, and masks. Identify the scheduled quantum inputs available causally to the detector.

**Prerequisites.** [M02](#m02-states-and-fresh-copies), [M05](#m05-a-destructive-detector-with-memory).

**Conceptual connection.** Conditioning on the full prior history permits cross-block memory without giving the detector future control choices.

**Sources.** [Detector model and temporal information](../science/model.md#access-and-resources).

### M07 Private Pauli masks
07
**Central question.** Which part of the pad is undone in a classical report?

**Understanding target.** Distinguish the phase part of a full Pauli pad from the bit-flip part. Undo the bit flip in the report and average over both privately chosen parts.

**Prerequisites.** [M01](#m01-bits-and-signs), [M04](#m04-product-pauli-measurements), [M06](#m06-causal-order-and-history).

**Conceptual connection.** The phase average will remove quantum coherences from the effective response. Output correction will retain the ideal bit labeling.

**Sources.** [Detector model and temporal information](../science/model.md#from-a-causal-detector-to-additive-error).

### M08 Marginals and joint records
08
**Central question.** Can two individually fair reports have an informative product?

**Understanding target.** Distinguish the distribution of a single slot from the distribution of the whole block. Compare shared fair flips with fresh independent fair flips.

**Prerequisites.** [M01](#m01-bits-and-signs), [M05](#m05-a-destructive-detector-with-memory).

**Conceptual connection.** The same marginal detector behavior can lead to different predictions for joint parity.

**Sources.** [One-qubit example](WORKED_EXAMPLE.md#the-two-shot-block).

### M09 Known pilot outcomes
09
**Central question.** What information does a known reference add to a signal block?

**Understanding target.** Use a pilot with a deterministic ideal bit pattern to reveal the corresponding corrected noise pattern in the additive model.

**Prerequisites.** [M03](#m03-ideal-outcome-probabilities), [M07](#m07-private-pauli-masks), [M08](#m08-marginals-and-joint-records).

**Conceptual connection.** A pilot can expose context for how to interpret the first output. Its value comes from correlation with that output.

**Sources.** [Detector model and temporal information](../science/model.md#pilot-conditioned-contrast).

### M10 Sampling and a finite interval
10
**Central question.** Why does an observed average need an uncertainty bound?

**Understanding target.** Distinguish the mean of a bounded score from its observed value. Understand coverage of a confidence set at a fixed budget and how its width expresses available precision.

**Prerequisites.** [M01](#m01-bits-and-signs), [M06](#m06-causal-order-and-history).

**Conceptual connection.** The calibration method will keep the conditional target fixed while allowing the detector contrast to vary.

**Sources.** [Finite-sample calibration](../science/calibration.md#confidence-set-and-resource-cost). See the [relevant Watrous foundations](WATROUS_BRIDGE.md#reading-route).

### M11 From estimation to testing
11
**Central question.** How can a binary test constrain the best possible estimation rate?

**Understanding target.** Choose two parameter values whose error intervals are disjoint. A successful estimator supplies a test between the corresponding transcript distributions.

**Prerequisites.** [M03](#m03-ideal-outcome-probabilities), [M10](#m10-sampling-and-a-finite-interval).

**Conceptual connection.** A bound on how quickly the complete transcript distinguishes the two values applies to all estimators in the experiment.

**Sources.** [Context-decoding cost](../science/context-cost.md#lower-bound-with-adaptive-acquisition). See the [relevant Watrous foundations](WATROUS_BRIDGE.md#reading-route).

### M12 The full measurement task
12
**Central question.** What are the operational inputs, outputs and costs?

**Understanding target.** Specify the unknown fresh source, trusted input operations, secret choices, accessible digital record and fixed detector-call budget. Count all pilot and all-reference reads.

**Prerequisites.** [M04](#m04-product-pauli-measurements), [M06](#m06-causal-order-and-history), [M07](#m07-private-pauli-masks), [M09](#m09-known-pilot-outcomes), [M11](#m11-from-estimation-to-testing).

**Conceptual connection.** These basic choices determine which readout information the experiment can access and which lower bounds apply.

**Sources.** [Detector model and temporal information](../science/model.md#access-and-resources).

## Narrative and contribution

### M13 One effect per block record
13
**Central question.** How can repeated causal measurements be represented in a joint probability formula?

**Understanding target.** Condition on the experimenter history and describe the conditional probability of every block outcome using a POVM on the scheduled input registers.

**Prerequisites.** [M05](#m05-a-destructive-detector-with-memory), [M06](#m06-causal-order-and-history), [M12](#m12-the-full-measurement-task).

**Conceptual connection.** Internal memory is absorbed into the effects. Inner-block time ordering still determines which inputs and outputs are physically available.

**Sources.** [Detector model and temporal information](../science/model.md#from-a-causal-detector-to-additive-error).

### M14 Phase averaging
14
**Central question.** Why is the corrected response governed by computational probabilities?

**Understanding target.** Average the input state over independent phase masks and see why unequal computational strings acquire canceling phases.

**Prerequisites.** [M07](#m07-private-pauli-masks), [M13](#m13-one-effect-per-block-record).

**Conceptual connection.** This removes a dependence of the final averaged response on the input's phase coherences in the rotated basis.

**Sources.** [Detector model and temporal information](../science/model.md#from-a-causal-detector-to-additive-error).

### M15 Translation averaging
15
**Central question.** How do private flips make the corrected error independent of the ideal bits?

**Understanding target.** Average the classical conditional response over randomized bit translations with the associated output correction. Interpret the resulting corrected record as ideal bits plus an additive block error.

**Prerequisites.** [M07](#m07-private-pauli-masks), [M14](#m14-phase-averaging).

**Conceptual connection.** The error law can change with earlier history and correlate different slots. Independence from the ideal readout within the current conditional law makes the scalar calibration possible.

**Sources.** [Detector model and temporal information](../science/model.md#from-a-causal-detector-to-additive-error).

### M16 Canceling the shared polarity
16
**Central question.** How does the two-call protocol recover a signal each call hides?

**Understanding target.** Multiply the corrected sign of a signal probe by the corrected sign of a known pilot. Use the shared fair polarity to show exact cancellation in the noiseless shared-sign case.

**Prerequisites.** [M08](#m08-marginals-and-joint-records), [M09](#m09-known-pilot-outcomes), [M15](#m15-translation-averaging).

**Conceptual connection.** This is the smallest example where the information available in time exceeds the information in any one slot.

**Sources.** [One-qubit example](WORKED_EXAMPLE.md#the-two-shot-block).

### M17 Information first appears at a chosen block length
17
**Central question.** Can all proper subsets be blind while the full product recovers the ideal sign?

**Understanding target.** Follow the construction that draws an even-parity error string. Every proper projection is uniform, while the product of all error signs is fixed.

**Prerequisites.** [M15](#m15-translation-averaging), [M16](#m16-canceling-the-shared-polarity).

**Conceptual connection.** The separation is about the accessible record. Measuring the same one-slot channel more accurately cannot reveal a parity that first appears at a larger temporal order.

**Sources.** [Detector model and temporal information](../science/model.md#information-at-an-exact-temporal-order).

### M18 Combining pilot records
18
**Central question.** What should a decoder predict from all the pilot outputs?

**Understanding target.** Read the conditional mean of the first error sign as a function of the pilot outcomes. Connect this quantity to an informative score and to the local Fisher information in the stationary one-parameter model.

**Prerequisites.** [M09](#m09-known-pilot-outcomes), [M15](#m15-translation-averaging), [M17](#m17-information-first-appears-at-a-chosen-block-length).

**Conceptual connection.** An average first-slot sign can cancel while a pilot-conditioned sign has predictable magnitude.

**Sources.** [Detector model and temporal information](../science/model.md#pilot-conditioned-contrast).

### M19 Matching signal and reference blocks
19
**Central question.** How does calibration measure the same contrast as data acquisition?

**Understanding target.** Randomize the first preparation privately between a source and the zero-state reference while keeping later pilots and scheduled controls matched. Identify the resulting conditional means of one score.

**Prerequisites.** [M09](#m09-known-pilot-outcomes), [M15](#m15-translation-averaging), [M18](#m18-combining-pilot-records).

**Conceptual connection.** Signal and all-reference blocks have the same predictable contrast. The signal arm carries an extra factor equal to the unknown target mean.

**Sources.** [Finite-sample calibration](../science/calibration.md#the-experiment).

### M20 A residual with zero conditional mean
20
**Central question.** Which statistic remains centered when the detector drifts?

**Understanding target.** Weight the arm scores by reciprocal assignment probabilities and subtract the reference sum multiplied by the candidate target mean. At the true mean, the residual increments have zero conditional expectation.

**Prerequisites.** [M10](#m10-sampling-and-a-finite-interval), [M19](#m19-matching-signal-and-reference-blocks).

**Conceptual connection.** A bounded martingale preserves inference under dependent blocks while the separate signal and reference averages can drift.

**Sources.** [Finite-sample calibration](../science/calibration.md#confidence-set-and-resource-cost).

### M21 Coverage and usable contrast
21
**Central question.** When does the finite confidence set become narrow?

**Understanding target.** Invert the bounded-martingale inequality for the target mean and identify the magnitude of the observed reference sum as the width-controlling quantity. Consider what happens when contrast changes sign across blocks.

**Prerequisites.** [M10](#m10-sampling-and-a-finite-interval), [M20](#m20-a-residual-with-zero-conditional-mean).

**Conceptual connection.** Coverage follows from centering at the true mean. Precision needs an observed or assumed bound on the combined contrast.

**Sources.** [Finite-sample calibration](../science/calibration.md#confidence-set-and-resource-cost).

### M22 The trusted input boundary
22
**Central question.** Why do secret controls matter even when a detector is causal?

**Understanding target.** Take a detector that reacts to leaked arm metadata and see how the signal and reference laws can become different. Identify trusted reference preparation and basis controls as conditions on the measurement interface.

**Prerequisites.** [M06](#m06-causal-order-and-history), [M07](#m07-private-pauli-masks), [M19](#m19-matching-signal-and-reference-blocks).

**Conceptual connection.** The martingale numerator is centered by matched assignment, so a mismatch in what the detector sees can become a systematic residual.

**Sources.** [Finite-sample calibration](../science/calibration.md#confidence-set-and-resource-cost).

### M23 Several Pauli expectations
23
**Central question.** How can the same reference blocks calibrate multiple observables?

**Understanding target.** Match a random product basis to each target on its support and retain the same support parity across reference blocks. Explain the decreasing match probability at higher Pauli weight.

**Prerequisites.** [M04](#m04-product-pauli-measurements), [M19](#m19-matching-signal-and-reference-blocks), [M21](#m21-coverage-and-usable-contrast).

**Conceptual connection.** Shared calibration economizes the references while the basis matching cost still grows with the observable's weight.

**Sources.** [Finite-sample calibration](../science/calibration.md#one-stream-for-many-pauli-observables) and [product-basis converse](../science/calibration.md#matching-weight-dependence-for-product-bases).

### M24 A hidden context-dependent correction
24
**Central question.** Why does a simple sign recovery rule need calibration data?

**Understanding target.** Trace the stationary detector whose pilots reveal a uniformly sampled context and a fair extra flip. After removing the extra flip, each context has an unknown, fixed correction sign.

**Prerequisites.** [M16](#m16-canceling-the-shared-polarity), [M18](#m18-combining-pilot-records), [M22](#m22-the-trusted-input-boundary).

**Conceptual connection.** A known table recovers every ideal sign. An unknown table makes the information in a first encounter with a context inaccessible through that signal alone.

**Sources.** [Context-decoding cost](../science/context-cost.md#a-detector-with-hidden-contexts).

### M25 Reference coverage and context matches
25
**Central question.** How do calibration and signal samples cooperate?

**Understanding target.** Build a dictionary from all-reference blocks and use a signal only if its context was seen in calibration. Explain why uniform independent contexts make retention independent of the ideal signal sign.

**Prerequisites.** [M09](#m09-known-pilot-outcomes), [M24](#m24-a-hidden-context-dependent-correction).

**Conceptual connection.** The number of covered contexts determines the fraction of signal samples that produce a correctly decoded sign.

**Sources.** [Context-decoding cost](../science/context-cost.md#upper-bound-by-matching-context-records).

### M26 Two regimes for the constructive budget
26
**Central question.** What determines whether encounters or ordinary sampling dominate?

**Understanding target.** Account for coverage when the dictionary is small relative to the context space and when it occupies a constant fraction. Combine the resulting match rate with the number of decoded signs needed for accuracy.

**Prerequisites.** [M10](#m10-sampling-and-a-finite-interval), [M24](#m24-a-hidden-context-dependent-correction), [M25](#m25-reference-coverage-and-context-matches).

**Conceptual connection.** The upper bound trades reference acquisition against the chance of a signal match while counting both arms and unmatched blocks.

**Sources.** [Context-decoding cost](../science/context-cost.md#upper-bound-by-matching-context-records).

### M27 Why singleton contexts cannot distinguish the signs
27
**Central question.** What information remains without a repeated context?

**Understanding target.** Randomize the unknown table entries in the lower-bound test. Explain why a singleton encountered in a signal block has an unbiased observed sign under either hypothesis, and a singleton calibration reveals only a fresh table entry.

**Prerequisites.** [M11](#m11-from-estimation-to-testing), [M24](#m24-a-hidden-context-dependent-correction).

**Conceptual connection.** Even a stronger experiment told the contexts and the repeated-context table entries gains distinguishing evidence only at repeated contexts.

**Sources.** [Context-decoding cost](../science/context-cost.md#lower-bound-with-adaptive-acquisition).

### M28 The matching lower bound
28
**Central question.** How do repeated-context counts and statistical accuracy combine?

**Understanding target.** Bound the expected number of indices in repeated contexts by the smaller of the full sample size and the pair-collision bound. Multiply this by the divergence scale of one informative sign and compare with a fixed-confidence test.

**Prerequisites.** [M11](#m11-from-estimation-to-testing), [M26](#m26-two-regimes-for-the-constructive-budget), [M27](#m27-why-singleton-contexts-cannot-distinguish-the-signs).

**Conceptual connection.** The encounter-limited and ordinary sampling terms are both necessary, giving the same order attained by the dictionary decoder in the specified family.

**Sources.** [Context-decoding cost](../science/context-cost.md#lower-bound-with-adaptive-acquisition).

### M29 A physical source of temporal contrast
29
**Central question.** How can phase fluctuations affect the two-read estimate?

**Understanding target.** Distinguish a shared phase in a block from independently refreshed phases, and connect imperfect reference preparation to a reduced usable contrast. Identify what a digital readout retains compared with an analogue phase monitor.

**Prerequisites.** [M16](#m16-canceling-the-shared-polarity), [M21](#m21-coverage-and-usable-contrast), [M22](#m22-the-trusted-input-boundary).

**Conceptual connection.** A practical claim depends on the measured temporal contrast and on which reference interface is available.

**Sources.** [Physical interpretation](../science/physical-model.md).

### M30 The complete temporal readout story
30
**Central question.** What is gained, and what does it cost?

**Understanding target.** Follow the chain from masked measurement effects to a joint error law, a calibrated score, and the resource cost of learning a decoder. State the assumptions for the drift-valid guarantee separately from the stationary family used for the sharp budget.

**Prerequisites.** [M17](#m17-information-first-appears-at-a-chosen-block-length), [M21](#m21-coverage-and-usable-contrast), [M22](#m22-the-trusted-input-boundary), [M23](#m23-several-pauli-expectations), [M26](#m26-two-regimes-for-the-constructive-budget), [M28](#m28-the-matching-lower-bound), [M29](#m29-a-physical-source-of-temporal-contrast).

**Conceptual connection.** A higher-order record can make a source expectation measurable. The resource account identifies when exploiting that record requires inexpensive matched pilots or many paid calibration encounters.

**Sources.** [Scientific reading route](../science/README.md).
