from openai import OpenAI
import re, html
from .models import TaggedBlock

_TAG = re.compile(r'<r id="([^"]+)">(.*?)</r>', re.DOTALL)

class OpenAITranslator:
    def __init__(self, model="gpt-4o-mini"):
        self.client = OpenAI()
        self.model = model

    def translate_blocks(self, blocks, src, tgt):
        joined = "\n".join(f'<block id="{b.block_id}">{b.tagged_text}</block>' for b in blocks)
        system = """You are a professional translator. Your task:
1. Translate ALL text content inside <r> tags from source language to target language
2. Keep the XML structure with <block> and <r> tags exactly as provided
3. Do NOT skip any text - translate EVERY single piece of content
4. Preserve all tag attributes (id values must remain unchanged)
5. Output must include ALL blocks from the input"""
        user = f"Translate from {src} to {tgt}:\n\n{joined}"
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role":"system","content":system},{"role":"user","content":user}]
        )
        out = resp.choices[0].message.content
        out_blocks = []
        for b in blocks:
            m = re.search(f'<block id="{re.escape(b.block_id)}">(.*?)</block>', out, re.DOTALL)
            if m is None:
                # Block not in response (likely empty), keep original
                out_blocks.append(TaggedBlock(b.block_id, b.block_type, b.tagged_text))
            else:
                out_blocks.append(TaggedBlock(b.block_id, b.block_type, m.group(1)))
        return out_blocks