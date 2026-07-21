# Pixelator

A simple full-stack app: type a description, get an AI-generated 16-bit pixel art image. The
backend calls OpenAI's model.

## Stack
- Backend: Python + Flask (app.py)
- Frontend: single static page (public/index.html), vanilla JS
- Model: gpt-image-2 via the OpenAI API

## Setup

1. Get an OpenAI API key from https://platform.openai.com/api-keys

2. Set it as an environment variable:
   ```
   export OPENAI_API_KEY="your-key-here"
   ```

3. Install dependencies (already present in this Anaconda env, but for a fresh one):
   ```
   pip install flask requests
   ```

## Run

```
export OPENAI_API_KEY="your-key-here"
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Configuration

| Variable         | Default                        | Purpose                     |
|------------------|--------------------------------|-----------------------------|
| `OPENAI_API_KEY` | *(required)*                   | Your OpenAI API key         |
| `OPENAI_MODEL`   | ``                     | Image model to use          |
| `PORT`           | `5000`                         | Local server port           |

## Example:
<img width="928" height="989" alt="Screenshot 2026-07-20 at 9 24 22 PM" src="https://github.com/user-attachments/assets/8a623d48-8f28-4b29-9e6b-83b0492c90b8" />
________________________________________________
<img width="1125" height="1028" alt="Screenshot 2026-07-20 at 9 18 02 PM" src="https://github.com/user-attachments/assets/0888b2a3-7c7e-4c7e-add4-44697fa3bbda" />
