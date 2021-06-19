# Python program to demonstrate insert operation in binary search tree

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


def insert(root, data):
    if root is None:
        return Node(data)
    elif root.data == data:
        return root
    elif data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


# Given a non-empty binary
# search tree, return the node
# with minimum key value
# found in that tree. Note that the
# entire tree does not need to be searched


def min_value_node(node):
    current = node

    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current


def delete_node(root, data):
    # Base Case
    if root is None:
        return root

    # Recursive calls for ancestors of
    # node to be deleted
    if data < root.data:
        root.left = delete_node(root.left, data)
        return root

    elif data > root.data:
        root.right = delete_node(root.right, data)
        return root

    # We reach here when root is the node
    # to be deleted.

    # If root node is a leaf node

    if root.left is None and root.right is None:
        return None

    # If one of the children is empty

    if root.left is None:
        temp = root.right
        # root = None
        return temp

    elif root.right is None:
        temp = root.left
        # root = None
        return temp

    # If both children exist

    succParent = root

    # Find Successor

    succ = root.right

    while succ.left is not None:
        succParent = succ
        succ = succ.left

    # Delete successor.Since successor
    # is always left child of its parent
    # we can safely make successor's right
    # right child as left of its parent.
    # If there is no succ, then assign
    # succ->right to succParent->right
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    # Copy Successor Data to root

    root.data = succ.data

    return root


# A utility function to search a given key in BST
def search(root, data):
    # Base Cases: root is null or key is present at root
    if root is None or root.data == data:
        return root

    # Key is greater than root's key
    if root.data < data:
        return search(root.right, data)

    # Key is smaller than root's key
    return search(root.left, data)


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def max_depth(node):
    if node is None:
        return 0

    else:

        # Compute the depth of each subtree
        lDepth = max_depth(node.left)
        rDepth = max_depth(node.right)

        # Use the larger one
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1


def main():
    # Driver program to test the above functions
    # Let us create the following BST
    #    50
    #  /     \
    # 30     70
    #  / \ / \
    # 20 40 60 80

    root = Node(50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    # Print inorder traversal of the BST
    inorder(root)

    print(f"Height of tree is {max_depth(root)}")

    print("\nDelete 20")
    root = delete_node(root, 20)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDelete 30")
    root = delete_node(root, 30)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDelete 50")
    root = delete_node(root, 50)
    print("Inorder traversal of the modified tree")
    inorder(root)


if __name__ == "__main__":
    main()
