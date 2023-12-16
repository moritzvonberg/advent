
import re
from typing import Generator, Iterator
# short function names 

def ns(line: str) -> Generator[int]:
    """parse numbers from line"""
    return map(int, re.finditer(r"\d+", line))