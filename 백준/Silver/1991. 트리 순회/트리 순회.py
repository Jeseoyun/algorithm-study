def pre_order(graph, node):
    if node == '.':
        return ''
    
    left, right = graph[node]
    return node + pre_order(graph, left) + pre_order(graph, right)


def in_order(graph, node):
    if node == '.':
        return ''
    
    left, right = graph[node]
    return in_order(graph, left) + node + in_order(graph, right)


def post_order(graph, node):
    if node == '.':
        return ''
    
    left, right = graph[node]
    return post_order(graph, left) + post_order(graph, right) + node


def main():
    N = int(input())
    
    graph = dict()
    for _ in range(N):
        parent, left, right = input().split()
        graph[parent] = (left, right)
        
    root = 'A'
    print(pre_order(graph, root))
    print(in_order(graph, root))
    print(post_order(graph, root))
    
    
if __name__ == "__main__":
    main()