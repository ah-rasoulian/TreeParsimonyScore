def main():
    number_of_nodes = int(input())
    edges = []
    for i in range(number_of_nodes - 1):
        edge = input().split(" ")
        edges.append([int(edge[0]), int(edge[1])])

    number_of_leaves = int(input())
    leaves = {}
    for i in range(number_of_leaves):
        leaf = input().split(" ")
        leaves[int(leaf[0])] = leaf[1]


if __name__ == '__main__':
    main()
