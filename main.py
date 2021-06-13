import math


class Node:
    def __init__(self, sequence=None):
        self.sequence = sequence

        self.left_child_id = None
        self.right_child_id = None
        self.tag = 0
        self.S = {}

    def add_edge(self, child_id):
        if self.left_child_id is None:
            self.left_child_id = child_id
        else:  # it is assumed that the tree is binary
            self.right_child_id = child_id


def main():
    number_of_nodes = int(input())
    node_ids = []
    for i in range(number_of_nodes):
        node_ids.append(i)

    edges = []
    for i in range(number_of_nodes - 1):
        edge = input().split(" ")
        edges.append([int(edge[0]), int(edge[1])])

    number_of_leaves = int(input())
    leaves = {}
    for i in range(number_of_leaves):
        leaf = input().split(" ")
        leaves[int(leaf[0])] = leaf[1]

    create_tree(node_ids, edges, leaves)


def create_tree(node_ids, edges, leaves):
    global tree
    # creating leaf nodes
    for leaf_id in leaves.keys():
        new_node = Node(sequence=leaves.get(leaf_id))
        node_ids.remove(leaf_id)
        tree[leaf_id] = new_node

    # creating other nodes
    for node_id in node_ids:
        new_node = Node()
        tree[node_id] = new_node

    # adding edges
    for edge in edges:
        parent_id = min(edge)
        child_id = max(edge)  # we assume that the upper node in tree has lower node_id
        tree.get(parent_id).add_edge(child_id)


tree = {}
if __name__ == '__main__':
    main()
