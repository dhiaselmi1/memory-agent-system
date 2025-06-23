# Persistent Memory Agent System

🧠 **Real-World Use Case**  
Athena Research Group performs long-term research over multiple topics. Analysts frequently revisit past sessions and need an AI assistant that:  
- Supports ongoing research sessions per topic  
- Saves summaries, notes, and interactions  
- Allows seamless continuation of research from previous sessions  
- Persists memory across sessions  

## Project Goal

Build a multi-agent AI system where each research topic maintains its own conversation history and memory, enabling users to:  
- Start new topics or continue previous ones  
- Interact with a summarizer/explainer agent  
- View a timeline of notes and memory logs  
- Export session summaries  

## How It Works

1. **Topic Management:** Users select an existing topic or create a new one. Each topic has its own persistent memory stored in a TinyDB database.  
2. **Conversation History:** User inputs and AI responses are stored and retrieved per topic to maintain context across sessions.  
3. **AI Interaction:** Queries are sent to a local LLaMA2 model API which generates responses based on conversation context.  
4. **Memory Updates:** Every interaction updates the memory log, ensuring knowledge continuity.  
5. **User Interface:** Streamlit provides an intuitive frontend to manage topics, ask questions, view AI responses, and browse conversation history.

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/memory-agent-system.git
cd memory-agent-system
```
2.  **Install Python Dependencies:**
    It's recommended to create a virtual environment first:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```
    Then, install the required libraries:
    ```bash
    pip install streamlit    requests
    ```
    *(For a production setup, you might want to create separate `requirements.txt` files for `backend` and `frontend`.)*

 ## ▶️ Running the Application

1.  **Start the Frontend Application:**
    Open a *new* terminal, navigate to the `frontend` directory:
    ```bash
    streamlit run app.py
    ```
    This will open the Streamlit application in your web browser (typically at `http://localhost:8501`).



