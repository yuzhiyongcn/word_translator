# Word Translator (OpenAI + uv)

This project uses **uv** to manage dependencies.

## Setup
Install uv first:
https://github.com/astral-sh/uv

Then:

```shell
uv venv
.venv/Scripts/activate
uv pip install -e .
```

## Usage
```shell
setx OPENAI_API_KEY your_key
word-translator input.docx --source-lang zh --target-lang en
```