import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")

    def test_leaf_to_html_code(self):
        node = LeafNode("code", "Hello, world!")
        self.assertEqual(node.to_html(), "<code>Hello, world!</code>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Hello, world!", {"href":"https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Hello, world!</a>')

    def test_leaf_to_html_img(self):
        node = LeafNode("img", "", {"src":"http://www.boot.dev/boots.jpg", "alt":"This is Boots"})
        self.assertEqual(node.to_html(), '<img src="http://www.boot.dev/boots.jpg" alt="This is Boots"></img>')

    def test_leaf_raise_valueerror(self):
        node = LeafNode(None, None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_raw_text(self):
        node = LeafNode(None, "Blarg", None)
        self.assertEqual(node.to_html(), "Blarg")



if __name__ == "__main__":
    unittest.main()
