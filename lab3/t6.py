def build_postorder(inorder, preorder):
    index_map = {value: i for i, value in enumerate(inorder)}  
    postorder_result = []
 
    def construct(in_left, in_right):
        if in_left > in_right:
            return
        root_value = preorder.pop(0)  
        root_index = index_map[root_value]  
        construct(in_left, root_index - 1)  
        construct(root_index + 1, in_right) 
        postorder_result.append(root_value)  
 
    construct(0, len(inorder) - 1)
    return postorder_result
 
 
n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))
 
if len(inorder) != n or len(preorder) != n:
    print("Error: Number of elements does not match n")
else:
    result = build_postorder(inorder, preorder)
    print(" ".join(map(str, result)))