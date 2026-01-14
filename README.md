# Word Translator (OpenAI + uv)

This project uses **uv** to manage dependencies.

## Setup
Install uv first:
https://github.com/astral-sh/uv

Then:

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

## Usage
```bash
export OPENAI_API_KEY=your_key
word-translator input.docx --source-lang zh --target-lang en
```