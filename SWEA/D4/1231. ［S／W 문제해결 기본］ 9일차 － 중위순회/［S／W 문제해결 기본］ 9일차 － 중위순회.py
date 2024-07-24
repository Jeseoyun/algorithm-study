class TreeNode:
    def __init__(self, num, value=None):
        self.left = None
        self.right = None
        self.num = num
        self.value = value
 
 
def make_tree(input_relation):
    tree = {}
     
    for parent, (value, children) in input_relation.items():
        if parent not in tree:
            tree[parent] = TreeNode(num=parent, value=value)
             
        if not tree[parent].value:
            tree[parent].value = value
         
        if len(children) > 0:  # 자식 노드가 1개 이상 -> left child에 삽입
            left_child = children[0]
            if left_child not in tree:
                tree[left_child] = TreeNode(num=left_child)
            tree[parent].left = tree[left_child]
             
        if len(children) > 1:  # 자식 노드가 2개 존재할 때 -> right child에 삽입
            right_child = children[1]
            if right_child not in tree:
                tree[right_child] = TreeNode(num=right_child)
            tree[parent].right = tree[right_child]
    return tree
 
 
def inorder_traversal(node):
    if not node:
        return []
    left = inorder_traversal(node.left)
    current = [node.value]
    right = inorder_traversal(node.right)
     
    return left + current + right
 
 
def main():
    for test_case in range(10):
        N = int(input())
 
        input_relation = {}
         
        # 입력값 받아옴
        for _ in range(N):
            node_num, node_value, *linked_node = input().split()
            input_relation[node_num] = (node_value, linked_node)
         
        tree = make_tree(input_relation)
        result = inorder_traversal(tree["1"])  # "1"이 루트라 가정
         
        print(f"#{test_case+1} {''.join(result)}")
 
 
if __name__ == "__main__":
    main()