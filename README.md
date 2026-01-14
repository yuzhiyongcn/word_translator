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

## bug
目前还有翻译不完全的bug, 有些段落, 句子还是原始语言, 没有被翻译, 需要添加审核机制, 确保所有句子都被正确翻译