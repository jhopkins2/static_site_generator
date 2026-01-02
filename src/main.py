from textnode import TextNode, TextType

def main() -> None:
    test_text_node = TextNode("My name is Michael J. Caboose, and I hate babies.", TextType.LINK, "https://www.boot.dev")

    another_text_node = TextNode("This is some anchor text", TextType.BOLD)

    print(test_text_node)
    print(another_text_node)

    print(test_text_node == another_text_node)

if __name__ == "__main__":
    main()
