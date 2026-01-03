from htmlnode import HTMLNode

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


