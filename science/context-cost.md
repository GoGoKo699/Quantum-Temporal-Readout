# The cost of learning the temporal decoder

A calibrated temporal receiver can extract an ideal source bit from every block. A finite supply of reference calls can still impose a substantial cost when the detector's decoding rule has no structure. The following model makes that cost explicit.

## A detector with hidden contexts

The source is a fresh qubit in state $`\rho_\mu=(I+\mu Z)/2`$, with $`\mu\in[-1,1]`$ unknown. In each independent block the detector draws an $`m`$-bit context $`V`$ uniformly from a set of size $`D=2^m`$ and a fair bit $`G`$ independently. The hidden detector parameter is one fixed table $`f:\{0,1\}^m\to\{+1,-1\}`$.

The detector measures the first probe in the computational basis, then multiplies its ideal sign by $`(-1)^G f(V)`$. It measures the next $`m+1`$ probes in the same basis, XORing the outputs with the bits of $`V`$ and $`G`$, respectively. The first probe can be a fresh source copy or a known zero-state reference. The remaining probes are known and can all be $`|0\rangle`$. Thus the experimenter can read $`V,G`$ from the pilots and multiply the corrected first report by $`(-1)^G`$. Denote this sign by $`T`$. The block record is now

```math
(V,T),\qquad
T=
\begin{cases}
f(V) X & \text{signal},\\
f(V) & \text{reference},
\end{cases}
\qquad X\in\{-1,1\},\quad\mathbb E[X]=\mu .
```

Every individual detector call has a uniform output for any isolated probe. For the first call, this follows from the fair bit $`G`$, even for an unbalanced table $`f`$. For the pilots, it follows from their fair flip bits. Given $`f`$, multiplying $`T`$ by $`f(V)`$ recovers the ideal source sign exactly in every signal block.

The budget counts every aligned block, with $`m+2`$ detector calls per block. The experimenter has one source copy at most per block in the first slot, trusted state preparation and single-qubit rotations, and classical control. There is no alternative measurement on a source copy or external quantum reference. The context is redrawn independently by the detector and cannot be chosen by the experimenter.

## Minimax block budget

At fixed success probability $`2/3`$ and $`0<\epsilon\le1/8`$, the minimax worst-case block budget for additive error $`\epsilon`$, uniform over $`\mu`$ and $`f`$, is

```math
B^\star(D,\epsilon)
=
\Theta\!\left(\max\left\{\epsilon^{-2},\frac{\sqrt D}{\epsilon}\right\}\right).
```

The two terms have different sources. The usual $`\epsilon^{-2}`$ budget pays for the sampling fluctuations of the ideal source. The context term pays for finding signal blocks whose detector sign is calibrated. The crossover is $`D`$ of order $`\epsilon^{-2}`$. The detector-call budget is $`(m+2)B^\star`$.

### Upper bound by matching context records

Use a calibration batch of size $`c=\lceil\min\{D,\sqrt{D}/\epsilon\}\rceil`$. Each reference block records one exact value $`f(V)`$. If $`K`$ is the number of distinct contexts in the batch, then

```math
\mathbb E K
=
D\big[1-(1-1/D)^c\big]
\ge (1-e^{-1})c.
```

Because $`K\le c`$, Paley–Zygmund gives a constant probability, independent of all parameters, of observing at least $`(1-e^{-1})c/2`$ distinct contexts. For example, repeat the calibration batch a fixed number of times and retain the first batch meeting this threshold. With a sufficiently large absolute number of batches, the probability that none qualifies is at most $`1/12`$.

Use an independent signal batch of size $`s=A\lceil\max\{\epsilon^{-2},\sqrt D/\epsilon\}\rceil`$ for an absolute constant $`A`$. Keep a signal block if its context is in the reference dictionary, and multiply $`T`$ by its stored sign. Conditional on the dictionary, the number of matches has the binomial law with parameters $`s,K/D`$. It has mean at least a constant times $`A\epsilon^{-2}`$ on the calibration success event, since $`sc/D\ge A\epsilon^{-2}`$. A binomial tail bound gives enough matches to estimate the mean of their signs to error $`\epsilon`$ with a Hoeffding bound. The matched source signs are independent with mean $`\mu`$ because the match event depends only on the random context. Choosing $`A`$ large enough bounds both tail probabilities by $`1/12`$. Unmatched calls and any unsuccessful calibration batches count in $`B`$.

### Lower bound with adaptive acquisition

Consider the two alternatives $`\mu=+2\epsilon`$ and $`\mu=-2\epsilon`$. Draw every table entry $`f(v)`$ independently and uniformly from the two signs, with the same table prior under both hypotheses. An estimator that is accurate with probability $`2/3`$ for every table yields a sign test with that success probability under this prior.

Give the experimenter all $`B`$ sampled contexts and all auxiliary bits $`G`$ before acquisition. Also supply the table entries for contexts that occur at least twice among the $`B`$ sampled blocks. These disclosures have the same law under both hypotheses and only add information. Allow the controller to choose adaptively which blocks use the unknown source and which use known references. A rotated unknown probe gives an ideal sign mean $`a\mu`$, with $`|a|\le1`$ and $`a`$ fixed by the control for that call. Known probe records at the later slots can be generated from the already disclosed context and auxiliary bit, together with randomness from the known states. They add no information about $`\mu`$.

Conditional on the disclosures, a singleton context has a fresh independent fair table entry. The first-slot read is then fair in either signal hypothesis, while a reference acquisition has identical law under both hypotheses. That context never occurs again within the budget. In a repeated context the table entry is supplied. A signal block there has conditional Kullback–Leibler divergence at most $`16\epsilon^2`$, because the two binary means are $`t`$ and $`-t`$ with $`|t|\le 2\epsilon`$ and

```math
t\log\frac{1+t}{1-t}\le 4t^2
\qquad (|t|\le1/2).
```

A repeated-context reference block has divergence zero. This bounds the full adaptive transcript divergence by $`16\epsilon^2`$ times the expected number of blocks whose contexts repeat. For any block, a union bound makes its probability of a match at most $`(B-1)/D`$. Thus the transcript divergence is at most

```math
16\epsilon^2\min\left\{B,\frac{B(B-1)}{D}\right\}.
```

A sign test with success probability at least $`2/3`$ under each hypothesis requires a divergence bounded below by a positive constant, by data processing to the binary test outcome. It follows that $`B=\Omega(\epsilon^{-2})`$ and $`B=\Omega(\sqrt D/\epsilon)`$. This argument covers a worst-case budget even for adaptive stopping, since a shorter acquisition can be padded to the full budget. The matched rate holds in the stated independent-block, deterministic-table model. Learning structured or stochastic decoders under drift is a separate problem.
