import os
import requests

def post_to_telegram(content):
    """
    Sends a message to a Telegram Channel/Group via Bot API.
    Uses headers to mimic a browser request to avoid firewall blocks.
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHANNEL_ID")

    if not token or not chat_id:
        return "❌ Error: Missing Telegram keys in .env file."

    # Simple validation
    if ":" not in token:
        return "❌ Error: Invalid Telegram Token format."

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": content
    }

    # FIX: Add a User-Agent header so we look like a legitimate browser, 
    # not a suspicious script.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/json"
    }

    try:
        # We add 'headers=headers' to the request
        response = requests.post(url, json=payload, headers=headers, timeout=20)
        
        if response.status_code == 200:
            return "✅ Posted to Telegram!"
        else:
            return f"❌ Telegram Error {response.status_code}: {response.text}"
            
    except requests.exceptions.ConnectionError:
        return "❌ Connection Error: Local firewall blocked the request. (Try adding the project folder to exceptions)."
    except requests.exceptions.Timeout:
        return "❌ Timeout Error: Telegram didn't respond in time."
    except Exception as e:
        return f"❌ Error: {str(e)}"
        
