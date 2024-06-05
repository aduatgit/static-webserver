import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_str = node.text.split(delimiter)
        length = len(split_str)

        if not length % 2:
            raise Exception("Missing closing delimiter")

        for i in range(0, length):
            if split_str[i] == "":
                continue
            if not i % 2:
                new_nodes.append(TextNode(split_str[i], text_type_text))
            else:
                new_nodes.append(TextNode(split_str[i], text_type))

    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches  # [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches  # [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]


def split_nodes_image(old_nodes):

    new_nodes = []

    for node in old_nodes:

        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        text = node.text

        for image in images:
            img_text = image[0]
            img_url = image[1]

            split_str = text.split(f"![{img_text}]({img_url})", 1)

            if len(split_str) != 2:
                raise ValueError("Invalid markdown, image section not closed")

            if split_str[0] != "":
                new_nodes.append(TextNode(split_str[0], text_type_text))

            new_nodes.append(TextNode(img_text, text_type_image, img_url))
            text = split_str[1]

        if text != "":
            new_nodes.append(TextNode(text, text_type_text))

    return new_nodes


def split_nodes_link(old_nodes):

    new_nodes = []

    for node in old_nodes:

        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        text = node.text

        for link in links:
            link_text = link[0]
            link_url = link[1]

            split_str = text.split(f"[{link_text}]({link_url})", 1)
            if len(split_str) != 2:
                raise ValueError("Invalid markdown, link section not closed")

            if split_str[0] != "":
                new_nodes.append(TextNode(split_str[0], text_type_text))

            new_nodes.append(TextNode(link_text, text_type_link, link_url))
            text = split_str[1]
        if text != "":
            new_nodes.append(TextNode(text, text_type_text))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", "bold")

    nodes = split_nodes_delimiter(nodes, "*", "italic")

    nodes = split_nodes_delimiter(nodes, "`", "code")

    nodes = split_nodes_image(nodes)

    nodes = split_nodes_link(nodes)

    return nodes
