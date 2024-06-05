from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node
from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


# def heading_block_to_HTMLNode(heading):
#     h1 = "# "
#     h2 = "## "
#     h3 = "### "
#     h4 = "#### "
#     h5 = "##### "
#     h6 = "###### "

#     if heading.startwith(h1):
#         string = heading.split(h1)
#         return HTMLNode(h1, string[1])
#     if heading.startwith(h2):
#         string = heading.split(h2)
#         return HTMLNode(h2, string[1])

#     if heading.startwith(h3):
#         string = heading.split(h3)
#         return HTMLNode(h3, string[1])

#     if heading.startwith(h4):
#         string = heading.split(h4)
#         return HTMLNode(h4, string[1])

#     if heading.startwith(h5):
#         string = heading.split(h5)
#         return HTMLNode(h5, string[1])

#     if heading.startwith(h6):
#         string = heading.split(h6)
#         return HTMLNode(h6, string[1])

#     raise Exception("Not a heading")


# def paragraph_block_to_HTMLNode(paragraph):
#     return HTMLNode("p", paragraph)


# def ulist_block_to_HTMLNode(ulist):
#     lines = ulist.split("\n")

#     child_lst = []

#     for line in lines:
#         child_lst.append(LeafNode("li", line))

#     return HTMLNode("ul", "", child_lst)


# def olist_block_to_HTMLNode(ulist):
#     lines = ulist.split("\n")

#     child_lst = []

#     for line in lines:
#         child_lst.append(LeafNode("li", line))

#     return HTMLNode("ol", "", child_lst)

# def code_block_to_HTMLNode(code):
#     code.replace("```", "<code>")
