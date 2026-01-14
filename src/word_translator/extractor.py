from docx import Document
import html
from .models import TaggedBlock, ExtractionResult, RunLocator

def extract_docx(path: str) -> ExtractionResult:
    doc = Document(path)
    blocks = []
    for pi, p in enumerate(doc.paragraphs):
        text = ""
        for ri, r in enumerate(p.runs):
            rid = RunLocator("paragraph", para_idx=pi, run_idx=ri).to_id()
            text += f'<r id="{rid}">{html.escape(r.text)}</r>'
        blocks.append(TaggedBlock(f"body:p{pi}", "paragraph", text))
    return ExtractionResult(path, blocks, {"count": len(blocks)})