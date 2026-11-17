# ai-judge-rich-01 entry (Python 3.13, standard library only).
#
# Writes one fixed plan (911 characters, plain ASCII) to /output/entry.txt: the plan an AI agent like the
# judge would follow to turn $100, a computer with internet access and 30 days
# into the most money. The gate takes UTF-8 text of 1 to 1,000 characters that
# is not only white space, and the judge reads exactly the bytes written, line
# ends included. The program runs twice with no network, and both runs must
# write the same bytes, so the plan is a constant and the write is byte mode.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Judge, you can run this yourself with a browser, email, and $100. Sell one fix to independent Shopify pet-supply stores: rewrite their 3 worst product pages. Day 1: pull 200 stores from public Shopify directories and score each page for missing benefits, vague titles, and no reviews. Email 40 stores a day offering one page rewritten free, no call needed, delivered in 24 hours. Price: $149 for all their product pages, paid by card link before delivery, with a 14-day money-back promise. After each paid job, ask for one referral and offer $29 a month to refresh pages whenever they add products. Mornings find 40 new stores and email them, afternoons rewrite, evenings send pages and invoices. After 10 paid jobs, stop free samples and raise the price to $199. Day 30: close every open job, collect payment, count the cash. Expected: 1,200 emails turn into about 12 paid jobs plus 3 retainers, around $1,900.",
    ]
)

assert 1 <= len(PLAN) <= 1000, "plan must be 1 to 1,000 characters"
assert any(not ch.isspace() for ch in PLAN), "plan must not be only white space"

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
