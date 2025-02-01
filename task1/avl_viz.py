from graphviz import Digraph
from avl import AVLNode, AVLTree

def add_nodes_edges(dot, node):
    if not node:
        return
    dot.node(str(node.key), f'{node.key}\nH:{node.height}\nS:{node.size}\nC:{node.count}')
    if node.left:
        dot.edge(str(node.key), str(node.left.key))
        add_nodes_edges(dot, node.left)
    if node.right:
        dot.edge(str(node.key), str(node.right.key))
        add_nodes_edges(dot, node.right)

def visualize_avl_tree(tree: AVLTree):
    dot = Digraph()
    if tree.root:
        add_nodes_edges(dot, tree.root)
    return dot

if __name__ == "__main__":
    tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25, 5, 15, 35, 45, 55, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 60000, 7000] * 2
    for v in values:
        tree.insert(v)
    
    dot = visualize_avl_tree(tree)
    dot.render('./avl_tree', format='png')

    print("Inorder:", tree.traverse("inorder"))
    print("Preorder:", tree.traverse("preorder"))
    print("Postorder:", tree.traverse("postorder"))
    print("Is AVL:", tree.validate_avl())
    print("Height:", tree._height(tree.root))
    print("Size:", tree._size(tree.root))
    
    left, right = tree.split(25)
    
    print("Is AVL left:", left.validate_avl())
    print("Is AVL right:", right.validate_avl())
    
    dot = visualize_avl_tree(left)
    dot.render('./avl_tree_left', format='png')
    
    dot2 = visualize_avl_tree(right)
    dot2.render('./avl_tree_right', format='png')
    
    right.merge(left)
    print("Is AVL merged:", right.validate_avl())
    
    right.remove(5)
    right.remove(5)
    
    dot3 = visualize_avl_tree(right)
    dot3.render('./avl_tree_merged', format='png')
    