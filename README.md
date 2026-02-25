# Binary Long Multiplication Demo (String-Based, 8-bit Truncation)

This repo contains a small Python program (`main.py`) that **demonstrates binary long multiplication SIMULATION** using **strings of `'0'`/`'1'`** rather than Python integers.

---

## What the program does

- Implements **binary addition** on bitstrings (`binary_add`)
- Implements **binary long multiplication** as repeated **shift + add** (`binary_multiply`)
- Constrains intermediate results to **8 bits** by truncating to the last 8 bits
  - This intentionally demonstrates **overflow / wraparound** behavior (mod \(2^8\))

At the end, it runs two examples:
1. A case that fits within 8 bits (13 × 11)
2. A case that overflows 8 bits (205 × 235), showing truncation effects

---

## Files

- `main.py` — implementation and demo runs
- `Binary_Long_Multiplication.pdf` — explanation of binary long multiplication

---

## Requirements

- Python 3.8+ (any modern Python 3 is fine)

No third-party libraries are used.

---

## How to run

```bash
python3 main.py
```

Expected output will look like:

- First case prints correct 8-bit product for 13 × 11
- Second case prints the **low 8 bits** of the true product (overflow demonstration)

---

## How it works (conceptually)

### `binary_add(X, Y)`

1. Pads both inputs to the same length using `zfill`.
2. Adds from right-to-left, tracking a `carry`.
3. Builds the result as a string.
4. Returns only the **last 8 bits**: `result[-8:]`

This models fixed-width register addition where overflow is discarded.

### `binary_multiply(A, B)`

Implements the standard “shift-and-add” multiplication:

- Reverse `B` to iterate from least significant bit to most significant bit.
- For each bit `B[i]`:
  - If it is `1`, add `(A << i)` to the running `product`.
  - The shift is implemented by appending zeros: `A + '0' * i`.
- Return the last 8 bits of the final `product`.

Mathematically:

\[
A \times B = \sum_{i: B_i = 1} (A \ll i)
\]

---

## Important constraints / caveats

1. **8-bit truncation is intentional**
   - The code models an 8-bit datapath by discarding higher bits.
   - For the second test case, the printed product is **not the true mathematical product**—it is the product modulo \(2^8\).

2. **Inputs are assumed valid**
   - Functions assume `X`, `Y`, `A`, `B` are binary strings.
   - No validation is performed (e.g., checking only `'0'`/`'1'`).

3. **Shifted multiplicands grow**
   - `shifted_A = A + '0'*i` may exceed 8 bits before truncation during addition.
   - The truncation occurs inside `binary_add` (and at the return of `binary_multiply`).

---

## Suggested improvements (optional)

If you want this to be more robust for teaching/demo purposes:

- Add input validation:
  - ensure strings contain only `'0'`/`'1'`
  - ensure inputs are 8 bits (or parameterize bit-width)
- Make bit-width configurable:
  - `WIDTH = 8`
  - replace `[-8:]` with `[-WIDTH:]`
- Print intermediate partial products to show the “long multiplication rows”
- Add a companion `binary_divide` implementation (shift-and-subtract long division)

---

## License

Educational/demo use for the course.
