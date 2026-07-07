import unittest
from markdown_blocks import markdown_to_blocks, markdown_to_html_node, block_to_block_type, BlockType, extract_title






class TestMarkdownBlocks(unittest.TestCase):



        def test_markdown_to_blocks(self):

            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )


        def test_markdown_to_blocks_newlines(self):
            md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        

        def test_block_to_block_types(self):
            block = "# heading"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)
            block = "```\ncode\n```"
            self.assertEqual(block_to_block_type(block), BlockType.CODE)
            block = "> quote\n> more quote"
            self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
            block = "- list\n- items"
            self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
            block = "1. list\n2. items"
            self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
            block = "paragraph"
            self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


        def test_block_to_block_type_heading(self):
            mk = "# This is a heading"
            blk_type_res = block_to_block_type(mk)
            self.assertEqual(
                    blk_type_res,
                    BlockType.HEADING,
                    )

        
        

        def test_paragraph(self):

            md = """
This is **bolded** paragraph
text in a p
tag here

"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
            )

        def test_paragraphs(self):
            md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )

        def test_lists(self):
            md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
            )

        def test_headings(self):
            md = """
# this is an h1

this is paragraph text

## this is an h2
"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
            )

        def test_blockquote(self):
            md = """
> This is a
> blockquote block

this is paragraph text

"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
            )

        def test_code(self):
            md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            )


        

        def test_extract_title(self):
            result = extract_title("# Hello World!")
            self.assertEqual(
                    result,
                    "Hello World!"
                )


        def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

        def test_eq_double(self):
            actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

        def test_eq_long(self):
            actual = extract_title(
            """
# title

this is a bunch

of text

- and
- a
- list
"""
        )
        self.assertEqual(actual, "title")

        def test_none(self):
            try:
                extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass





if __name__ == "__main__":
    unittest.main()
