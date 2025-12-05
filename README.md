\# 🚀 PPA Mobilization Agent (Lite)



\*\*Local-First • Private • Decentralized AI Marketing Tool\*\*



This is the open-source engine behind the \[Poor People App](https://poorpeople.app) mobilization strategy. We built this tool to amplify our voice without relying on big tech infrastructure. Now, we are giving it to you.



\## 🌟 What This Is

A standalone AI agent that runs entirely on your local computer.

\*   \*\*The Brain:\*\* Reads PDFs from your local folder (no AWS required).

\*   \*\*The Voice:\*\* Generates content using your own OpenAI keys.

\*   \*\*The Megaphone:\*\* Broadcasts directly to \*\*Nostr\*\* and \*\*Telegram\*\*.



\## ⚡ Quick Start Cheat Sheet



| Action | Command |

| :--- | :--- |

| \*\*1. Install Dependencies\*\* | `python -m pip install -r requirements.txt` |

| \*\*2. Run the App\*\* | `python -m streamlit run run.py` |

| \*\*3. Update Keys\*\* | Edit `.env` file |

| \*\*4. Add Knowledge\*\* | Drop PDFs into `/knowledge` folder |



---



\## 🛠️ Installation Guide



\### 1. Prerequisites

\*   \[Python 3.12+](https://www.python.org/downloads/) (Make sure to check "Add to PATH" during install)

\*   \[Git](https://git-scm.com/downloads)



\### 2. Clone \& Setup

```bash

git clone https://github.com/FreedomMarch/ppa-mobilization-agent.git

cd ppa-mobilization-agent



\# Create Virtual Environment (Optional but recommended)

python -m venv venv



\# Windows:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

.\\venv\\Scripts\\activate



\# Mac/Linux:

source venv/bin/activate

