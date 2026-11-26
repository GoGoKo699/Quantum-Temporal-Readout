# Verification

From the repository root, use Python 3.10 or later.

```sh
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

| Output | Calculation checked |
|---|---|
| `Twirl and parity` | Direct averaging over Pauli masks agrees with the additive-noise model and factors every character. The test uses 30 normalized complex POVMs across dimensions 2, 4 and 8 and a causal two-slot detector that retains a qubit. The probability residual should be below `1e-12`. |
| `Even masks` | For lengths 2 through 6, every proper subset of the errors is exactly uniform while the full corrected parity gives the signal bit. |
| `Decoder` | The small-context hidden-sign family has zero marginal contrast and exact decoding when a reference context has been seen. Enumeration checks the expected repeated-context count used in the converse. |
| `Product-basis converse` | The product-axis overlap squares sum to one, and the hard detector's reverse divergence agrees with the Bernoulli formula. |

The suite uses fixed random seeds where sampling a matrix or an axis. The guarantees for arbitrary dimensions, histories and block budgets are proved in the [scientific account](../science/README.md).

Run `python3 verification/phase_benchmark.py` to reproduce the contrast table in the [thresholded readout model](../science/physical-model.md). The script uses the Python standard library and checks the zero single-use contrast, Parseval identity and lag bound.
