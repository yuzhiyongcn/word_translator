from dataclasses import dataclass
from typing import Optional, Dict, Any, List, Literal

BlockType = Literal["paragraph", "table_cell_paragraph"]

@dataclass(frozen=True)
class RunLocator:
    block_type: BlockType
    para_idx: Optional[int] = None
    run_idx: Optional[int] = None
    table_idx: Optional[int] = None
    row_idx: Optional[int] = None
    cell_idx: Optional[int] = None
    cell_para_idx: Optional[int] = None

    def to_id(self) -> str:
        if self.block_type == "paragraph":
            return f"p{self.para_idx}r{self.run_idx}"
        return f"t{self.table_idx}r{self.row_idx}c{self.cell_idx}p{self.cell_para_idx}r{self.run_idx}"

@dataclass
class TaggedBlock:
    block_id: str
    block_type: BlockType
    tagged_text: str

@dataclass
class ExtractionResult:
    source_path: str
    blocks: List[TaggedBlock]
    meta: Dict[str, Any]