from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):

    def test_html_create(self):
        node = HTMLNode("p", "Blarg", None, {"href":"http://www.boot.dev"})
        test_string = "HTMLNode(p, Blarg, None, {'href': 'http://www.boot.dev'})"
        self.assertEqual(node.__repr__(), test_string)

    def test_props_to_html(self):
        node = node = HTMLNode("p", "Blarg", None, {"href":"https://www.boot.dev", "target":"__blank"})
        test_str = ' href="https://www.boot.dev" target="__blank"'
        self.assertEqual(node.props_to_html(), test_str)

    def test_html_children(self):
        child_node = HTMLNode(None, None, None, None)
        node = HTMLNode("p", "Blarg", [child_node], None)
        self.assertNotEqual(node, child_node)

    def test_empty_node_repr(self):
        node = HTMLNode()
        test_str = "HTMLNode(None, None, None, None)"
        self.assertEqual(node.__repr__(), test_str)

    def test_none_vs_empty(self):
        node = HTMLNode("p", "Blarg")
        node2 = HTMLNode("p", "Blarg", [], {})
        self.assertEqual(node, node2)

    def test_eq(self):
        child = HTMLNode()
        node = HTMLNode("p", "Blarg", [child], {"href":"www.boot.dev"})
        node2 = HTMLNode("p", "Blarg", [child], {"href":"www.boot.dev"})
        self.assertEqual(node, node2)

    def test_empty_props(self):
        node = HTMLNode("p", "Blarg", [])
        node2 = HTMLNode("p", "Blarg", None, None)
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
