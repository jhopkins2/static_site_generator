from re import findall
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

def extract_markdown_images(text):
    return findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes: [TextNode]):
    new_nodes = []
    
    for old_node in old_nodes:

        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue

        extracted_images = extract_markdown_images(old_node.text)

        if not extracted_images:
            new_nodes.append(old_node)
            continue

        current_str = old_node.text
        
        for extracted_image in extracted_images:

            sections = current_str.split(f"![{extracted_image[0]}]({extracted_image[1]})", 1)

            if sections[0] == "":
                new_nodes.append(TextNode(extracted_image[0], TextType.IMAGE, extracted_image[1]))
            else:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(extracted_image[0], TextType.IMAGE, extracted_image[1]))
    
            current_str = sections[1]

        if current_str != "":
            new_nodes.append(TextNode(current_str, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes: [TextNode]):
    new_nodes = []
    
    for old_node in old_nodes:
        
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue

        extracted_images = extract_markdown_links(old_node.text)

        if not extracted_images:
            new_nodes.append(old_node)
            continue

        current_str = old_node.text
        
        for extracted_image in extracted_images:

            sections = current_str.split(f"![{extracted_image[0]}]({extracted_image[1]})", 1)

            if sections[0] == "":
                new_nodes.append(TextNode(extracted_image[0], TextType.IMAGE, extracted_image[1]))
            else:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(extracted_image[0], TextType.IMAGE, extracted_image[1]))
    
            current_str = sections[1]

        if current_str != "":
            new_nodes.append(TextNode(current_str, TextType.TEXT))

    return new_nodes

