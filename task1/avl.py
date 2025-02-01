from typing import Optional, Tuple, List

class AVLNode:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1
        self.size: int = 1  # Количество элементов в поддереве
        self.count: int = 1  # Количество повторяемых ключей в узле
    
    def __repr__(self) -> str:
        return f"AVLNode(key={self.key}, height={self.height}, size={self.size}, count={self.count})"
    
    def __str__(self) -> str:
        return str(self.key)

class AVLTree:
    def __init__(self) -> None:
        self.root: Optional[AVLNode] = None

    def _height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _size(self, node: Optional[AVLNode]) -> int:
        return (node.size + node.count - 1) if node else 0 # Учитываем дубликаты
    
    def _update(self, node: Optional[AVLNode]) -> None:
        if node:
            # Рекурсивно обновляем высоту
            node.height = max(self._height(node.left), self._height(node.right)) + 1 
            # Рекурсивно обновляем количество элементов в поддереве
            node.size = self._size(node.left) + self._size(node.right) + 1 
            
    def _rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        if not x:
            return y
        T2 = x.right
        x.right = y
        y.left = T2
        self._update(y)
        self._update(x)
        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        if not y:
            return x
        T2 = y.left
        y.left = x
        x.right = T2
        self._update(x)
        self._update(y)
        return y

    def _balance_factor(self, node: Optional[AVLNode]) -> int:
        return self._height(node.left) - self._height(node.right) if node else 0
    
    def _balance(self, node: AVLNode) -> AVLNode:
        self._update(node)
        if self._balance_factor(node) > 1:
            if node.left and self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left) 
            return self._rotate_right(node)
        if self._balance_factor(node) < -1:
            if node.right and self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _insert(self, node: Optional[AVLNode], key: int) -> AVLNode:
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            node.count += 1 # Увеличиваем количество дубликатов
            return node
        return self._balance(node)

    def insert(self, key: int) -> None:
        """Вставка ключа в дерево"""
        if key <= 0:
            raise ValueError("Key must be greater than 0")
        self.root = self._insert(self.root, key)

    def _find_min(self, node: AVLNode) -> AVLNode:
        while node.left:
            node = node.left
        return node

    def _remove(self, node: Optional[AVLNode], key: int) -> Optional[AVLNode]:
        if not node:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.count > 1:
                node.count -= 1 # Если есть дубликаты, уменьшаем количество
                return node
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Если у узла два потомка, находим минимальный элемент в правом поддереве
            # и заменяем удаляемый узел на него 
            # (после чего удаляем минимальный элемент из правого поддерева) 
            temp = self._find_min(node.right)
            node.key = temp.key
            node.count = temp.count
            temp.count = 1 
            node.right = self._remove(node.right, temp.key)
        return self._balance(node)

    def remove(self, key: int) -> None:
        """Удаление ключа из дерева"""
        self.root = self._remove(self.root, key)

    def search(self, key: int) -> bool:
        """Поиск ключа в дереве"""
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def _traverse(self, node: Optional[AVLNode], result: List[int], order: str) -> None:
        if node:
            if order == "preorder":
                result += [node.key] * (node.count)
            self._traverse(node.left, result, order)
            if order == "inorder":
                result += [node.key] * (node.count)
            self._traverse(node.right, result, order)
            if order == "postorder":
                result += [node.key] * (node.count)

    def traverse(self, order: str = "inorder") -> List[int]:
        """Обход дерева: inorder, preorder, postorder"""
        result: List[int] = []
        self._traverse(self.root, result, order)
        return result
    
    def _validate_avl(self, node: Optional[AVLNode], min_key=float('-inf'), max_key=float('inf')) -> bool:
        if not node:
            # Пустое поддерево является AVL
            return True 
        if not (min_key < node.key < max_key):
            # Нарушение свойства BST
            # print(f"Node key {node.key} is not in the range ({min_key}, {max_key})")
            return False 
        bf = self._balance_factor(node)
        if abs(bf) > 1:
            # Нарушение балансировки AVL
            # print(f"Node key {node.key} has balance factor {bf}")
            return False 
        if node.size != (self._size(node.left) + self._size(node.right) + 1):
            # Нарушение свойства size в данной реализации AVL
            # print(f"Node key {node.key} has invalid size")
            return False 
        return self._validate_avl(node.left, min_key, node.key) and self._validate_avl(node.right, node.key, max_key)
        
    def validate_avl(self) -> bool:
        """Проверка на то, что дерево является AVL"""
        return self._validate_avl(self.root)

    def _split(self, node: Optional[AVLNode], key: int) -> Tuple[Optional[AVLNode], Optional[AVLNode]]:
        if not node:
            return None, None
        # Рекурсивно разделяем левое и правое поддеревья 
        # Элементы, меньшие или равные key, попадают в левое поддерево; остальные -- в правое
        if key < node.key:
            left, node.left = self._split(node.left, key)
            node = self._balance(node)
            return left, node
        else:
            node.right, right = self._split(node.right, key)
            node = self._balance(node)
            return node, right

    def split(self, key: int) -> Tuple['AVLTree', 'AVLTree']:
        """Разделение дерева на два по ключу; левое дерево содержит все ключи <= key, правое -- > key"""
        left, right = self._split(self.root, key)
        left_tree, right_tree = AVLTree(), AVLTree()
        left_tree.root, right_tree.root = left, right
        left_tree._rebalance_tree()
        right_tree._rebalance_tree()
        return left_tree, right_tree

    def _rebalance_tree(self):  
        def _rebalance(node: Optional[AVLNode]) -> Optional[AVLNode]:
            if not node:
                return None
            node.left = _rebalance(node.left)
            node.right = _rebalance(node.right)
            return self._balance(node)
        self.root = _rebalance(self.root)

    def merge(self, other: 'AVLTree') -> None:
        """Слияние двух AVL-деревьев"""
        for key in other.traverse():
            self.insert(key)
    
    def height(self) -> int:
        """Высота дерева"""
        return self._height(self.root)
    
    def size(self) -> int:
        """Количество элементов в дереве"""
        return self._size(self.root)
    
    def __len__(self) -> int:
        return self.size()
    
    def max(self) -> int:
        """Максимальный ключ в дереве"""
        if not self.root:
            raise ValueError("The AVL tree is empty")
        node = self.root
        while node.right:
            node = node.right
        return node.key
    
    def min(self) -> int:
        """Минимальный ключ в дереве"""
        if not self.root:
            raise ValueError("The AVL tree is empty")
        node = self.root
        while node.left:
            node = node.left
        return node.key
    
    def _copy(self, node: Optional[AVLNode]) -> Optional[AVLNode]:
        if not node:
            return None
        new_node = AVLNode(node.key)
        new_node.height = node.height
        new_node.size = node.size
        new_node.count = node.count
        new_node.left = self._copy(node.left)
        new_node.right = self._copy(node.right)
        return new_node
        
    def __copy__(self) -> 'AVLTree':
        new_tree = AVLTree()
        new_tree.root = self._copy(self.root)
        return new_tree
