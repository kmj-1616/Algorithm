import sys
input = sys.stdin.readline

n = int(input())
graph = {}

for _ in range(n):
    parent, left, right = list(input().split())
    graph[parent] = [left, right]

# 전위순회
global preorder_value
preorder_value = ''

def preorder(node):
    global preorder_value
    if node != '.':  
        preorder_value += node
        preorder(graph[node][0])
        preorder(graph[node][1])

# 중위순회
global inorder_value
inorder_value = ''

def inorder(node):
    global inorder_value
    if node != '.':  
        inorder(graph[node][0])
        inorder_value += node
        inorder(graph[node][1])

# 후위순회
global postorder_value
postorder_value = ''

def postorder(node):
    global postorder_value
    if node != '.':  
        postorder(graph[node][0])
        postorder(graph[node][1])
        postorder_value += node
        
preorder('A')
inorder('A')
postorder('A')

print(preorder_value)
print(inorder_value)
print(postorder_value)