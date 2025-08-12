from textnode import TextNode
from file_handler import *
from generate_page import generate_page
def main():

    source_to_public("static")
    generate_page("./content/index.md", "./template.html", "./public/index.html")

main()