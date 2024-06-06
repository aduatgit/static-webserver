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


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")


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


def paragraph_to_html_node(paragraph):
    lines = paragraph.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(heading):
    level = 0
    for head in heading:
        if head == "#":
            level += 1
        else:
            break
    if level + 1 >= len(heading):
        raise ValueError(f"Invalid heading level: {heading}")

    text = heading[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(code):
    if not code.startswith("```") or not code.endswith("```"):
        raise ValueError("Invalid code block")

    text = code[4:-3]
    children = text_to_children(text)
    code_tag = ParentNode("code", children)
    return ParentNode("pre", [code_tag])


def quote_to_html_node(quote):
    lines = quote.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())

    quote = " ".join(new_lines)

    children = text_to_children(quote)

    return ParentNode("blockquote", children)


def ulist_to_html_node(ulist):
    lines = ulist.split("\n")

    children = []
    for line in lines:
        if not line.startswith("- ") and not line.startswith("* "):
            raise ValueError("Invalid unordered list block")
        line = line[2:]
        line_children = text_to_children(line)

        children.append(ParentNode("li", line_children))

    return ParentNode("ul", children)


def olist_to_html_node(olist):
    lines = olist.split("\n")

    children = []
    i = 1
    for line in lines:
        if not line.startswith(f"{i}. "):
            raise ValueError("Invalid ordered list block")
        line = line[3:]
        line_children = text_to_children(line)
        children.append(ParentNode("li", line_children))
        i += 1
    return ParentNode("ol", children)


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
