from docx import Document
import shutil, re, html
from .models import RunLocator

_TAG = re.compile(r'<r id="([^"]+)">(.*?)</r>', re.DOTALL)

def apply_translation(src, dst, blocks):
    shutil.copyfile(src, dst)
    doc = Document(dst)
    mapping = {}
    for b in blocks:
        for m in _TAG.finditer(b.tagged_text):
            mapping[m.group(1)] = html.unescape(m.group(2))
    for pi, p in enumerate(doc.paragraphs):
        for ri, r in enumerate(p.runs):
            rid = RunLocator("paragraph", para_idx=pi, run_idx=ri).to_id()
            if rid in mapping:
                r.text = mapping[rid]
    doc.save(dst)