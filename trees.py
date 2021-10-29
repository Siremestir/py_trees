class Tree:
    def __init__(self, knot) -> None:
        self.root = knot
    
    def __str__(self) -> str:
        return str(self.root) #temporary


class Knot:
    def __init__(self, label, children=[], parent=None) -> None:
        self.label = label
        self.children=children
        self.parent=parent

    def __str__(self) -> str:
        return self.label
    
    def is_leaf(self) -> bool:
        """Returns True if the knot doesn't have any children
        Returns False otherwise
        """
        return self.children == []

    def add_child(self, child) -> None:
        """Adds a knot to the children list and sets self to its parent
        """
        self.children.append(child)
        child.parent = self

    def print_children(self) -> None:
        """Displays the children in a readable list
        """
        display = []
        for child in self.children:
            display.append(str(child))
        print(display)