# 📝 Text Summarization Microservice

A lightweight and efficient **FastAPI-based microservice** for summarizing long-form text using AI models. Built with simplicity, extensibility, and modern Python tooling in mind, ideal as a microservice.

---

## 🚀 Features

- REST API with FastAPI
- Supports customizable summarization with optional parameters
- Logs all requests and responses to `request_logs.json`
- Uses Pydantic for validation and structured responses
- Easily containerizable and cloud-deployable

---

## 📦 Requirements

Make sure to have Python 3.8+ installed.

.env file that follows this structure:
```.env
openai-compatible-model-url=*url*/v1
model-api-key=*key*
```
Please note that the model-api-key should be set to None
if the key is not required, or you will get an error.

Install dependencies in a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🏁 Running the App
To start the FastAPI server locally:

```bash
uvicorn main:app --reload
```

Visit the docs at http://127.0.0.1:8000/docs for interactive API testing.

---

## 🐋 Docker

You can also build the docker-image:
```bash
docker build -t summarizer .
```

And run it:
```bash
docker run -d -p 8000:8000 summarizer
```

Your app will be available at: http://localhost:8000