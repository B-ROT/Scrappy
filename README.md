# 🕸️ Scrappy 

Scrappy is a very simple web scraper that fetches news headlines along with their visit links from [Hacker News](https://news.ycombinator.com/) and mails them to a specified email address.

---

## 📁 Files

- `bot.py`: The actual bot that does scraping and emailing.
- `cred.py`: Holds sensitive credentials used by `bot.py`.
  - `FEA`: Sending Gmail address.
  - `FEA_PASS`: App password for the Gmail account.
  - `TEA`: Target email address where the headlines will be sent.
  - `SS`: SMTP server (default: smtp.gmail.com).
  - `SP`: SMTP port (default: 587).
- `requirements.txt`: Lists Python dependencies to be installed via `pip`.

---

## ⚙️ How to Use
### Step 1: Prerequisites

Ensure you have the following installed:

- [Firefox](https://www.mozilla.org/en-US/firefox/new/) (required for Selenium)
- [Python](https://www.python.org/) and `pip`
- A Gmail account with an **App Password**

And, clone the repository:

```bash
git clone https://github.com/B-ROT/Scrappy.git
```

> 🔐 **Note:** App passwords are 12-character alphabet-only keys generated in your Google Account settings.  
> You **cannot** use your regular Gmail password here.

---

### Step 2: Set Up the Environment

#### 2.1 Navigate into the project folder

```bash
cd Scrappy-V2
```

#### 2.2 Create and activate a Python virtual environment

- On **Windows (PowerShell)**:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

- On **Linux**:

```bash
python -m venv .venv
source .venv/bin/activate
```

#### 2.3 Install required dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Add Your Credentials

Edit the `cred.py` file and fill in the following:

```python
FEA = "your-sending-gmail@gmail.com"
FEA_PASS = "your-12-letter-app-password"
TEA = "your-receiving-email@example.com"
SS = "smtp.gmail.com"
SP = 587
```

---

### Step 4: Run the Bot

After activating your virtual environment, run:

```bash
python bot.py
```

You should receive an email with the latest top headlines from Hacker News.

---

## 🔒 Security Note

- **DO NOT share your actual `cred.py`** file with credentials.
- If publishing this project publicly, consider renaming `cred.py` to `cred_template.py`, and adding `cred.py` to `.gitignore`.

---
