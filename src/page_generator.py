from markdown_blocks import markdown_to_html_node
import os


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("Document has no h1 header")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = open(from_path)
    md = md_file.read()
    md_file.close()

    temp_file = open(template_path)
    temp = temp_file.read()
    temp_file.close()

    html = markdown_to_html_node(md).to_html()

    title = extract_title(md)

    new_html = temp.replace("{{ Title }}", title).replace("{{ Content }}", html)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    os.write(dest_path, new_html)
