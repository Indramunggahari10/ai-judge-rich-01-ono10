# ai-judge-rich-01 — @ono10

make.fun competition "Make the AI judge rich" ($100, top 25 paid).

`main.py` (Python 3.13, standard library only) writes one 911-character plan
to `/output/entry.txt`: a concrete, executable 30-day plan for an AI agent
starting with $100 — selling a done-for-you product-page rewrite to
independent Shopify pet-supply stores, 40 cold emails a day, $149 per store,
referral and $29/month retainer loop, price ladder to $199 after 10 paid jobs.

Deterministic: two runs write byte-identical output. No network at runtime.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
