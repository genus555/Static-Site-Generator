from textnode import TextNode
from file_handler import *
from generate_page import generate_page_recursive
import sys
def main():

    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    source_to_public("static", "./docs")
    generate_page_recursive("./content", "./template.html", "./docs", basepath)

main()