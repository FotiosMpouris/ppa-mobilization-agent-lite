# PPA Mobilization Agent (Local Edition)

**A standalone AI agent that runs entirely on your local computer.**

We built this tool to automate the mobilization strategy for the **Poor People App**, but we are releasing it as a modular tool for the community.

### 🎯 What This Tool Does
This is a **RAG (Retrieval-Augmented Generation) Agent** designed to make your advocacy easier, faster, and more consistent.

*   **The Brain (RAG):** It reads PDF documents from a local folder to understand your specific cause, arguments, and data points.
*   **The Voice:** It uses AI (OpenAI) to write content in a specific "persona" or writing style that you define.
*   **The Memory:** It remembers the last 5 posts it generated so it doesn't repeat itself.
*   **The Broadcast:** It connects directly to **Nostr** (using your private key) and **Telegram** to post content immediately without censorship.

---

## 🛠️ Prerequisites

Before you start, ensure you have these installed on your computer:

1.  **Python (3.10 or higher)**
    *   *Verify:* Open your terminal and type `python --version`
2.  **Git**
    *   *Verify:* Type `git --version`
3.  **A Code Editor**
    *   We recommend **VS Code** or **Cursor**.

---

## 🚀 Installation Guide

Follow these steps exactly to set up the agent on your machine.

### 1. Download the Code
Open your terminal (PowerShell on Windows, Terminal on Mac) and run:

```bash
git clone https://github.com/FotiosMpouris/ppa-mobilization-agent-lite.git
cd ppa-mobilization-agent-lite
```

### 2. Create the Python Environment
We create a "virtual environment" (sandbox) so this tool doesn't interfere with your other computer settings.

**For Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```
*(Note: If you get a "script is disabled" error on Windows, run this command: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`, then try the activate command again).*

**For Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

*You should see `(venv)` appear at the start of your command line.*

### 3. Install Dependencies
This installs the necessary libraries (OpenAI, Nostr SDK, Streamlit, etc).

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration (The Secrets)

This agent runs on **your** keys. Your secrets never leave your local computer.

1.  Look for the file named `.env.example` in the project folder.
2.  **Rename** this file to just `.env` (remove the .example extension).
3.  Open `.env` in your text editor.

You need to fill in these values:

*   **OPENAI_API_KEY**: Required. This powers the intelligence. You can get one from [platform.openai.com](https://platform.openai.com).
*   **NOSTR_NSEC**: Required if you want to post to Nostr. This is your **Private Key** (starts with `nsec1...`).
*   **TELEGRAM_BOT_TOKEN**: Optional. Only needed if you are broadcasting to Telegram.

**Save the file.**

---

## 🖥️ How to Run It

Once installed and configured, run the application with this command:

```bash
streamlit run run.py
```

This will automatically open a browser window with your **Mission Control** interface.

### Using the Interface
1.  **Directives:** Type what you want the agent to write about (e.g., "Explain why decentralized money matters").
2.  **Target Audience:** Select who you are talking to (this adjusts the tone/persona).
3.  **Execute Mission:** The agent reads your PDFs, checks its memory, and writes a draft.
4.  **Edit & Launch:** You can edit the generated text in the box. When ready, click **Nostr** or **Telegram** to broadcast live.

---

## 🧠 Customizing the Brain

### The Knowledge Base (PDFs)
The agent reads **any PDF** you put inside the `knowledge/` folder.

*   **Default:** The kit comes pre-loaded with the **Poor People App White Paper**. Out of the box, it will advocate for the PPA mission.
*   **Customize:** To make this agent work for *your* cause, simply **delete the existing PDFs** in the `knowledge/` folder and drag in your own manifestos, research papers, or articles. The agent immediately "learns" whatever you put there.

### The Persona
You can change *how* the agent writes by editing the file `src/agent.py`. Look for the `system_prompt` section to adjust its personality instructions.

---

## ⚠️ Troubleshooting

**"Command not found"**
Make sure you installed Python and added it to your PATH during installation.

**"Access Denied" on Windows**
If PowerShell won't let you run the activate script, run this command:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

**Browser doesn't open**
If `streamlit run` doesn't open a tab automatically, copy the "Local URL" shown in the terminal (usually `http://localhost:8501`) and paste it into your browser.
