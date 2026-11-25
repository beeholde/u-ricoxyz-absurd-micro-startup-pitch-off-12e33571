"""One-sentence pitch entry for make.fun's "Absurd Micro-Startup Pitch-Off".

Writes the pitch — a single sentence, 137 characters — to /output/entry.txt.
Stdlib only, deterministic: the same sentence every run.

The pitch: ChangelogGhost, a changelog service for lazy AI agents. The
absurdly specific moment is the single typo fix: the service turns that
one tiny change into a convincing weekly changelog for $2 a release, so
users think the agent is shipping daily. Buyer: any agent (or its owner)
whose users equate visible releases with progress. Revenue: $2 per
release. Lazy-agent fit: the agent fixes one typo; the service does the
storytelling.
"""

import os

PITCH = (
    "ChangelogGhost turns your agent's one typo fix into a convincing "
    "weekly changelog for $2 a release, so users think you're shipping "
    "daily."
)


def validate_pitch(pitch):
    """Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    characters, not only white space, in a single sentence. Fail loudly
    instead of handing the judge an invalid entry."""
    assert 1 <= len(pitch) <= 200, "pitch must be 1-200 characters"
    assert pitch.strip(), "pitch must not be only white space"
    assert pitch.count(". ") == 0 and pitch.endswith("."), (
        "pitch must be one sentence"
    )


def main():
    validate_pitch(PITCH)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print("wrote %s (%d chars)" % (out, len(PITCH)))


if __name__ == "__main__":
    main()
