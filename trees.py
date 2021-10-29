class Tree:
    def __init__(self, knot):
        self.root = knot
    
    def __str__(self) -> str:
        return str(self.root) #temporary


class Knot:
    def __init__(self, label, children=[], parent=None):
        self.label = label
        self.children=children
        self.parent=parent

    def __str__(self) -> str:
        return self.label
    
    def is_leaf(self):
        """Returns True if the knot doesn't have any children
        Returns False otherwise
        """
        return self.children == []

    def add_child(self, child):
        """Adds a knot to the children list
        """