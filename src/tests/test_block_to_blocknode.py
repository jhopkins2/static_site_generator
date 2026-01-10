import unittest
from src.block_functions import BlockType, markdown_to_blocks, block_to_blocktype

class TestBlockToBlockType(unittest.TestCase):

    def test_block_to_heading(self):
        block_text = "### This is a heading\n"
        block_type = BlockType.HEADING

        self.assertEqual(block_to_blocktype(block_text), block_type)

    def test_block_to_code(self):
        block_text = '```\nThis is code\n```'
        block_type = BlockType.CODE

        self.assertEqual(block_to_blocktype(block_text), block_type)

    def test_block_to_quote(self):
        block_text = "> This is a quote"
        block_type = BlockType.QUOTE

        self.assertEqual(block_to_blocktype(block_text), block_type)

    def test_block_to_unordered(self):
        block_text = '''- This is an unordered list
- This is an unordered list
- This is an unordered list'''
        block_type = BlockType.UNORDERED_LIST

        self.assertEqual(block_to_blocktype(block_text), block_type)

    def test_block_to_ordered(self):
        block_text = '''1. This is an ordered list
2. This is an ordered list
3. This is an ordered list'''
        block_type = BlockType.ORDERED_LIST

        self.assertEqual(block_to_blocktype(block_text), block_type)

    def test_block_to_paragraph(self):
        block_text = "This is a heading"
        block_type = BlockType.PARAGRAPH

        self.assertEqual(block_to_blocktype(block_text), block_type)

    def test_multiline_to_blocktypes(self):
        block_text = '''# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item'''

        blocks = markdown_to_blocks(block_text)

        block_types = [block_to_blocktype(block) for block in blocks]

        self.assertEqual(block_types, [BlockType.HEADING, BlockType.PARAGRAPH, 
                                       BlockType.UNORDERED_LIST])

    def test_multiline_not_unordered(self):
        block_text = '''# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
2. This is a list item
- This is anotiher list item'''

        blocks = markdown_to_blocks(block_text)

        block_types = [block_to_blocktype(block) for block in blocks]

        self.assertEqual(block_types, [BlockType.HEADING, BlockType.PARAGRAPH, 
                                       BlockType.PARAGRAPH])





if __name__ == '__main__':
    unittest.main()
