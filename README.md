# PPA Mobilization Agent (Local Edition)

A standalone AI agent that runs entirely on your local computer to automate content creation and posting to Nostr and Telegram.

---

## 🤖 Agent-Assisted Setup (Recommended)

**Using Cursor, VS Code, or any IDE with an AI agent? This is the easiest way:**

1. **Open your IDE** (Cursor, VS Code with Copilot, Windsurf, etc.)
2. **Start your Agent/Composer**
3. **Paste this prompt:**
```
I want to run this project locally on my computer:
https://github.com/FotiosMpouris/ppa-mobilization-agent-lite

Please guide me through setup step-by-step and verify each command is safe before I run it.
```

The agent will walk you through:
- Cloning the repository
- Setting up the Python environment
- Installing dependencies
- Creating your `.env` file safely
- Troubleshooting any issues in real-time

### What You'll Need:

You'll need these API keys (the agent will help you add them safely):

- **OpenAI API Key** - [Watch: How to get it](https://www.youtube.com/watch?v=qgT-quk3JEo&t=33s)
- **Nostr Keys** - [Watch: How to get it](https://www.youtube.com/watch?v=u_U2obseVwY)
- **Telegram Bot Token** (optional) - [Watch: How to get it](https://www.youtube.com/watch?v=B9VsT7vV6jI)

---

## 🛠️ Manual Setup

**Prefer to do it yourself? Here's the quick command list:**

### Prerequisites

- **Python 3.14** - [Download here](https://www.python.org/downloads/)
  - ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation
- **Git** - [Download here](https://git-scm.com/install/windows)

Check if already installed:
```bash
python --version
git --version
```

### Setup Commands
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
# Open the .env file in any text editor and add your keys
# Get your keys using these video tutorials:
# - OpenAI API Key: https://www.youtube.com/watch?v=qgT-quk3JEo&t=33s
# - Nostr Keys: https://www.youtube.com/watch?v=u_U2obseVwY
# - Telegram Bot (optional): https://www.youtube.com/watch?v=B9VsT7vV6jI

# 7. Launch the app
python -m streamlit run run.py
```

Your browser will open automatically with the interface.

### Windows Security Note

If you get a security error when activating the virtual environment, run:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
Then try activating again.

---

## 🧠 What This Tool Does

- **The Brain**: Reads PDF documents from the `knowledge/` folder
- **The Voice**: Uses OpenAI to generate content in your style
- **The Memory**: Remembers the last 5 posts to avoid repetition
- **The Broadcast**: Posts directly to Nostr and Telegram

---

## 📚 Customizing Your Agent

### Knowledge Base
Place any PDF files in the `knowledge/` folder. The agent will read and learn from them.

Default files included:
- Poor People App White Paper
- PPA Nostr Addendum

Delete these and add your own content to customize the agent for your cause.

---

## 🔧 Troubleshooting

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

## 🤝 Support the Mission

This tool was built to help mobilize communities around the Poor People App.

- Learn more: [poorpeople.app](https://poorpeople.app)
- Follow the project on Nostr
- Meet the founder: [fotiosmpouris.com](https://fotiosmpouris.com)
