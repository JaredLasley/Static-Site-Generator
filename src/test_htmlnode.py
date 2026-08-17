import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(tag="p", props={"class": "intro", "id": "header"})
        correct_string = ' class="intro" id="header"'
        self.assertEqual(node.props_to_html(),correct_string)

    def test_props_nospace(self):
        node = HTMLNode(tag="p", props={"class": "intro", "id": "header"})
        incorrect_string = 'class="intro" id="header"'
        self.assertNotEqual(node.props_to_html(),incorrect_string)

    def test_tohtml(self):
        node = HTMLNode(
            tag="a",
            value="Click here",
            props={"href": "https://www.google.com", "target": "_blank"})
        self.assertRaises(NotImplementedError,node.to_html)

    def test_repr(self):
        node = HTMLNode(
            tag="a",
            value="Click here",
            props={"href": "https://www.google.com", "target": "_blank"})
        correct_string = "HTMLNode(tag = a, value = Click here, children = None, props = {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node),correct_string)