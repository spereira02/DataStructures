from collections import deque

def BFS(root):
    q: list = deque()
    q.append(root)
    traversal: list = []
    #to measure depth of tree init depth:int = 0
    while q:

        for _ in range(len(q)):
            node = q.popleft()
            traversal.append(node)
            #optionally print node or store it in a visited array/set, whatever

            if node.left:q.append(node.left)
            
            if node.right: q.append(node.right)
        #optionally do depth += 1
    return traversal
    #or return depth





class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)

# to test the algo create a tree and its viz

def draw_tree(node, level=0, is_left=None)->None:
    if node is None:
        return
    
    draw_tree(node.right, level + 1, False)
    
    indent = "    " * level
    if is_left is None:
        branch = "───" 
    elif is_left:
        branch = "└── "
    else:
        branch = "┌── " 
        
    print(f"{indent}{branch}{node.val}")
    draw_tree(node.left, level + 1, True)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("--- Tree Structure ---")
draw_tree(root)

print("\n--- BFS Traversal Result ---")
result = BFS(root)
print(result)