class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.x = 0
        self.y = 0
        self.cx = 0
        self.cy = 0

def build_tree_postorder(nodes):
    if not nodes: return None
    val = nodes.pop()
    if val == '#': return None
    node = Node(int(val))
    node.right = build_tree_postorder(nodes)
    node.left = build_tree_postorder(nodes)
    return node

def get_butterfly_tree_string(root):
    if not root: return "Дерево порожнє."

    root.x = 0
    root.y = 0

    def process_subtree(node, is_left_side):
        if not node: return

        def assign_x(n, depth):
            if not n: return
            n.x = -depth if is_left_side else depth
            assign_x(n.left, depth + 1)
            assign_x(n.right, depth + 1)

        assign_x(node, 1)

        inorder_list = []
        def get_inorder(n):
            if not n: return
            get_inorder(n.left)
            inorder_list.append(n)
            get_inorder(n.right)

        get_inorder(node)

        root_idx = inorder_list.index(node)
        for i, n in enumerate(inorder_list):
            n.y = i - root_idx

    process_subtree(root.left, is_left_side=True)
    process_subtree(root.right, is_left_side=False)

    all_nodes = []
    def collect(n):
        if not n: return
        all_nodes.append(n)
        collect(n.left)
        collect(n.right)
    collect(root)

    min_x = min(n.x for n in all_nodes)
    max_x = max(n.x for n in all_nodes)
    min_y = min(n.y for n in all_nodes)
    max_y = max(n.y for n in all_nodes)

    X_SPACING = 6
    Y_SPACING = 2

    for n in all_nodes:
        n.cx = (n.x - min_x) * X_SPACING
        n.cy = (n.y - min_y) * Y_SPACING

    width = (max_x - min_x) * X_SPACING + 10
    height = (max_y - min_y) * Y_SPACING + 1
    canvas = [[' ' for _ in range(width)] for _ in range(height)]

    for n in all_nodes:
        val_str = str(n.value)
        for i, char in enumerate(val_str):
            if n.cx + i < width:
                canvas[n.cy][n.cx + i] = char

        for child in (n.left, n.right):
            if child:
                if n.cy == child.cy:
                    left_n = n if n.cx < child.cx else child
                    right_n = child if n.cx < child.cx else n
                    for ix in range(left_n.cx + len(str(left_n.value)) + 1, right_n.cx):
                        canvas[n.cy][ix] = '-'
                else:
                    mid_x = (n.cx + child.cx) // 2
                    mid_y = (n.cy + child.cy) // 2
                    
                    dx = child.cx - n.cx
                    dy = child.cy - n.cy
                    
                    if dx * dy > 0:
                        canvas[mid_y][mid_x] = '\\'
                    else:
                        canvas[mid_y][mid_x] = '/'

    result = []
    for row in canvas:
        line = "".join(row).rstrip()
        if line:
            result.append(line)
    return "\n".join(result)

def process_tree_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
        if not content:
            return None 
            
        print(f"Зчитано Post-order з файлу: {content}\n")
        nodes_list = content.split()
        tree_root = build_tree_postorder(nodes_list)
        print(get_butterfly_tree_string(tree_root))
        print("\n" + "="*60 + "\n")
        
        return tree_root
    except FileNotFoundError:
        return None