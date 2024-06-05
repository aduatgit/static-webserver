import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "http://google.com")
        node2 = TextNode("This is a text node", "bold", "http://google.com")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a text node", "bold", "http://google.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_neq_type(self):
        node = TextNode("This is a text node", "bold", "http://google.com")
        node2 = TextNode("This is a text node", "italic", "http://google.com")
        self.assertNotEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("This is a text node", "bold", "http://google.com")
        node2 = TextNode("This is NOT a text node", "bold", "http://google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
