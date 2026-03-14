# 🔍 FraudForge — Autonomous Fraud Detection Swarm

> **Track B: Quantitative Forge** | Hackathon 2025 Submission

An autonomous multi-agent fraud detection system that analyzes CSV datasets, detects anomalies, and generates full risk intelligence reports using Google Gemini AI.

---

## 🎬 Demo Video

[![FraudForge Demo](https://img.youtube.com/vi/4jpmUNQcwmg/0.jpg)](https://youtu.be/4jpmUNQcwmg)

▶️ Watch the full demo: https://youtu.be/4jpmUNQcwmg

---

## 🏗️ System Architecture Diagram (A2A Flow)

```
┌─────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                        │
│                  fraudforge_gemini.html                      │
│            (CSV Upload → Trigger Analysis → View Report)     │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP POST /chat
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   ORCHESTRATOR AGENT                         │
│                   gemini_proxy.py                            │
│         - Receives CSV data from frontend                    │
│         - Builds structured prompt                           │
│         - Routes to Gemini AI                                │
│         - Handles errors & retries                           │
└─────────────────────┬───────────────────────────────────────┘
                      │ google-genai SDK
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  ANALYSIS AGENT                              │
│               Google Gemini 2.0 Flash                        │
│         - Pattern Recognition Agent                          │
│         - Anomaly Detection Agent                            │
│         - Risk Scoring Agent                                 │
│         - Report Generation Agent                            │
└─────────────────────┬───────────────────────────────────────┘
                      │ Structured JSON Response
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   REPORTING AGENT                            │
│              fraudforge_gemini.html (JS)                     │
│         - Parses AI response                                 │
│         - Renders risk dashboard                             │
│         - Highlights flagged rows                            │
│         - Displays anomaly severity levels                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🤖 Agent Profiles (Role Descriptions)

### 1. Orchestrator Agent — `gemini_proxy.py`
- **Role**: Central coordinator that manages the flow between frontend and AI
- **Responsibilities**: Authenticate requests, build prompts, forward to Gemini, handle failures
- **Recovery**: Returns structured error messages with HTTP status codes for graceful frontend handling

### 2. Pattern Recognition Agent — Gemini 2.0 Flash
- **Role**: Scans CSV data for statistical anomalies and suspicious patterns
- **Detects**: Duplicate entries, outlier values, round-number bias, velocity attacks
- **Output**: Structured JSON with anomaly list and severity levels

### 3. Risk Scoring Agent — Gemini 2.0 Flash
- **Role**: Computes an overall fraud risk score (0–100) based on detected patterns
- **Logic**: Weighs frequency, severity, and type of anomalies
- **Output**: Risk score + confidence percentage

### 4. Reporting Agent — `fraudforge_gemini.html` (JavaScript)
- **Role**: Renders the final intelligence report to the user
- **Responsibilities**: Parse JSON, display dashboard, highlight flagged rows, show severity badges
- **Recovery**: Handles malformed JSON responses with fallback parsing

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.9+
- Google Gemini API Key → [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

### Installation

```bash
# Clone the repo
git clone https://github.com/Virocchan/fraudforge.git
cd fraudforge

# Install dependencies
pip install flask flask-cors google-genai
```

### Running the App

**Terminal 1 — Start the AI proxy:**
```bash
python gemini_proxy.py
```
Expected output:
```
✅ FraudForge proxy running at http://localhost:8181
```

**Terminal 2 — Start the web server:**
```bash
python -m http.server 3000
```

**Open browser:**
```
http://localhost:3000/fraudforge_gemini.html
```

### Usage
1. Enter your Gemini API key (`AIza...`) → click **SAVE KEY**
2. Upload any `.csv` file (drag & drop or click)
3. Click **LAUNCH SWARM ANALYSIS**
4. View full fraud report with risk score, anomalies, and flagged rows

---

## 📁 Directory Structure

```
/agents
  └── gemini_proxy.py         # Orchestrator + AI routing agent
/tools
  └── gemini_proxy.py         # MCP-style tool server (Flask)
/app
  └── fraudforge_gemini.html  # Frontend agent + reporting UI
requirements.txt
README.md
```

---

## 🧠 Agentic Features

| Feature | Description |
|---|---|
| **Reasoning Traces** | AI returns detailed pattern analysis explaining WHY each anomaly is flagged |
| **Failure Recovery** | Proxy catches all exceptions and returns structured errors, frontend handles gracefully |
| **Structured Output** | Forces JSON schema compliance for reliable agent-to-agent communication |
| **Severity Classification** | Each anomaly auto-classified as HIGH / MEDIUM / LOW |
| **Confidence Scoring** | AI reports its own confidence level for transparency |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vanilla HTML/CSS/JS |
| Proxy/Orchestrator | Python Flask + flask-cors |
| AI Model | Google Gemini 2.0 Flash |
| AI SDK | google-genai |
| Fonts | Orbitron, Rajdhani, Share Tech Mono |

---

## 🔒 Security Note

**Never commit your API key to GitHub.** The key is entered only in the browser UI and sent via `X-API-Key` header — it is never stored or logged.

---

*Built for Hackathon 2025 — Track B: Quantitative Forge*
