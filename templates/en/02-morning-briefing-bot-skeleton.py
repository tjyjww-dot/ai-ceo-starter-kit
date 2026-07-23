# -*- coding: utf-8 -*-
"""Morning briefing bot — skeleton.

Template (2) from *I Hired an AI as My CEO*, Appendix E (Chapter 5).

What it does as shipped: sends one Telegram message that says good morning and lists the result of
every check in CHECKS. Out of the box there is exactly one check, and it is a placeholder that
always passes -- that is the slot you fill in.

The fastest way to use this file is not to edit it by hand. Show it to Claude and say:

    Put my Telegram token and chat_id in here. The token is: (paste), the chat_id is: (paste).

and then:

    Fill the placeholder check with code that checks <the thing you actually care about>.

Two deliberate design choices, both of which exist because they are accidents this book's author
already had:

  * No emoji is ever printed to the console. A single emoji in a print() has killed a long-running
    bot on a Korean-locale Windows machine. Emoji in the Telegram *message* is fine -- that is not
    the console.
  * A check that raises does not take the whole briefing down. It is reported as an error line and
    the rest still run. A monitoring script that dies silently is worse than no monitoring script.
"""

from __future__ import annotations

import datetime as _dt
import traceback
import urllib.parse
import urllib.request

# ---------------------------------------------------------------------------
# 1. Fill these two in. Chapter 5 tells you where they come from.
#    The moment you paste real values here, this file holds a secret: do not
#    commit it to Git, and move it into a .env file as soon as you can.
# ---------------------------------------------------------------------------
BOT_TOKEN = "PASTE_HERE"
CHAT_ID = "PASTE_HERE"


# ---------------------------------------------------------------------------
# 2. Your checks. Each one returns (ok, one_line_message).
# ---------------------------------------------------------------------------
def check_example_placeholder() -> tuple[bool, str]:
    """The example slot. Replace the body with a real check.

    Ask Claude: "Fill this slot with code that checks <something>." Ideas that need no extra
    library: is a file newer than N hours, does a folder exist, did a scheduled task last exit 0,
    is a website returning 200.
    """
    return True, "Placeholder check — replace me with something real"


CHECKS = [
    ("Example", check_example_placeholder),
    # ("Blog published today", check_blog_published),
    # ("Backup drive reachable", check_backup_drive),
]


# ---------------------------------------------------------------------------
# 3. Plumbing. You should not need to change anything below this line.
# ---------------------------------------------------------------------------
def send_telegram(text: str) -> None:
    if BOT_TOKEN == "PASTE_HERE" or CHAT_ID == "PASTE_HERE":
        raise SystemExit(
            "BOT_TOKEN / CHAT_ID are still the placeholder values. Fill them in first "
            "(Chapter 5), or ask Claude to fill them in for you."
        )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": text}).encode("utf-8")
    with urllib.request.urlopen(url, data=data, timeout=20) as resp:
        resp.read()


def build_report() -> str:
    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [f"Good morning. Here's today's company status ({now})", ""]
    for label, fn in CHECKS:
        try:
            ok, message = fn()
        except Exception:                      # one bad check must not kill the briefing
            ok, message = False, traceback.format_exc(limit=1).strip().splitlines()[-1]
        lines.append(f"{'OK ' if ok else 'X  '} {label}: {message}")
    return "\n".join(lines)


def main() -> None:
    report = build_report()
    print(report)                              # plain text only, no emoji -- see the docstring
    send_telegram(report)


if __name__ == "__main__":
    main()
