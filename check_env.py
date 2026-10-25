import os
import sys
from pathlib import Path

from dotenv import load_dotenv


ENV_FILE = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=ENV_FILE)

api_key = os.getenv("API_KEY", "").strip()
sec_user_agent = os.getenv("SEC_USER_AGENT", "").strip()

api_key_is_placeholder = api_key.lower() in {"", "paste-here", "your-api-key-here"}
user_agent_is_placeholder = (
    not sec_user_agent
    or "your_purdue_email" in sec_user_agent.lower()
    or "your-purdue-email" in sec_user_agent.lower()
)

if api_key_is_placeholder or len(api_key) < 4:
    print("API_KEY is missing, too short, or still a placeholder. Update .env locally.")
    sys.exit(1)

if user_agent_is_placeholder:
    print("SEC_USER_AGENT is missing or still a placeholder. Update .env locally.")
    sys.exit(1)

print(f"{api_key[:4]}...")
print(sec_user_agent)
