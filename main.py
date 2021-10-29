import trees

me = trees.Knot("Swan")
print(me)
print(me.is_leaf())
my_child = trees.Knot("My child")

me.add_child(my_child)
print(me.children)
me.print_children()

family_tree = trees.Tree(me)
print(family_tree)