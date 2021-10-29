class Tree:
    def __init__(self, knot) -> None:
        self.root = knot
    
    def __str__(self) -> str:
        return str(self.root) #temporary
    
    def reset_root(self, knot) -> None:
        """Sets the root of the tree to the highest parent found from the
        given knot
        """
        if knot.parent == None:
            self.root = knot
        else:
            self.reset_root(knot.parent)


class Knot:
    def __init__(self, label) -> None:
        self.label = label
        self.children=[]
        self.parent=None

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