# 🌿 MindPulse AI

<div align="center">

### Intelligent Mental Wellness Companion

*A calm, conversational AI assistant that helps users reflect on their emotions, receive personalized wellness guidance, and track emotional well-being.*

**IBM SkillsBuild – AI Automation & Intelligent Solutions Internship Project**

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Streamlit-Live-red?style=for-the-badge&logo=streamlit"/>
<img src="https://img.shields.io/badge/scikit--learn-ML-orange?style=for-the-badge&logo=scikitlearn"/>
<img src="https://img.shields.io/badge/Plotly-Analytics-3F4F75?style=for-the-badge&logo=plotly"/>

</div>

---

## 📖 Project Overview

**MindPulse AI** is a conversational AI-powered mental wellness assistant designed to provide a safe and calming space for users to express their feelings and receive supportive wellness guidance.

The application uses **Natural Language Processing (NLP)** to analyze emotional tone in user messages and responds with empathetic suggestions, breathing exercises, and wellness insights. It also maintains **emotion analytics** to help users observe patterns in their emotional well-being over time.

The interface is designed with a **light, nature-inspired aesthetic** featuring soft sage-green colors, leaf-themed visuals, and mobile-friendly chat interactions.

---

## ✨ Key Features

### 💬 Conversational Wellness Chatbot

* Natural chat-based interaction
* Context-aware wellness responses
* Friendly and supportive tone

### 🧠 Real-Time Emotion Detection

* NLP-based emotion classification
* Detects emotions such as **joy, sadness, fear, anger, and neutral**
* Displays confidence scores for predictions

### 🌿 Personalized Wellness Guidance

* Emotion-specific coping suggestions
* Stress and anxiety support prompts
* Mindfulness and self-care recommendations

### 🫁 Guided Breathing Exercises

* Built-in **4-4-6 breathing technique**
* Quick 30-second calming exercise

### 📊 Emotion Analytics Dashboard

* Tracks detected emotions during conversations
* Visualizes emotion frequency using Plotly charts
* Displays dominant emotional trends

### 🌼 Dynamic Daily Wellness Intention

* Fetches inspirational wellness quotes from an external resource
* Cached daily for a consistent experience

### 📱 Responsive Mobile Design

* Optimized for phones and tablets
* Collapsible sidebar on smaller screens
* Touch-friendly chat interface

---

## 🧩 System Architecture

```text
User
  │
  ▼
Streamlit Chat Interface
  │
  ▼
NLP Emotion Classifier
  │
  ├── Emotion Detection
  ├── Confidence Estimation
  └── Wellness Scoring
  │
  ▼
Recommendation Engine
  │
  ▼
Analytics Dashboard (Plotly)
```

---

## 🛠️ Technology Stack

| Category             | Technology                                |
| -------------------- | ----------------------------------------- |
| Programming Language | Python 3.11                               |
| Web Framework        | Streamlit                                 |
| Machine Learning     | scikit-learn                              |
| NLP                  | CountVectorizer + Multinomial Naive Bayes |
| Data Handling        | Pandas                                    |
| Visualization        | Plotly                                    |
| API Integration      | Requests                                  |
| Deployment           | Streamlit Community Cloud                 |
| Version Control      | Git & GitHub                              |

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/MindPulseAI.git
cd MindPulseAI
```

### 2️⃣ Create a virtual environment

**Windows (PowerShell)**

```powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

Open the local URL shown in the terminal (usually **http://localhost:8501**).

---

## 🌐 Live Demo

🔗 **Deployed App:** `https://your-app-name.streamlit.app`

*(Replace this with your actual Streamlit Cloud URL after deployment.)*

---

## 📂 Project Structure

```text
MindPulseAI/
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Ignored files
│
└── .streamlit/
    └── config.toml            # Streamlit theme configuration
```

---

## 📸 Screenshots

### 🌿 Home Screen

Add a screenshot here after deployment.

### 💬 Chat Interface

Add a screenshot of the chatbot conversation.

### 📊 Emotion Analytics

Add a screenshot of the analytics dashboard.

---

## 🎯 How It Works

### Step 1 – User Input

The user types a message describing their feelings.

### Step 2 – Emotion Analysis

The NLP model processes the text and predicts the most likely emotion.

### Step 3 – Wellness Response

The assistant generates a supportive response tailored to the detected emotion.

### Step 4 – Analytics Update

The detected emotion is added to the session history and visualized in the dashboard.

---

## 🧪 Example Interaction

**User**

> I feel stressed and anxious about my exams.

**MindPulse AI**

> **Detected emotion:** FEAR
> **Confidence:** 86.4%
> **Wellness score:** 42/100
>
> Anxiety can feel overwhelming. Try grounding yourself by taking three slow breaths and focusing on what you can control right now.

---

## 🔒 Privacy & Ethics

* Conversations are stored only in the active session unless additional storage is added.
* No personal data is shared with third parties.
* The application is designed for **educational and wellness support purposes only**.

---

## ⚠️ Disclaimer

**MindPulse AI is not a medical or psychological diagnostic tool.**
It is an educational prototype and should not replace professional mental health care, counseling, or emergency support services.

If you are experiencing severe emotional distress, please contact a licensed mental health professional or a local emergency support service.

---

## 👩‍💻 Team IntelliCrew

This project was developed by **Team IntelliCrew** as part of the **IBM SkillsBuild Internship**.

* **Ramya Sri Pichuka**
* **Harshinee Shree G**
* **Muhammad Haroon Rasheed M K**
* **Vikasini S**
* **Rajeshwari R**

---

## Acknowledgements

* **IBM SkillsBuild** for the internship opportunity
* **Streamlit** for the rapid web app framework
* **scikit-learn** for lightweight machine learning tools
* **Plotly** for interactive analytics
* **Quotable API** for daily wellness inspirations

---

<div align="center">

### 🌱 Take a deep breath. Your well-being matters.

**MindPulse AI — Built with empathy, intelligence, and care.**

</div>
