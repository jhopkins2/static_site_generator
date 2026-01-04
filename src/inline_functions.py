from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: [TextNode], delimiter: str, text_type: TextType):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        text_split = node.text.split(delimiter)

        if len(text_split) % 2 == 0:
            raise Exception(f"invalid syntax: Missing {delimiter} closure")

        for i, text_substr in enumerate(text_split):
            if text_substr == "":
                continue
            if i % 2 != 0:
                new_nodes.append(TextNode(text_substr, text_type))
            else:
                new_nodes.append(TextNode(text_substr, TextType.TEXT))

    return new_nodes
