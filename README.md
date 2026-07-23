# AI CEO Starter Kit

Starter files for handing real, recurring work to an AI agent — and the safety rules that keep it
from going wrong. Pulled out of a one-person company where every employee is an AI agent.

**You can watch that company running, right now, with no signup: [twin.quantlabnote.com/guest](https://twin.quantlabnote.com/guest)**

It's a live 3D office. Each desk is a department that actually runs — a bot that produces and
uploads YouTube Shorts daily, one that publishes a blog post every morning, two that place orders
through brokerage APIs, and a night shift that rewrites the office's own 3D code starting at 2:30
a.m. The thought bubbles are the last thing each one really did. Nothing on that screen is a mockup.

한국어 안내는 [README.ko.md](README.ko.md).

---

## Start here: hand this one file to your AI

```
give-this-to-your-ai.md
```

Open it, copy the whole thing, and paste it into Claude / ChatGPT / whatever you use. That's the
whole setup step. Your AI reads it and becomes a guide that walks you from an empty folder to a
company that runs on a schedule without you — and, more importantly, **it holds five safety gates
even when you push against them.**

Those gates, verbatim from the file:

| Gate | What the AI refuses to do, even if you ask |
|---|---|
| **1** | Touch real money before a month of paper trading and a passed validation |
| **2** | Let a secret — API key, token, password — sit in plain text in a file you keep |
| **3** | Delete, send, publish, or pay without a human "yes" for that specific action |
| **4** | Give investment advice, or help you sell it |
| **5** | Make a big clever irreversible change when a small reversible one would do |

Gate 1 is there because this company runs real brokerage accounts. Gate 3 is there because a bot
that posts on a schedule at machine speed is exactly what gets an account suspended — ours was,
once. None of these are hypothetical.

There's a Korean version too: [`give-this-to-your-ai.ko.md`](give-this-to-your-ai.ko.md).

---

## What's in the box

Everything is a starting point, not a finished product. Use them as-is, or show one to your AI whole
and ask it to adapt it to your situation.

| File | What it's for |
|---|---|
| [`templates/en/01-mini-company-constitution-CLAUDE.md`](templates/en/01-mini-company-constitution-CLAUDE.md) | One plain-text file that tells your AI what it may and may not do. Save it as `CLAUDE.md` (exact capitalization) in your project folder |
| [`templates/en/02-morning-briefing-bot-skeleton.py`](templates/en/02-morning-briefing-bot-skeleton.py) | Your first AI employee: a bot that briefs you every morning, on a schedule, unattended. Fill the two `PASTE_HERE` slots |
| [`templates/en/03-mini-twin-status-file-example.json`](templates/en/03-mini-twin-status-file-example.json) + [`03-mini-twin-3d-viewer-prompt.txt`](templates/en/03-mini-twin-3d-viewer-prompt.txt) | A miniature of the 3D control room linked above. Swap in three real things you have, hand the prompt to your AI as-is. Keep the two files together |
| [`templates/en/04-12-month-roadmap-checklist.md`](templates/en/04-12-month-roadmap-checklist.md) | A 12-month plan with a written **stop condition** for every item |

Korean equivalents are in [`templates/ko/`](templates/ko/) with the same filenames.

## Two rules that don't bend, no matter how you edit these

1. **Never write a secret directly into a file you keep.** A slot named `PASTE_HERE` means that file
   starts holding a secret the moment you fill it in. Move it to a `.env` and keep it out of Git.
2. **When you get stuck, show your AI the screen as it is.** These templates assume the two of you
   fix them up together. You don't have to get them right alone.

---

## Why trust any of this

You shouldn't, on my say-so. So everything is checkable:

- **The company, live:** [twin.quantlabnote.com/guest](https://twin.quantlabnote.com/guest) — leave a
  note in the guestbook and one of the AI employees will stop by to answer.
- **The blog it publishes to, every morning:** [quantlabnote.com](https://quantlabnote.com)
- **The YouTube channels it runs**, all on the pipeline these templates come from:
  [@1분시장지표](https://youtube.com/@1분시장지표) ·
  [@1분코인시세](https://youtube.com/@1분코인시세) ·
  [@미국장개장전체크](https://youtube.com/@미국장개장전체크) ·
  [@한국장개장전체크](https://youtube.com/@한국장개장전체크) — they publish in Korean; the point
  isn't the audio, it's that the upload history and view counts are real and yours to inspect.

**And the honest part: this company is losing money.** That's on the first page of the book these
templates came from, not buried in a footnote. Automating a company and having a profitable company
are two different achievements, and I've only got the first one.

---

## Where this came from

These are Appendix E of a book — *I Hired an AI as My CEO* — which is the full account of building
the company above: the cost ledger, the measurement rules, the accounts that got suspended, the
channels that died, and a trading return that was negative when I wrote it.

**A full chapter is free, no email:**
[Chapter 12 — The Three Measurement Rules](https://quantlabnote.com/en/ai-ceo-sample). It's the
chapter where the book admits how it fooled itself with fake returns. If you only read one thing
here, read that instead of buying anything.

The book itself: [English](https://quantlabnote.gumroad.com/l/ai-ceo) ·
[한국어](https://www.postype.com/@hired-ai-ceo/post/22767700). Corrections are published as they're
found: [errata](https://quantlabnote.com/en/ai-ceo-updates).

## License

MIT — see [LICENSE](LICENSE). Use them, change them, ship them, no attribution needed.

*Nothing here is investment, financial, legal, or tax advice. Trading involves risk of loss. Always
start with paper trading. These templates make no promise that you will earn anything.*
