import streamlit as st
from transformers import pipeline
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

import requests
import random

# ---------------------------------------------------
# DAILY AFFIRMATION FROM API
# ---------------------------------------------------
import requests

@st.cache_data(ttl=86400)  # cache for 24 hours
def get_daily_affirmation():
    try:
        response = requests.get(
            "https://api.quotable.io/random?tags=inspirational|wisdom|happiness",
            timeout=5
        )

        data = response.json()

        return data["content"], data["author"]

    except Exception:
        return (
            "Take a deep breath. You are doing better than you think.",
            "MindPulse AI"
        )

    # Fallback quotes if API fails
    fallback_quotes = [
        ("You are allowed to rest.", "MindPulse AI"),
        ("Your feelings are valid.", "MindPulse AI"),
        ("One gentle step at a time is enough.", "MindPulse AI"),
        ("Progress does not have to be perfect.", "MindPulse AI"),
        ("Breathe. You are doing better than you think.", "MindPulse AI")
    ]

    return random.choice(fallback_quotes)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="MindPulse AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------
# LOAD AI MODEL
# ---------------------------------------------------
@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        top_k=None
    )

classifier = load_model()

# ---------------------------------------------------
# AESTHETIC LIGHT CSS
# ---------------------------------------------------
st.markdown(
    """
<style>

/* ---------- APP BACKGROUND ---------- */
.stApp {
    background: linear-gradient(180deg, #F7FBF4 0%, #EEF6E8 100%);
}

/* Decorative leaves */
.stApp::before {
    content: "";
    position: fixed;
    top: -40px;
    right: -20px;
    width: 260px;
    height: 260px;
    background-image: url('https://cdn-icons-png.flaticon.com/512/415/415733.png');
    background-size: contain;
    background-repeat: no-repeat;
    opacity: 0.12;
    z-index: 0;
}

.stApp::after {
    content: "";
    position: fixed;
    bottom: -50px;
    left: -30px;
    width: 300px;
    height: 300px;
    background-image: url('https://cdn-icons-png.flaticon.com/512/2909/2909761.png');
    background-size: contain;
    background-repeat: no-repeat;
    opacity: 0.10;
    z-index: 0;
}

/* Main container */
.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    position: relative;
    z-index: 1;
}

/* ---------- HERO ---------- */
.hero {
    background: rgba(255,255,255,0.78);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.75);
    padding: 2.4rem;
    border-radius: 30px;
    text-align: center;
    box-shadow: 0 12px 28px rgba(107,175,146,0.18);
    margin-bottom: 1.2rem;
}

.hero h1 {
    color: #2F5D44;
    font-size: 3rem;
    margin-bottom: 0.3rem;
}

.hero h3 {
    color: #6BAF92;
    margin-top: 0;
    font-weight: 600;
}

.hero p {
    color: #587565;
}

/* ---------- GLASS CARDS ---------- */
.glass-card {
    background: rgba(255,255,255,0.78);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.7);
    border-radius: 24px;
    padding: 1rem 1.1rem;
    box-shadow: 0 10px 24px rgba(107,175,146,0.12);
}

.metric-value {
    font-size: 1.9rem;
    font-weight: 700;
    color: #2F5D44;
}

.metric-label {
    color: #6C8A76;
}

/* ---------- CHAT BUBBLES ---------- */
[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.82);
    border: 1px solid rgba(220,235,223,0.9);
    border-radius: 24px;
    padding: 0.9rem 1rem;
    box-shadow: 0 8px 20px rgba(107,175,146,0.10);
}

/* User bubble */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: linear-gradient(135deg, #DFF1E3 0%, #CFE8D5 100%);
}

/* Assistant bubble */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: linear-gradient(135deg, #FFFFFF 0%, #F3F8EF 100%);
}

/* ---------- SIDEBAR ---------- */
[data-testid="stSidebar"] {
    background: rgba(245,250,241,0.92);
    border-right: 1px solid rgba(107,175,146,0.15);
}

[data-testid="stSidebar"] * {
    color: #2F5D44 !important;
}

/* ---------- INPUT ---------- */
.stChatInputContainer {
    background: rgba(255,255,255,0.92);
    border: 1px solid #CFE3D4;
    border-radius: 24px;
    padding: 0.35rem;
    box-shadow: 0 8px 18px rgba(107,175,146,0.10);
}

.stChatInputContainer textarea {
    color: #2F5D44 !important;
}

/* ---------- BUTTONS ---------- */
.stButton > button {
    background: linear-gradient(90deg, #7CB69A, #5FA585);
    color: white;
    border: none;
    border-radius: 999px;
    padding: 0.65rem 1.3rem;
    font-weight: 600;
    box-shadow: 0 8px 18px rgba(95,165,133,0.22);
}

.stButton > button:hover {
    background: linear-gradient(90deg, #6EAE90, #4E9475);
}

/* ---------- HEADINGS ---------- */
h1, h2, h3, h4 {
    color: #2F5D44 !important;
}

/* Hide Streamlit default header */
header[data-testid="stHeader"] {
    background: transparent;
}

/* ---------- MOBILE OPTIMIZATION ---------- */
@media (max-width: 768px) {

    .block-container {
        padding-left: 0.7rem;
        padding-right: 0.7rem;
        padding-top: 0.6rem;
    }

    .hero {
        padding: 1.3rem !important;
        border-radius: 22px !important;
    }

    .hero h1 {
        font-size: 2rem !important;
        line-height: 1.1;
    }

    .hero h3 {
        font-size: 1rem !important;
    }

    .hero p {
        font-size: 0.9rem !important;
    }

    .glass-card {
        padding: 0.9rem !important;
        border-radius: 18px !important;
        margin-bottom: 0.6rem;
    }

    .metric-value {
        font-size: 1.4rem !important;
    }

    .metric-label {
        font-size: 0.85rem !important;
    }

    [data-testid="stChatMessage"] {
        border-radius: 18px !important;
        padding: 0.75rem !important;
    }

    .stChatInputContainer {
        border-radius: 18px !important;
        padding: 0.25rem !important;
    }

    .section-title {
        font-size: 1.15rem !important;
    }

    [data-testid="stSidebar"] {
        width: 82vw !important;
        max-width: 320px !important;
    }

    .stApp::before,
    .stApp::after {
        width: 120px !important;
        height: 120px !important;
        opacity: 0.08 !important;
    }
}

/* Sidebar glass effect */
[data-testid="stSidebar"] {
    background: rgba(245,250,241,0.78) !important;
    backdrop-filter: blur(14px);
    border-right: 1px solid rgba(107,175,146,0.14);
}

/* Sidebar images rounded */
[data-testid="stSidebar"] img {
    border-radius: 18px;
    box-shadow: 0 8px 18px rgba(107,175,146,0.12);
}

</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# HERO
# ---------------------------------------------------
st.markdown(
    """
<div class="hero">
    <div style="font-size:3.2rem; margin-bottom:0.3rem;">🌿</div>
    <h1>MindPulse AI</h1>
    <h3>Intelligent Mental Wellness Companion</h3>
    <p style="font-size:1.05rem;">
        A calm space to reflect, chat, and receive personalized emotional wellness guidance ✨
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

cards = [
    ("24/7", "Wellness Support"),
    ("AI", "Emotion Analysis"),
    ("100", "Risk Score Scale"),
    ("SDG 3", "Good Health"),
]

for col, (value, label) in zip([c1, c2, c3, c4], cards):
    with col:
        st.markdown(
            f"""
            <div class="glass-card">
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
# ---------------------------------------------------
# PINTEREST-STYLE SIDEBAR
# ---------------------------------------------------

# Top aesthetic image
st.sidebar.image(
    "https://images.unsplash.com/photo-1490750967868-88aa4486c946?q=80&w=800&auto=format&fit=crop",
    use_container_width=True
)

st.sidebar.markdown(
    """
    <div style="text-align:center; padding:10px 0 0 0;">
        <h2 style="color:#2F5D44; margin-bottom:0;">🌿 Your Wellness Space</h2>
        <p style="color:#6C8A76; margin-top:4px;">
            A calm corner for reflection, breathing, and emotional balance
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# AI status card
st.sidebar.markdown(
    """
    <div style="
        background: rgba(255,255,255,0.75);
        border: 1px solid rgba(107,175,146,0.18);
        border-radius: 18px;
        padding: 14px;
        margin: 10px 0;
        box-shadow: 0 8px 18px rgba(107,175,146,0.08);
    ">
        <div style="color:#6C8A76; font-size:0.9rem;">AI Companion</div>
        <div style="color:#2F5D44; font-size:1.4rem; font-weight:700;">🟢 Online</div>
        <div style="color:#6C8A76; font-size:0.9rem;">Ready to listen and support you</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Daily affirmation
# ---------------------------------------------------
# DYNAMIC DAILY AFFIRMATION
# ---------------------------------------------------
quote, author = get_daily_affirmation()

st.sidebar.markdown("### 🌼 Today’s Wellness Intention")

st.sidebar.markdown(
    f"""
    <div style="
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(107,175,146,0.18);
        border-radius: 18px;
        padding: 16px;
        box-shadow: 0 8px 18px rgba(107,175,146,0.08);
    ">
        <div style="color:#2F5D44; font-style:italic; line-height:1.6; font-size:0.98rem;">
            “{quote}”
        </div>
        <div style="color:#6C8A76; text-align:right; margin-top:12px; font-size:0.9rem;">
            — {author}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
# Quick mood buttons
st.sidebar.markdown("### 😊 Quick Mood Check")

mood = st.sidebar.radio(
    "How are you feeling right now?",
    ["😊 Happy", "😌 Calm", "😟 Stressed", "😰 Anxious", "😢 Sad"],
    label_visibility="collapsed"
)

st.sidebar.markdown(f"**Current mood:** {mood}")

# Mini breathing card
st.sidebar.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #E7F5EA, #D7EFD9);
        border-radius: 18px;
        padding: 14px;
        margin-top: 12px;
        border: 1px solid rgba(107,175,146,0.18);
    ">
        <div style="color:#2F5D44; font-weight:700; margin-bottom:6px;">🫁 30-second reset</div>
        <div style="color:#55715B; font-size:0.92rem;">
            Inhale for <b>4s</b> · Hold for <b>4s</b> · Exhale for <b>6s</b>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Inspiration image
st.sidebar.markdown("### 🌿 Calm Inspiration")
st.sidebar.image(
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=800&auto=format&fit=crop",
    use_container_width=True
)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("MindPulse AI • Built with care for IBM SkillsBuild 💚")

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I’m **MindPulse AI** 🌿. I’m here to listen and help you reflect on how you’re feeling today. What’s on your mind?"
        }
    ]

if "emotion_history" not in st.session_state:
    st.session_state.emotion_history = []

# ---------------------------------------------------
# CHAT UI
# ---------------------------------------------------
st.markdown("<div class='section-title'>💬 Wellness Chat</div>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your thoughts here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    results = classifier(user_input)[0]
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    emotion = results[0]["label"]
    confidence = results[0]["score"] * 100

    st.session_state.emotion_history.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "emotion": emotion,
        "confidence": confidence
    })

    if emotion in ["joy", "love", "surprise"]:
        wellness_score = 88
    elif emotion in ["sadness", "anger", "fear", "disgust"]:
        wellness_score = 42
    else:
        wellness_score = 65

    responses = {
        "joy": "😊 That’s wonderful to hear. Hold onto this positive moment and notice what contributed to it.",
        "love": "💖 Feeling connected to others can be deeply comforting. Consider expressing gratitude to someone you care about.",
        "surprise": "🌼 Unexpected events can bring excitement or uncertainty. Give yourself a moment to process them gently.",
        "neutral": "😌 You seem fairly balanced right now. A short mindful break could help maintain that calm feeling.",
        "sadness": "💙 I’m sorry you’re feeling this way. Be gentle with yourself today, and if you can, reach out to someone supportive.",
        "fear": "🌿 Anxiety can feel overwhelming. Try placing both feet on the floor and taking three slow, steady breaths.",
        "anger": "🍃 Anger is a valid emotion. Taking a pause before reacting can help you respond in a way that feels right later.",
        "disgust": "🌱 That sounds uncomfortable. Creating a little distance from the situation may help you regain clarity."
    }

    reply = f"""
### 🌿 Emotion Insight

**Detected emotion:** `{emotion.upper()}`  
**Confidence:** `{confidence:.1f}%`  
**Wellness score:** `{wellness_score}/100`

{responses.get(emotion)}

#### ✨ Gentle suggestion
- Take a sip of water
- Relax your shoulders
- Breathe in slowly for **4 seconds**
- Exhale slowly for **6 seconds**
- Notice one thing around you that feels calming

I’m here with you. What do you think is contributing most to this feeling right now?
"""

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)

# ---------------------------------------------------
# ANALYTICS
# ---------------------------------------------------
st.write("---")
st.markdown("<div class='section-title'>📊 Emotion Analytics</div>", unsafe_allow_html=True)

if st.session_state.emotion_history:
    history_df = pd.DataFrame(st.session_state.emotion_history)

    a1, a2, a3 = st.columns(3)

    with a1:
        st.metric("Conversations", len(history_df))

    with a2:
        dominant = history_df["emotion"].mode()[0]
        st.metric("Most Frequent Emotion", dominant.upper())

    with a3:
        avg_conf = history_df["confidence"].mean()
        st.metric("Average Confidence", f"{avg_conf:.1f}%")

    emotion_counts = history_df["emotion"].value_counts().reset_index()
    emotion_counts.columns = ["Emotion", "Count"]

    fig = go.Figure(
        go.Bar(
            x=emotion_counts["Emotion"],
            y=emotion_counts["Count"],
            marker_color="#66bb6a",
            text=emotion_counts["Count"],
            textposition="auto"
        )
    )

    fig.update_layout(
        template="simple_white",
        height=320,
        title="Emotion Frequency",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Start chatting to generate your emotion analytics 🌱")

# ---------------------------------------------------
# BREATHING
# ---------------------------------------------------
st.write("---")
st.markdown("<div class='section-title'>🫁 Guided Breathing</div>", unsafe_allow_html=True)

with st.expander("Start a 30-second calming exercise"):
    st.markdown(
        """
### 🌿 4-4-6 Breathing

- **Inhale** gently for **4 seconds**
- **Hold** for **4 seconds**
- **Exhale** slowly for **6 seconds**
- Repeat this cycle **5 times**

This exercise can help calm the nervous system and reduce stress.
"""
    )

# ---------------------------------------------------
# SUPPORT
# ---------------------------------------------------
st.write("---")
st.markdown("<div class='section-title'>🚨 Need Immediate Support?</div>", unsafe_allow_html=True)

st.warning(
    "If you are experiencing severe emotional distress or thoughts of self-harm, please contact a trusted person or a mental health professional immediately."
)

st.info(
    "🇮🇳 **India:** Tele-MANAS mental health helpline — **14416** or **1-800-891-4416** (24/7)."
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.write("---")
st.caption(
    "MindPulse AI is an educational prototype developed for IBM SkillsBuild and is not a substitute for professional medical or mental health care."
)