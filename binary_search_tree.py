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

    # If the key to be deleted is smaller than the root's key then it lies in  left subtree
    if data < root.data:
        root.left = delete_node(root.left, data)

    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif data > root.data:
        root.right = delete_node(root.right, data)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = min_value_node(root.right)

        # Copy the inorder successor's
        # content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.key)

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

# Print inoder traversal of the BST
inorder(root)

print("Height of tree is %d" % (max_depth(root)))

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
