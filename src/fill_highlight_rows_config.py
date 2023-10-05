from typing import List
from src.highlight_rows_config import HIGHLIGHT_ROWS


def fill_highlight_rows_config(sections: List[str], types: List[str], ids: List[int]):
    if len(sections) == 0 or len(types) == 0:
        return

    for section in sections:
        HIGHLIGHT_ROWS[section] = HIGHLIGHT_ROWS.get(section) or {}
        for type in types:
            HIGHLIGHT_ROWS[section][type] = ids
