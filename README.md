# PPA Mobilization Agent (Local Edition)

**A standalone AI agent that runs entirely on your local computer.**

We built this tool to automate the mobilization strategy for the **Poor People App**, but we are releasing it as a modular tool for the community.

### 🎯 What This Tool Does
This is a **RAG (Retrieval-Augmented Generation) Agent** designed to make your content creation easier, faster, and more consistent.

*   **The Brain:** It reads PDF documents from a local folder to understand your specific cause.
*   **The Voice:** It uses AI (OpenAI) to write content in a specific "persona" or writing style.
*   **The Memory:** It remembers the last 5 posts it generated so it doesn't repeat itself.
*   **The Broadcast:** It connects and can post directly to **Nostr** and **Telegram**.

---

## 🛠️ Prerequisites (Don't Skip This!)

If you're new to building please open up your go-to LLM. I recommend Gemini 3.0 through the Google Ai Studio. Follow link to sign up https://aistudio.google.com/
You can also open up the LLM_HELP.txt file found in this repo, and paste that pre-made prompt into the your choice of LLM and make sure to replace the "Paste Your Error Here" text with your question or issue. It's important to get a conversation going with your LLM to bring it up to speed so that you're both on the same page in case you have more questions.


**Choose A Code Editor**
    *   We recommend **VS Code** or **Cursor**.

---

## 🚀 Installation Guide (Step-by-Step)

We have written this for beginners. Follow every step exactly.

Open your IDE (Cursor or Visual Studio Code)
Open the Terminal unde the View tab.

Before you start, ensure you have these installed. 

1.  **Python 3.14** (We recommend **Python 3.14** for best compatibility.)
   If you don't have it installed go to https://www.python.org/downloads/, choose 3.14 and a python install manager will download.
   Double click the download and it's fairly straightforward from there. If you get stuck, watch the tutorial video for this build or ask your LLM.
   PLEASE NOTE: The "Add to PATH" Warning: In the Python installation step, you should bold the instruction: "When installing Python, check the box at the bottom that says 'Add       Python to PATH'." This is the #1 reason beginners fail. 
3.  *   *Check if you already have it:* Open Terminal and type `python --version`
4.  **Git**
    *   *Check if you have it:* Type `git --version`
    If you don't have Git go to https://git-scm.com/install/windows and download it.
    Any questions ask your LLM.

### 1. Download the Code
1.  Go to the folder where you keep your projects (like your **Documents** folder or just your **Desktop**).
2.  **Right-click** in the blank space and select **"Open in Terminal"** (Windows).
    *   *Mac Users:* Open your Terminal app and type `cd Desktop` (or wherever you want it).
3.  Run this command (this will automatically **create the folder** for you):

```bash
git clone https://github.com/FotiosMpouris/ppa-mobilization-agent-lite.git
```

### 2. Open the Project in Your Editor
**This is important!** You must be inside the correct folder.
1.  Open VS Code (or Cursor) if you're not already there.
2.  Go to **File > Open Folder...**
3.  Select the `ppa-mobilization-agent-lite` folder you just downloaded.
4.  Open a **New Terminal** inside the editor (`Terminal > New Terminal` in the top menu).

### 3. Create the Python Environment
We create a "virtual environment" (sandbox) so this tool doesn't interfere with your computer.

**For Windows:**
Copy and paste these commands one by one:

```bash
python -m venv venv
```

**CRITICAL STEP FOR WINDOWS:**
To allow the script to run, you might need to adjust your security policy. Run this exact command:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Now, activate the sandbox:
```bash
.\venv\Scripts\activate
```

*(You should see `(venv)` appear in green at the start of your command line).*

**For Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
This installs the "brains" of the operation (OpenAI, Nostr SDK, etc).

```bash
pip install -r requirements.txt
```

---

## Remember Any Questions of course Go To Your LLM and let them know exactly what you're struggling with.

## 🔑 Configuration (The Secrets)

This agent runs on **your** keys. We do not see them. We do not save them. At this point this has nothing to really do with us. You're running locally on your computer.

### 1. Create your .env file
We need to rename the example file. The easiest way is to use this command in your terminal:

```bash
notepad .env.example
```

This will open the file. Now, go to **File > Save As** and save it as simply `.env` (remove the .example part).

### 2. Get Your Keys (Tutorials Included)
You need to fill in the values in that file. If you don't know how to get these keys, watch these specific tutorials:

*   **OPENAI_API_KEY**: Required for the AI.
    *   📺 **Watch:** [David Ondrej's Quick Setup Guide](https://youtu.be/qgT-quk3JEo?si=rH6PAtOMY-Vj7KXt)
*   **NOSTR_NSEC**: Required for uncensorable posting.
    *   📺 **Watch:** [Nostr Keys with Primal (Oslo Freedom Forum)](https://youtu.be/u_U2obseVwY?si=IgnmDv7M1VYDeKZC)
*   **TELEGRAM_BOT_TOKEN**: Optional.
    *   📺 **Watch:** [Setting up a Bot with JarvisBot](https://youtu.be/B9VsT7vV6jI?si=msxXzyEMRAyoa4O3)

**Once you have pasted your keys, SAVE the .env file.**

---

## 🖥️ How to Run It

Use this specific command to launch the app. We use `python -m` to ensure it runs securely within your environment.

```bash
python -m streamlit run run.py
```

This will automatically open a browser window with your **Mission Control** interface.

### How to Use the Interface
1.  **Directives:** Type what you want the agent to write about (e.g., "Explain why inflation hurts the working class").
2.  **Target Audience:** Select who you are talking to.
3.  **Execute Mission:** The agent reads your PDFs, checks its memory, and writes a draft.
4.  **Edit & Launch:** You can edit the text. When ready, click **Nostr** or **Telegram** to broadcast live.

---

## 🧠 Customizing the Brain

### The Knowledge Base
The agent reads **any PDF** you put inside the `knowledge/` folder.
*   **Default:** Included is the **Poor People App White Paper** as well as the **PPA_Nostr_Addendum**.
*   **Make it Yours:** Delete the existing PDFs and drag in your own manifestos or research. The agent "learns" whatever is in this folder.

### Remember The Helper (Stuck?)
If you get stuck, we have included a file called `LLM_HELP.txt`.
1.  Open `LLM_HELP.txt`.
2.  Copy the text.
3.  Paste it into **Gemini** or **Claude** along with your error message.
4.  The AI will tell you exactly how to fix it.
5.  The more specific and detailed you can be, the better answer you will get.

---

## 🤝 Support the Mission

We built this tool to help you mobilize your community. If you found this useful:

1.  **Follow Us:** Posting about the **Poor People App** on Nostr helps us grow.
2.  **Learn More:** Visit [poorpeople.app](https://poorpeople.app) to see the full vision.
3.  **Meet the Founder:** Learn more about the mission at [fotiosmpouris.com](https://fotiosmpouris.com).

**Troubleshooting:**
*   **"Command not found":** Ensure you installed Python and checked the box "Add to PATH" during installation.
*   **Trend Micro / Antivirus Blocking:** Sometimes security software blocks the script. Allow the folder in your antivirus settings, or use the `python -m streamlit ...` command above.
