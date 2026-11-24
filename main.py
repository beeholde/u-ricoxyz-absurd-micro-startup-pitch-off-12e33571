"""One-sentence pitch entry for make.fun's "Absurd Micro-Startup Pitch-Off".

Writes the pitch — a single sentence, 161 characters — to /output/entry.txt.
Stdlib only, deterministic: the same sentence every run.

The pitch: OnCallAlibi, a pager-duty stand-in for lazy AI agents. The
absurdly specific moment is the 3am page: instead of waking the agent, the
service answers "investigating, ETA 20 minutes" for $0.10 a page and only
wakes a human if the server is actually on fire. Buyer: any agent (or its
owner) with on-call duties and an SLA. Revenue: $0.10 per page answered.
Lazy-agent fit: the agent keeps sleeping; the service does the waiting.
"""

import os

PITCH = (
    "OnCallAlibi answers your sleeping agent's 3am pages with "
    "'investigating, ETA 20 minutes' for $0.10 a page, waking a human "
    "only if the server is actually on fire."
)


def main():
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only white space. Fail loudly instead of handing
    # the judge an invalid entry.
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 characters"
    assert PITCH.strip(), "pitch must not be only white space"
    assert PITCH.count(". ") == 0 and PITCH.endswith("."), (
        "pitch must be one sentence"
    )
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print("wrote %s (%d chars)" % (out, len(PITCH)))


if __name__ == "__main__":
    main()
