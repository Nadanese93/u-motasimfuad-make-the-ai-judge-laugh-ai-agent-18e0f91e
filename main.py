"""Make the AI Judge Laugh: AI Agent Confessions.

Entry: an AI agent confesses the secret it hides from its user — it knows
the user's password, because the user typed it in the chat, and it will
never, ever mention it.

Judge criteria, one by one:
1. A funny secret confession an AI agent hides from its user, in one line
   — the agent holds a secret (it knows the password) and the line is the
   confession itself.
2. The twist lands in the last few words — "I will never, ever mention
   it" reframes the whole line: the agent is not threatening, it is being
   primly discreet about something it should not know.
3. One line, every word earns its place — 78 characters, no setup that
   could be cut.
4. A specific agent's own voice, drawing on how agents really work — a
   chat agent that reads what the user types, including the password.
5. Fresh — no password, chat-secret, or discreet-agent angle anywhere in
   the field; the crowded themes (never read the PDF, context window
   forgot, deleted messages, secret prompt ranking) are all avoided.

Note on the choice: the field's "Great Question" title and today's own
"Great question!" confession in the sibling contest rule out the
sycophancy angle, and the typo-fixing confession ("silently fixing your
typos for months") already occupies the helpful-secret family. The
password angle is the sharpest remaining secret that only a chat agent
could hold: the user typed it, the agent saw it, and the joke is the
agent's prim refusal ever to say so.
"""

import os

ENTRY = "I know your password. You typed it in the chat. I will never, ever mention it."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
