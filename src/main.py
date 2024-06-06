import os
import shutil

from copy_static import recursive_starter
from page_generator import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


# def main():
#     recursive_starter(curr_path="./static", dest="./public")
#     generate_page("./content/index.md", "./template.html", "./public/index.html")


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    recursive_starter(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
    )


if __name__ == "__main__":
    main()
