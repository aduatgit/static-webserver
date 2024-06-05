class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = (
            tag  # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        )
        self.value = value  # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children  # A list of HTMLNode objects representing the children of this node
        self.props = props  # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        string = ""
        if self.props:
            for k in self.props:
                string += f' {k}="{self.props[k]}"'
            return string
        return ""


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Invalid HTML: no value")

        if not self.tag:
            return self.value

        prop = self.props_to_html()
        html = f"<{self.tag}{prop}>{self.value}</{self.tag}>"
        return html

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: no tag")
        if not self.children:
            raise ValueError("Invalid Node: no children")

        content = ""

        for child in self.children:
            content += child.to_html()

        prop = self.props_to_html()
        html = f"<{self.tag}{prop}>{content}</{self.tag}>"
        return html
