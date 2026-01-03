import unittest
from htmlnode import text_node_to_html_node, LeafNode
from textnode import TextType, TextNode

class test_textnode_to_htmlnode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href":"https://www.boot.dev"})

    def test_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, "https://www.boot.dev/boots.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"https://www.boot.dev/boots.jpg", "alt":node.text})

    def test_node_type_checking(self):
        node = LeafNode("p", "This is a test")
        with self.assertRaises(ValueError):
            html_node = text_node_to_html_node(node)

    def test_text_type_checking(self):
        node = TextNode("This is a text", "test")
        with self.assertRaises(Exception):
            html_node = text_node_to_html_node(node)

    def test_missing_img_link(self):
        node = TextNode("This is a text", TextType.IMAGE)
        with self.assertRaises(ValueError):
            html_node = text_node_to_html_node(node)

    def test_missing_link(self):
        node = TextNode("This is a text", TextType.LINK)
        with self.assertRaises(ValueError):
            html_node = text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
