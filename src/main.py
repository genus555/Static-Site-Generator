from textnode import TextNode
from file_handler import *
from generate_page import generate_page_recursive
def main():

    source_to_public("static")
    generate_page_recursive("./content", "./template.html", "./public")

main()