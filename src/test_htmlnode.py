import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_eq(self):
        prop = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=prop)
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        prop = {}
        node = HTMLNode(props=prop)
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_None(self):
        node = HTMLNode()
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    # LEAFNODE

    def test_LeafNode_to_html_no_prop(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected)

    def test_LeafNode_to_html_with_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_ParentNode_recursion_no_prop(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)

    def test_ParentNode_recursion_with_prop(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                LeafNode("a", "Click me!", {"href": "https://www.google.com"}),
            ],
        )
        expected = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<a href="https://www.google.com">Click me!</a></p>'
        self.assertEqual(node.to_html(), expected)

    def test_ParentNode_recursion_nested_parent(self):
        nested_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node = ParentNode(
            "p",
            [
                nested_node,
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                LeafNode("a", "Click me!", {"href": "https://www.google.com"}),
            ],
        )
        expected = '<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text<a href="https://www.google.com">Click me!</a></p>'
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
