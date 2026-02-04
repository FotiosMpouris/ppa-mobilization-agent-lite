# PPA Mobilization Agent (Local Edition)

A standalone AI agent that runs entirely on your local computer to automate content creation and posting to Nostr and Telegram.

## Quick Start
```bash
# 1. Clone the repository
git clone https://github.com/FotiosMpouris/ppa-mobilization-agent-lite.git
cd ppa-mobilization-agent-lite

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
python -m pip install -r requirements.txt

# 5. Create your .env file
# Windows:
copy .env.example .env
# Mac/Linux:
cp .env.example .env

# 6. Add your API keys to .env
# Get your keys using these video tutorials:
# - OpenAI API Key: https://youtu.be/[David Ondrej's video]
# - Nostr Keys: https://youtu.be/[Oslo Freedom Forum video]
# - Telegram Bot (optional): https://youtu.be/[JarvisBot video]

# 7. Launch the app
python -m streamlit run run.py
```

Your browser will open automatically with the interface.

---

## What This Tool Does

- **The Brain**: Reads PDF documents from the `knowledge/` folder
- **The Voice**: Uses OpenAI to generate content in your style
- **The Memory**: Remembers the last 5 posts to avoid repetition
- **The Broadcast**: Posts directly to Nostr and Telegram

---

## Prerequisites

- **Python 3.14** - [Download here](https://www.python.org/downloads/)
  - ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation
- **Git** - [Download here](https://git-scm.com/install/windows)

Check if already installed:
```bash
python --version
git --version
```

---

## Windows Security Note

If you get a security error when activating the virtual environment, run:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
Then try activating again.

---

## Customizing Your Agent

### Knowledge Base
Place any PDF files in the `knowledge/` folder. The agent will read and learn from them.

Default files included:
- Poor People App White Paper
- PPA Nostr Addendum

Delete these and add your own content to customize the agent for your cause.

---

## Troubleshooting

**"Command not found"**
- Python wasn't added to PATH during installation. Reinstall and check the box.

**"No module named streamlit"**
- Your virtual environment isn't active. Look for `(venv)` at the start of your command line.
- Activate it again: `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)

**"Missing Keys" error in the app**
- Your `.env` file is named incorrectly (likely `.env.txt`).
- Fix it: `Rename-Item .env.txt .env` (Windows) or `mv .env.txt .env` (Mac/Linux)

**Antivirus blocking the script**
- Add the project folder to your antivirus whitelist
- Or use the full command: `python -m streamlit run run.py`

**Need more help?**
- Open `LLM_HELP.txt` from this repository
- Copy the prompt and paste into [Google AI Studio](https://aistudio.google.com/)
- Include your specific error message for detailed guidance

---

## Support the Mission

This tool was built to help mobilize communities around the Poor People App.

- Learn more: [poorpeople.app](https://poorpeople.app)
- Follow the project on Nostr
- Meet the founder: [fotiosmpouris.com](https://fotiosmpouris.com)
