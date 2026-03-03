from collections import deque
from typing import List, Optional

class TreeNode:
    """
    Create TreeNode class
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)


def bfs_tree(root: Optional[TreeNode])-> List[TreeNode]:
    """ 
    Takes in a TreeNode and returns a list of all nodes in the tree, traversed in order
    """
    if not root:
    	return []
    q = deque()
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


# ------- Viz and testing --------

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

if __name__ == "__main__":
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.right.right = TreeNode(6)

	print("--- Tree Structure ---")
	draw_tree(root)

	print("\n--- bfs_tree Traversal Result ---")
	print(bfs_tree(root))
