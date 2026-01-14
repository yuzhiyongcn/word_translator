import argparse
from pathlib import Path
from .extractor import extract_docx
from .translator import OpenAITranslator
from .applier import apply_translation

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--source-lang", default="zh")
    ap.add_argument("--target-lang", default="en")
    args = ap.parse_args()

    inp = Path(args.input)
    outp = inp.with_name(inp.stem + "." + args.target_lang + ".docx")

    ext = extract_docx(str(inp))
    tr = OpenAITranslator()
    translated = tr.translate_blocks(ext.blocks, args.source_lang, args.target_lang)
    apply_translation(str(inp), str(outp), translated)
    print("Output:", outp)