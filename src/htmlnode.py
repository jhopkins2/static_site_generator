from textnode import TextNode, TextType

class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict[str, str] = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("The 'to_html' method has not been implemented.")

    def props_to_html(self) -> str:
        
        if not self.props:
            return ""
        
        props_str = ""
        for key in self.props.keys():
            props_str += f' {key}="{self.props[key]}"'

        return props_str

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children.__repr__()}, {self.props})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, HTMLNode):
            return False

        temp_self_children = self.children if self.children else []
        temp_self_props = self.props if self.props else {}
        temp_other_children = other.children if other.children else []
        temp_other_props = other.props if other.props else {}

        return (self.tag == other.tag and 
                self.value == other.value and 
                temp_self_children == temp_other_children and 
                temp_self_props == temp_other_props)

class ParentNode(HTMLNode):

    def __init__(self, tag: str, children: list, props: dict[str, str] = None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:

        if self.tag is None:
            raise ValueError("invalid HTML: no tag")

        if self.children is None:
            raise ValueError("invalid HTML: no children")

        html_str = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:

            html_str += child.to_html()

        html_str += f"</{self.tag}>"

        return html_str

class LeafNode(HTMLNode):

    def __init__(self, tag: str , value: str , props: dict[str, str] = None) -> None:
        super().__init__(tag = tag, value = value, props = props)

    def to_html(self) -> str:

        if self.value is None:
            raise ValueError("invalid HTML: no value")

        if self.tag is None:
            return self.value

        opening_tag = f"<{self.tag}{self.props_to_html()}>"

        closing_tag = f"</{self.tag}>"

        return opening_tag + self.value + closing_tag

    def text_node_to_html_node(self, text_node):

        if text_node.text_type not in TextType:
            raise Exception("TextType Error: invalid value")

def text_node_to_html_node(text_node):

    if not isinstance(text_node, TextNode):
        raise ValueError("argument error: text_node not a TextNode object")
        
    if text_node.text_type not in TextType:
        raise Exception("enum error: invalid TextType value")

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            if text_node.url is None:
                raise ValueError("textnode member error: missing url value")
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            if text_node.url is None:
                raise ValueError("textnode member error: missing url value")
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
