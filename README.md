# 👑 Pageant Q&A Practice App

A Streamlit app that generates AI-powered pageant questions by topic with a countdown timer — so you can practice realistic Q&A conditions anytime.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your API key
Open `.env` and replace the placeholder with your real key:
```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```
Get a key at [console.anthropic.com](https://console.anthropic.com).

### 3. Run the app
```bash
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

## How to use
1. Select a **topic** from the dropdown
2. Choose a **timer** duration
3. Click **Generate New Question**
4. Answer out loud — the timer counts down with color changes (purple → orange → red)
5. Click Generate again for a new question

## Topics
- Women Empowerment
- Environment
- Culture & Identity
- General Personality

## Deploying to Streamlit Community Cloud (free)
1. Push this repo to GitHub (`.env` is in `.gitignore` — safe to push)
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Add `ANTHROPIC_API_KEY` as a secret in the Streamlit Cloud dashboard
4. Deploy — your app gets a public URL instantly
