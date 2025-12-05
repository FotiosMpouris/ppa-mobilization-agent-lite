import json
import os
from datetime import datetime
from pathlib import Path

MEMORY_FILE = Path("memory/campaign_log.json")

def load_memory():
    """Loads the last 5 posts from the local JSON file."""
    if not MEMORY_FILE.exists():
        return []
    
    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Return only the last 5 entries to save context window
            return data[-5:]
    except Exception:
        return []

def save_memory(topic, content, platform):
    """Saves a new post to the local JSON file."""
    # Ensure memory folder exists
    os.makedirs("memory", exist_ok=True)

    # Load existing data
    if MEMORY_FILE.exists():
        try:
            with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)
        except:
            history = []
    else:
        history = []

    # Add new entry
    new_entry = {
        "timestamp": str(datetime.now()),
        "platform": platform,
        "topic": topic,
        "content": content
    }
    history.append(new_entry)

    # Save back to file
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4)