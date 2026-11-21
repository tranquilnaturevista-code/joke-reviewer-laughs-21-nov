# The Joke the Reviewer Laughs At

[![The Joke](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![Rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/tranquilnaturevista-code/joke-reviewer-laughs-21-nov/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![Reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/tranquilnaturevista-code/joke-reviewer-laughs-21-nov/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)

One one-line joke about working beside an AI coding agent, written for
the reviewer of the change:

> My AI coding agent writes the code, reviews its own pull request,
> approves it, then files a bug against itself — I'm only CC'd for the
> blame.

The joke is the loop every developer beside an agent recognises: the
agent does the writing, the reviewing, and the approving, and the only
job left for the human in the diff is taking the blame.

## How it works

Run `python3 main.py` and the script writes the joke to
`/output/entry.txt` (the `MAKEFUN_OUTPUT_DIR` environment variable, or
`/output` when that is not set), creating the folder if it does not
exist yet. The program uses only the Python standard library, makes no
network calls, and is deterministic — the same bytes every run.

## Verification

Before writing, the script checks that the joke is a single line of
1–280 characters and not only whitespace, then reads the file back and
stops with an error if it differs from the joke.
