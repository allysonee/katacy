import random
import time
import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Pageant Q&A Practice",
    page_icon="👑",
    layout="centered",
)

# ── Styles ─────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap');

    html, body, [data-testid="stApp"] {
        background: linear-gradient(135deg, #1a0533 0%, #2d1b4e 60%, #1a0533 100%);
        color: #f0e6ff;
        font-family: 'Inter', sans-serif;
    }

    /* hide the default Streamlit header/footer */
    #MainMenu, footer, header { visibility: hidden; }

    h1 {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem;
        text-align: center;
        color: #e8c9ff;
        letter-spacing: 0.04em;
        margin-bottom: 0.1rem;
    }

    .subtitle {
        text-align: center;
        color: #b89fd4;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    /* Question card */
    .question-card {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(200, 150, 255, 0.3);
        border-radius: 18px;
        padding: 2rem 2.4rem;
        margin: 1.5rem 0;
        backdrop-filter: blur(8px);
    }

    .question-card p {
        font-family: 'Playfair Display', serif;
        font-size: 1.35rem;
        line-height: 1.7;
        color: #f5eaff;
        margin: 0;
    }

    /* Timer display */
    .timer-display {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 700;
        font-family: 'Inter', sans-serif;
        letter-spacing: 0.05em;
        padding: 0.5rem 0;
    }

    .timer-label {
        text-align: center;
        font-size: 0.85rem;
        color: #b89fd4;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-top: -0.5rem;
    }

    /* Streamlit button overrides */
    .stButton > button {
        background: linear-gradient(135deg, #7b2fff, #a855f7);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.65rem 2rem;
        font-size: 1rem;
        font-weight: 500;
        width: 100%;
        letter-spacing: 0.03em;
        transition: opacity 0.2s;
    }
    .stButton > button:hover {
        opacity: 0.88;
        color: white;
        border: none;
    }

    /* Selectbox / radio labels */
    label, .stRadio label, .stSelectbox label {
        color: #c9a8f0 !important;
        font-size: 0.9rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    /* Divider */
    hr { border-color: rgba(200, 150, 255, 0.15); }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Question bank ──────────────────────────────────────────────────────────────
QUESTIONS = {
    "Women Empowerment": [
        "If you could change one systemic barrier that holds women back, what would it be and why?",
        "How do you personally define women's empowerment, and how do you live that definition every day?",
        "What advice would you give to a young girl who has been told she is 'too much' or 'not enough'?",
        "In what ways can men be better allies in the fight for gender equality?",
        "How do you balance ambition with the societal expectations placed on women?",
        "Who is a woman — historical or living — who changed the world quietly, and what can we learn from her?",
        "What does it mean to lead with both strength and compassion, and why does that matter for women in power?",
        "How can communities better support mothers who are also pursuing careers and personal dreams?",
        "If you were president for a day, what single policy would you implement to uplift women?",
        "How do you respond when your competence is questioned simply because of your gender?",
        "What role does education play in closing the gender gap, and how do we make it accessible to all girls?",
        "How can social media be used as a tool for women's empowerment rather than a source of comparison?",
    ],
    "Environment": [
        "What is one small daily habit every person can adopt that would collectively make a massive difference for our planet?",
        "How do you personally reconcile the convenience of modern life with the responsibility to protect the environment?",
        "If you could speak to world leaders about climate change, what is the one truth you would make them face?",
        "How can local communities take environmental action without waiting for national or global policy changes?",
        "What role should young people play in shaping the environmental decisions that will define their future?",
        "How do we make sustainability accessible to people who are focused on day-to-day survival?",
        "What is the connection between protecting the environment and protecting human rights?",
        "How can technology be both a cause of and a solution to our environmental crisis?",
        "What does leaving a healthy planet for future generations mean to you personally?",
        "If you had one year and unlimited resources to address a single environmental issue, what would you choose and why?",
        "How do we inspire environmental responsibility in children before it becomes an emergency for them?",
        "What is the most underrated environmental issue that deserves more public attention?",
    ],
    "Culture & Identity": [
        "How has your cultural background shaped the values you carry into every room you enter?",
        "What is one tradition from your heritage that you believe the whole world could benefit from?",
        "How do you navigate spaces where your identity is underrepresented or misunderstood?",
        "What does it mean to be proud of where you come from while still being open to growth and change?",
        "How can societies celebrate diversity without reducing people to stereotypes?",
        "If you could preserve one aspect of your culture for future generations, what would it be and why?",
        "How do language and storytelling shape the way a culture sees itself and its place in the world?",
        "What is the most important lesson your family or community taught you that schools never could?",
        "How do you define home — is it a place, a people, or something else entirely?",
        "In a world that is increasingly globalized, how do we keep local cultures from disappearing?",
        "How has encountering a culture different from your own changed the way you see yourself?",
        "What responsibility do public figures have in representing their culture with accuracy and dignity?",
    ],
    "General Personality": [
        "What is a failure you once experienced that turned out to be one of the greatest gifts of your life?",
        "If you could have dinner with anyone — living or historical — who would it be and what would you ask them?",
        "What is the bravest thing you have ever done, and what did it teach you about yourself?",
        "How do you stay grounded and true to yourself when the world is constantly telling you who to be?",
        "What does success mean to you, and has that definition changed as you have grown?",
        "If you had to describe yourself using only three words, which words would you choose and why?",
        "What is a cause you would give up everything for, and what drew you to it?",
        "How do you handle self-doubt, and what do you tell yourself on your hardest days?",
        "What is one thing most people do not know about you that you wish they did?",
        "If your life had a theme song, what would it be and what chapter of your life does it represent?",
        "What does kindness look like in action, and how do you practice it when it is inconvenient?",
        "How do you want to be remembered, and are you living in a way that reflects that today?",
    ],
}

TIMER_OPTIONS = {
    "No timer": 0,
    "30 seconds": 30,
    "45 seconds": 45,
    "60 seconds": 60,
    "90 seconds": 90,
}

# ── Session state defaults ─────────────────────────────────────────────────────
if "question" not in st.session_state:
    st.session_state.question = None
if "timer_running" not in st.session_state:
    st.session_state.timer_running = False

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("<h1>👑 Pageant Q&A Practice</h1>", unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Train your confidence. Master the moment.</p>',
    unsafe_allow_html=True,
)
st.markdown("---")

# ── Controls ───────────────────────────────────────────────────────────────────
col_topic, col_timer = st.columns([3, 2])

with col_topic:
    selected_topic = st.selectbox(
        "Topic",
        options=list(QUESTIONS.keys()),
        index=0,
    )

with col_timer:
    selected_timer_label = st.radio(
        "Timer",
        options=list(TIMER_OPTIONS.keys()),
        index=0,
        horizontal=False,
    )

timer_seconds = TIMER_OPTIONS[selected_timer_label]

st.markdown("---")

# ── Question picker ────────────────────────────────────────────────────────────
def generate_question(topic: str) -> str:
    pool = QUESTIONS[topic]
    last = st.session_state.get("last_question")
    choices = [q for q in pool if q != last] or pool
    return random.choice(choices)


# ── Generate button ────────────────────────────────────────────────────────────
if st.button("✨ Generate New Question", use_container_width=True):
    st.session_state.question = generate_question(selected_topic)
    st.session_state.last_question = st.session_state.question
    st.session_state.timer_running = True

# ── Question card ──────────────────────────────────────────────────────────────
if st.session_state.question:
    st.markdown(
        f'<div class="question-card"><p>{st.session_state.question}</p></div>',
        unsafe_allow_html=True,
    )

    # ── Timer ──────────────────────────────────────────────────────────────────
    if timer_seconds > 0 and st.session_state.timer_running:
        timer_placeholder = st.empty()

        for remaining in range(timer_seconds, -1, -1):
            if remaining > 10:
                color = "#a855f7"   # purple
            elif remaining > 5:
                color = "#f97316"   # orange
            else:
                color = "#ef4444"   # red

            if remaining == 0:
                timer_placeholder.markdown(
                    '<div class="timer-display" style="color:#ef4444;">TIME\'S UP!</div>'
                    '<p class="timer-label">Great job — reset and go again</p>',
                    unsafe_allow_html=True,
                )
            else:
                mins = remaining // 60
                secs = remaining % 60
                display = f"{mins}:{secs:02d}" if mins else f"0:{secs:02d}"
                timer_placeholder.markdown(
                    f'<div class="timer-display" style="color:{color};">{display}</div>'
                    '<p class="timer-label">Time remaining</p>',
                    unsafe_allow_html=True,
                )
                time.sleep(1)

        st.session_state.timer_running = False

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#7e5a9e; font-size:0.78rem;">'
    "Practice makes perfect &nbsp;·&nbsp; You've got this 👑"
    "</p>",
    unsafe_allow_html=True,
)
