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

        return " ".join([f'{key}="{self.props[key]}"' for key in self.props.keys()])

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
