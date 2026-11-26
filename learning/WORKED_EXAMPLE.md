# One qubit, two reads, one shared sign

We want the mean $`\mu`$ of the ideal $`Z`$ outcome on a fresh qubit. Denote that ideal sign by $`T`$, with mean $`\mu`$. A freshly prepared $`|0\rangle`$ reference has ideal sign $`+1`$.

## The two-shot block

Choose the first input privately by a fair coin. A signal block sends the unknown source qubit first. An all-reference block sends $`|0\rangle`$ first. Both send a freshly prepared $`|0\rangle`$ second. Independently choose a full Pauli mask for each slot, apply it before readout, and undo its bit flip in the returned classical record. Each block uses two calls. A signal block consumes one source copy and one known reference. An all-reference block consumes two known references.

Consider a detector whose corrected output signs multiply the ideal signs by a fair polarity $`H`$ drawn anew for each block. On the second slot only, add an independent sign $`J`$ with mean $`\kappa`$. The experimenter sees the following pair after undoing the Pauli masks.

| Block | First corrected sign | Second corrected sign | Product |
|---|---:|---:|---:|
| Signal | $`H T`$ | $`H J`$ | $`T J`$ |
| All-reference | $`H`$ | $`H J`$ | $`J`$ |

Every entry in either single-output column is an unbiased sign, because $`H`$ is fair and independent of the other random variables. The product removes $`H`$ exactly. Its mean is $`\mu\kappa`$ in the signal arm and $`\kappa`$ in the reference arm. If the second slot instead had an independent fair polarity, both product means would vanish and the entire two-slot record would be blind.

When $`\mu=1/2`$ and $`\kappa=1/2`$, the product is positive with probability $`5/8`$ in the signal arm and $`3/4`$ in the all-reference arm. An unbiased sign would give $`1/2`$. The two positive-output frequencies encode the two means needed to estimate the target.

## Read a finite certificate

Suppose 4,000 blocks yield 2,000 observations in each arm. The signal arm has 1,250 positive products and the all-reference arm has 1,500. Twice their signed sums are $`S=1000`$ and $`C=2000`$, respectively. Their ratio gives a central estimate of $`1/2`$. The fixed-budget certificate is

```math
\left|S-uC\right|\leq 2\sqrt{2B\log(2/\delta)},\qquad -1\leq u\leq 1.
```

Here $`B=4000`$ is the number of allocated blocks and $`\delta=0.05`$ is the chosen error probability. Solving the inequality gives approximately $`[0.328,0.672]`$, rounded outward. The result uses 8,000 detector calls, including every reference shot. For a weaker measured contrast the interval widens. If $`C=0`$ and the inequality holds, the certificate cannot exclude any physical mean.

This certificate holds under history-dependent detector drift with hidden, freshly randomized arms and the stated trusted controls. The shared-polarity model above makes the two response means explicit. The [general proof](../science/calibration.md) uses the conditional score identity to allow broader detector behavior. For a longer block the score can use the entire pilot record, as in the [context decoder](../science/context-cost.md).
