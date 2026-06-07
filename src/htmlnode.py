



class HTMLNode:

    def __init__(
            self, 
            tag: str | None = None, 
            value: str | None = None, 
            children: list["HTMLNode"] | None = None, 
            props: dict[str, str] | None = None) -> None:

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):

        raise NotImplementedError("Overrided by child classes.")


    def props_to_html(self) -> str:

        if self.props is None:
            return ""

        formatted_str = ""

        for attr, value in self.props.items():
            formatted_str += f' {attr}="{value}"'

        return formatted_str

    def __repr__(self):

        return f"HTMLNode({self.tag},{self.value}, children: {self.children}, {self.props})"





class LeafNode(HTMLNode):

    def __init__(self, tag: str | None, value: str | None, props: dict[str, str] | None = None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props


    def to_html(self):
        if self.value is None:
            raise ValueError("Must have a value")

        if self.tag is None:
            return self.value
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


    def __repr__(self):

        return f"LeafNode({self.tag}, {self.value}, {self.props})"




class ParentNode(HTMLNode):

    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None):
        super().__init__(tag, None, children, props)
        self.tag = tag
        self.children = children
        self.props = props


    def to_html(self):
        if not self.tag:
            raise ValueError("tag required.")

        if not self.children:
            raise ValueError("children required.")

        the_children = ""
        for child in self.children:
            the_children += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{the_children}</{self.tag}>"






