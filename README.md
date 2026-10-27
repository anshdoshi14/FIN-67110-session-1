# FIN 67110 Session 1

This project checks that Python can read the local `.env` file. It does not make an API call.

## Install

In PowerShell, run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

## Configure `.env`

Create a copy of .env.example to .env and edit the local `.env` file. Set `API_KEY` to your real key. 
Set `SEC_USER_AGENT` to your name and Purdue email address. 
Keep `.env` private. Do not put a real key in `.env.example`.

## Run the check

```powershell
py check_env.py
```

When configured, the script prints only the first four API-key characters followed by `...`, and the SEC user agent. It never prints the full key.

## AI Policy
This is a learning exercise, not financial advice.
AI assistance: ChatGPT and Codex. I verified the sources myself; the judgments are mine.
Any remaining errors are my own.
