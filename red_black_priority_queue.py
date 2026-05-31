class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.color = 1
        self.parent = None
        self.left = None
        self.right = None

class RedBlackPriorityQueue:
    def __init__(self):
        self.TNULL = Node(None, None)
        self.TNULL.color = 0 
        self.root = self.TNULL

    def peek(self):
        if self.root == self.TNULL:
            return None
        highest = self._minimum(self.root)
        return highest.value, highest.priority

    def insert(self, value, priority):
        node = Node(value, priority)
        node.parent = None
        node.value = value
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.priority >= x.priority:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.priority >= y.priority:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self._fix_insert(node)

    def extract_max(self):
        if self.root == self.TNULL:
            return None
        
        node = self._minimum(self.root)
        value_to_return = node.value
        priority_to_return = node.priority
        
        self._delete_node_helper(node)
        return value_to_return, priority_to_return


    def _minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def _rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _delete_node_helper(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.TNULL:
            x = node.right
            self._rb_transplant(node, node.right)
        elif node.right == self.TNULL:
            x = node.left
            self._rb_transplant(node, node.left)
        else:
            y = self._minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._rb_transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self._rb_transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == 0:
            self._fix_delete(x)

    def _fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self._left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self._right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self._right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self._left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def display(self):
        elements = []
        self._inorder_helper(self.root, elements)
        print("Черга (від найвищого пріоритету до найнижчого):", elements)

    def _inorder_helper(self, node, elements):
        if node != self.TNULL:
            self._inorder_helper(node.left, elements)
            elements.append((node.value, node.priority))
            self._inorder_helper(node.right, elements)