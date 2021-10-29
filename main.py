import trees

me = trees.Knot("Swan")
print(me)
print(me.is_leaf())
my_child = trees.Knot("My child")

me.add_child(my_child)
print(me.children)
me.print_children()
print(my_child.parent)

mom = trees.Knot("Mom")
bro = trees.Knot("Loic")
mom.add_child(me)
mom.add_child(bro)
mom.print_children()

family_tree = trees.Tree(me)

family_tree.reset_root(me)

print(family_tree)