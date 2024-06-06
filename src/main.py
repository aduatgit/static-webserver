from textnode import TextNode
from copy_static import recursive_starter
from page_generator import generate_page


def main():
    recursive_starter(curr_path="../static", dest="../public")
    generate_page("../content/index.md", "../template.html", "../public/index.html")


if __name__ == "__main__":
    main()
