import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown_document: str):
    
    temp_strs = markdown_document.split("\n\n")
    
    blocks = []
    for temp_str in temp_strs:
        if temp_str == "":
            continue

        blocks.append(temp_str.strip())

    return blocks

def block_to_blocktype(markdown_block: str) -> BlockType:
    
    if re.match(r'^(#{1,6})\s+.*', markdown_block):
        return BlockType.HEADING

    if re.match(r'^```[\r]?\n[\s\S]*?\n```$', markdown_block):
        return BlockType.CODE

    if re.match(r'^> (.*)\n', markdown_block, re.MULTILINE):
        return BlockType.QUOTE

    if re.match(r'- (.*)\n', markdown_block, re.MULTILINE):
        return BlockType.UNORDERED_LIST

    if re.match(r'^\d+\. (.*)\n', markdown_block, re.MULTILINE):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH



