# 👾 Pixelator

A simple full-stack app: type a description, get an AI-generated 16-bit pixel art image. The
backend calls OpenAI's model.

## Stack
- **Backend:** Python + Flask (`app.py`)
- **Frontend:** single static page (`public/index.html`), vanilla JS
- **Model:** `gpt-image-2` via the OpenAI API

## Setup

1. Get an OpenAI API key from https://platform.openai.com/api-keys

2. Set it as an environment variable:
   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```

3. Install dependencies (already present in this Anaconda env, but for a fresh one):
   ```bash
   pip install flask requests
   ```

## Run

```bash
export OPENAI_API_KEY="your-key-here"
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Configuration

| Variable         | Default                        | Purpose                     |
|------------------|--------------------------------|-----------------------------|
| `OPENAI_API_KEY` | *(required)*                   | Your OpenAI API key         |
| `OPENAI_MODEL`   | `dall-e-3`                     | Image model to use          |
| `PORT`           | `5000`                         | Local server port           |
