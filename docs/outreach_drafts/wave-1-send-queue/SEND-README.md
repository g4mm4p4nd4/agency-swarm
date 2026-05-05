# Wave 1 Send Queue — Quick Start

## What's Here

```
wave-1-send-queue/
  SEND-README.md           ← this file
  send-queue.json          ← master queue (update after each send)
  01-harrison-chase-...md  ← personalized drafts (email)
  02-shreya-rajpal-...md
  ...
  li-01-harrison-chase.md  ← LinkedIn connection request drafts
  li-02-shreya-rajpal.md
  ...
```

## Prerequisites

1. **Email**: Himalaya CLI installed (`brew install himalaya` — already done)
2. **Gmail App Password**: https://myaccount.google.com/apppasswords
3. **Himalaya config**: `~/.config/himalaya/config.toml` (see template below)

## Himalaya Setup

```bash
mkdir -p ~/.config/himalaya
```

Create `~/.config/himalaya/config.toml` with:

```toml
[accounts.gmail]
email = "YOUR_EMAIL@gmail.com"
display-name = "Your Name"
default = true

backend.type = "imap"
backend.host = "imap.gmail.com"
backend.port = 993
backend.encoding.type = "tls"
backend.login = "YOUR_EMAIL@gmail.com"
backend.auth.type = "password"
backend.auth.cmd = "echo YOUR_APP_PASSWORD"

message.send.backend.type = "smtp"
message.send.backend.host = "smtp.gmail.com"
message.send.backend.port = 587
message.send.backend.encoding.type = "start-tls"
message.send.backend.login = "YOUR_EMAIL@gmail.com"
message.send.backend.auth.type = "password"
message.send.backend.auth.cmd = "echo YOUR_APP_PASSWORD"
```

## Sending

### Send one email

```bash
cat <draft-file> | himalaya template send
```

The draft files use MML syntax. For himalaya to work, you need to add proper From/To headers.

### Send all Wave 1 emails

```bash
for draft in wave-1-send-queue/[0-9]*.md; do
  cat "$draft" | himalaya template send
  echo "Sent: $draft"
  sleep 5  # rate limit
done
```

### Send LinkedIn connection requests

LinkedIn connection requests require manual action via LinkedIn's web interface or API. No CLI tool is available. The drafts in `li-*.md` are ready to copy-paste.

## After Sending

1. Update `send-queue.json` — set `email_sent: true` / `linkedin_sent: true`
2. Update `docs/outreach_drafts/metrics-tracker-14day.md` — log sends in Day 1 row
3. Update `docs/outreach_drafts/YYYY-MM-DD.md` — standup notes

## Troubleshooting

- Himalaya debug: `RUST_LOG=debug himalaya template send < draft.md`
- Gmail app passwords: https://myaccount.google.com/apppasswords
- For Yahoo/Outlook: use different SMTP/IMAP hosts and app passwords
