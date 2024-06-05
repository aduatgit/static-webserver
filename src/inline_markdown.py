import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
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

    print(new_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches
