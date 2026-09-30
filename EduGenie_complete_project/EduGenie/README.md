# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a FastAPI + HTML/CSS/JavaScript educational assistant based on the supplied project document.

## Features

- Q&A — `/qa`
- Concept explanation — `/explain`
- Quiz generation — `/quiz`
- Summarization — `/summarize`
- Personalized learning path — `/learn/recommendations`
- Responsive browser UI
- Structured JSON responses for quiz and learning-path generation
- Optional LaMini-Flan-T5 local explanation backend with Gemini fallback

## Architecture

```text
EduGenie/
├── main.py
├── config.py
├── gemini_client.py
├── schemas.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── tests/
│   └── test_health.py
├── requirements.txt
├── requirements-local.txt
├── .env.example
├── .gitignore
└── README.md
```

## VS Code setup — Windows

1. Install Python 3.10+.
2. Open this folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Create a virtual environment:

```powershell
py -3 -m venv .venv
```

5. Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate
```

6. Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

7. Copy `.env.example` to `.env`.

8. Put your Google AI Studio Gemini API key into `.env`:

```text
GEMINI_API_KEY=your_real_key_here
```

9. Start the server:

```powershell
uvicorn main:app --reload
```

10. Open:

```text
http://127.0.0.1:8000
```

## API documentation

After starting the server:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- Health: `http://127.0.0.1:8000/health`

## Test the project

Run:

```powershell
pytest
```

The included tests do not call Gemini, so they can run without an API key.

For a full AI test, open the browser UI and try:

1. Ask a question: `What is photosynthesis?`
2. Explain: `Object oriented programming`
3. Quiz: paste a short educational paragraph.
4. Summarize: paste a long paragraph.
5. Learning path: `SQL`.

## Optional local LaMini explanation

The project document specifies LaMini-Flan-T5-783M for concept explanation. The default installation intentionally keeps this model optional because PyTorch/model downloads are much larger than the FastAPI app.

To enable it:

```powershell
pip install -r requirements-local.txt
```

Then edit `.env`:

```text
LOCAL_EXPLANATION_ENABLED=true
LOCAL_MODEL=MBZUAI/LaMini-Flan-T5-783M
```

The first local explanation may download model files. If the local model cannot load, EduGenie automatically falls back to Gemini.

## API examples

### Q&A

```powershell
curl -X POST http://127.0.0.1:8000/qa `
  -H "Content-Type: application/json" `
  -d '{"question":"What is an API?","level":"beginner"}'
```

### Explain

```powershell
curl -X POST http://127.0.0.1:8000/explain `
  -H "Content-Type: application/json" `
  -d '{"topic":"Photosynthesis","level":"school"}'
```

### Quiz

```powershell
curl -X POST http://127.0.0.1:8000/quiz `
  -H "Content-Type: application/json" `
  -d '{"text":"Water boils at 100 degrees Celsius at standard atmospheric pressure.","level":"beginner"}'
```

### Summary

```powershell
curl -X POST http://127.0.0.1:8000/summarize `
  -H "Content-Type: application/json" `
  -d '{"text":"Paste a long educational paragraph here.","level":"college"}'
```

### Learning path

```powershell
curl -X POST http://127.0.0.1:8000/learn/recommendations `
  -H "Content-Type: application/json" `
  -d '{"topic":"SQL","level":"beginner","hours_per_week":5}'
```

## Notes

- Keep `.env` private and never commit your API key.
- Gemini model availability can vary by account and region. Set `GEMINI_MODEL` to a model available to your Google AI Studio account if needed.
- The frontend talks only to the FastAPI backend; the Gemini key is never exposed to browser JavaScript.
