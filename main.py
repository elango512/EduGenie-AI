from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path


app = FastAPI(
    title="EduGenie - AI Learning Assistant",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "application": "EduGenie"
    }


@app.post("/qa")
async def qa(question: str = Form(...)):
    result = answer_question(question)

    return {
        "success": True,
        "result": result
    }


@app.post("/explain")
async def explain(text: str = Form(...)):
    result = explain_concept(text)

    return {
        "success": True,
        "result": result
    }


@app.post("/quiz")
async def quiz(text: str = Form(...)):
    result = generate_quiz(text)

    return {
        "success": True,
        "result": result
    }


@app.post("/summarize")
async def summarize(text: str = Form(...)):
    result = summarize_text(text)

    return {
        "success": True,
        "result": result
    }


@app.post("/learn/recommendations")
async def learning_recommendations(
    topic: str = Form(...),
    level: str = Form("Beginner")
):
    result = recommend_learning_path(topic, level)

    return {
        "success": True,
        "result": result
    }