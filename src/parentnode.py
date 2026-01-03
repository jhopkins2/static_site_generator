from htmlnode import HTMLNode

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
