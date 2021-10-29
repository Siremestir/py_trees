class Tree:
    def __init__(self, knot) -> None:
        self.root = knot
    
    def __str__(self) -> str:
        to_display = "Tree from " + str(self.root)
        to_display = to_display + ": " + str(self.count_knots(self.root)) + " knots"
        return to_display
    
    def reset_root(self, knot) -> None:
        """Sets the root of the tree to the highest parent found from the
        given knot
        """
        if knot.parent == None:
            self.root = knot
        else:
            self.reset_root(knot.parent)
    
    def count_knots(self, knot) -> int:
        """Counts how many knots are in the tree with the given knot
        as the root
        """
        count=1
        for child in knot.children:
            count += 1
            count += self.count_knots(child)
        return count
    
    def display(self, knot, spacing=0) -> None:
        """Displays the whole tree with the knot given as the root
        """
        print(" "*spacing+ str(knot))
        for child in knot.children:
            self.display(child, spacing+1)


class Knot:
    def __init__(self, label) -> None:
        self.label = label
        self.children=[]
        self.parent=None
        self.siblings=False

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
    
    def add_sibling(self, sibling) -> None:
        """Adds a sibling to self.
        If self has no parent, creates a ghost parent"""
        self.siblings = True
        sibling.siblings = True
        if self.parent != None:
            self.parent.add_child(sibling)
        else:
            parent = Knot("(abstract root)")
            parent.add_child(self)
            parent.add_child(sibling)
    
    def move_left(self) -> None:
        """Moves self left in the tree. Makes it the next sibling to its parent.
        If self has no parent, an abstract one will be created."""
        pass

    def move_right(self) -> None:
        """Moves self right in the tree. Makes it the first child to its older sibling.
        If self has no older sibling, an abstract one will be created."""
        pass

    def move_up(self) -> None:
        """Moves self up in the tree. Makes it the older sibling to its older sibling.
        If self has no older sibling, an abstract one will be created."""
        pass

    def move_down(self) -> None:
        """Moves self down in the tree. Makes it the younger sibling to its younger sibling.
        If self has no younger sibling, an abstract one will be created."""
        pass