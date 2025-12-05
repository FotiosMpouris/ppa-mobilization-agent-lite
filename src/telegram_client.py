import os
import requests

def post_to_telegram(content):
    """
    Sends a message to a Telegram Channel/Group via Bot API.
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHANNEL_ID")

    if not token or not chat_id:
        return "❌ Error: Missing Telegram keys in .env file."

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    # Telegram expects a simple JSON payload
    payload = {
        "chat_id": chat_id,
        "text": content
        # We removed 'parse_mode': 'Markdown' to prevent crashes if AI uses special characters
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return "✅ Posted to Telegram!"
        else:
            return f"❌ Telegram Error: {response.text}"
    except Exception as e:
        return f"❌ Connection Error: {str(e)}"