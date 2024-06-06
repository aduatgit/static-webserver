from markdown_blocks import markdown_to_html_node
import os
from pathlib import Path


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("Document has no h1 header")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = open(from_path, "r")
    md = md_file.read()
    md_file.close()

    temp_file = open(template_path)
    temp = temp_file.read()
    temp_file.close()

    node = markdown_to_html_node(md)
    html = node.to_html()

    title = extract_title(md)

    new_html = temp.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    to_file = open(dest_path, "w")
    to_file.write(new_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dirs = os.listdir(dir_path_content)
    for dir in dirs:
        from_path = os.path.join(dir_path_content, dir)
        dest_path = os.path.join(dest_dir_path, dir)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(
                from_path,
                template_path,
                dest_path,
            )
        else:
            generate_pages_recursive(
                from_path,
                template_path,
                dest_path,
            )
