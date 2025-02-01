from avl import AVLNode, AVLTree
import copy

def test_insert():
    tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25, 5, 5, 5, 15, 35, 45, 55, 1000, -200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 60000, 7000]
    for v in values:
        tree.insert(v)
    assert tree.validate_avl() == True
    assert tree.size() == len(values)
    
def test_traverse():
    tree = AVLTree()
    values = [10, 20, 30, 40, 50, 50, 25]
    for v in values:
        tree.insert(v)
    assert tree.traverse("inorder") == sorted(values)
    assert tree.traverse("preorder") == [30, 20, 10, 25, 40, 50, 50]
    assert tree.traverse("postorder") == [10, 25, 20, 50, 50, 40, 30]
    
def test_split():
    tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25, 25, 25, 5, 15, 35, 45, 55, 1000, -200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 60000, 7000]
    for v in values:
        tree.insert(v)
    left, right = tree.split(25)
    assert left.validate_avl() == True
    assert left.traverse("inorder") == sorted([v for v in values if v <= 25])
    assert left.size() == len([v for v in values if v <= 25])
    assert right.validate_avl() == True
    assert right.traverse("inorder") == sorted([v for v in values if v > 25])
    assert right.size() == len([v for v in values if v > 25])
    
    
def test_merge():
    tree1 = AVLTree()
    tree2 = AVLTree()
    values1 = [10, 20, 30, 40, 50, 25, 5, 15, 35, 45, 55, 1000, -200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 60000, 7000]
    values2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for v in values1:
        tree1.insert(v)
    for v in values2:
        tree2.insert(v)
    tree1.merge(tree2)
    assert tree1.validate_avl() == True
    assert tree1.traverse("inorder") == sorted(values1 + values2)
    assert tree1.size() == len(values1 + values2)
    
def test_max():
    tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25, 5, 15, 35, 45, 55, 1000, -200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 60000, 7000]
    for v in values:
        tree.insert(v)
    assert tree.max() == max(values)
    
def test_min():
    tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25, 5, 15, 35, 45, 55, 1000, -200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 60000, 7000]
    for v in values:
        tree.insert(v)
    assert tree.min() == min(values)
    
def test_remove():
    tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25, 5, 15, 35, 45, 55, 1000, -200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 60000, 7000] * 2
    for v in values:
        tree.insert(v)
    tree.remove(30)
    values.remove(30)
    assert tree.validate_avl() == True
    assert tree.size() == len(values)
    assert tree.traverse("inorder") == sorted(values)
    tree.remove(30)
    values.remove(30)
    assert tree.validate_avl() == True
    assert tree.size() == len(values)
    assert tree.traverse("inorder") == sorted(values)
    
def test_search():
    tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25, 5, 15, 35, 45, 55, 1000, -200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 60000, 7000] * 2
    for v in values:
        tree.insert(v)
    for v in values:
        assert tree.search(v) == True
    assert tree.search(100) == False
    assert tree.search(10000) == False
    assert tree.search(-10000) == False
    
def test_copy():
    tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25, 5, 15, 35, 45, 55, 1000, -200, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 60000, 7000] * 2
    for v in values:
        tree.insert(v)
    copy_tree = copy.copy(tree)
    assert copy_tree.validate_avl() == True
    assert copy_tree.size() == tree.size()
    assert copy_tree.traverse("inorder") == tree.traverse("inorder")
    tree.remove(30)
    assert copy_tree.size() != tree.size()