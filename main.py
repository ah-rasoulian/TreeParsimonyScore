import math


class Node:
    def __init__(self, number_of_chars, sequence=None):
        self.sequence = sequence

        self.left_child_id = None
        self.right_child_id = None
        self.tag = 0
        self.S = {}  # for each char position, for each char, its value is parsimony score until current node for that character
        for i in range(number_of_chars):
            self.S[i] = {'A': math.inf, 'C': math.inf, 'G': math.inf, 'T': math.inf}

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
    number_of_chars = 0

    for i in range(number_of_leaves):
        leaf = input().split(" ")
        if i == 0:
            number_of_chars = len(leaf[1])
        leaves[int(leaf[0])] = leaf[1].upper()

    create_tree(node_ids, edges, leaves, number_of_chars)

    minimum_parsimony = 0
    for position in range(number_of_chars):
        minimum_parsimony += small_parsimony(position)

    print(minimum_parsimony)


def create_tree(node_ids, edges, leaves, number_of_chars):
    global tree
    # creating leaf nodes
    for leaf_id in leaves.keys():
        new_node = Node(number_of_chars=number_of_chars, sequence=leaves.get(leaf_id))
        node_ids.remove(leaf_id)
        tree[leaf_id] = new_node

    # creating other nodes
    for node_id in node_ids:
        new_node = Node(number_of_chars=number_of_chars)
        tree[node_id] = new_node

    # adding edges
    for edge in edges:
        parent_id = min(edge)
        child_id = max(edge)  # we assume that the upper node in tree has lower node_id
        tree.get(parent_id).add_edge(child_id)


def small_parsimony(char_position):
    global tree
    for node in tree.values():
        node: Node
        node.tag = 0
        if node.sequence is not None:  # if node is leaf
            node.tag = 1
            for char in CHARS:
                if node.sequence[char_position] == char:
                    node.S.get(char_position)[char] = 0
    ripe_nodes_ids = get_ripe_nodes()
    while len(ripe_nodes_ids) > 0:
        node = tree.get(ripe_nodes_ids[0])
        node.tag = 1
        for char in CHARS:
            left_min = math.inf
            daughter_node = tree.get(node.left_child_id)
            daughter_node: Node
            for char2 in CHARS:
                possible_cost = daughter_node.S.get(char_position).get(char2) + mutation_cost(char, char2)
                if possible_cost < left_min:
                    left_min = possible_cost

            right_min = math.inf
            son_node = tree.get(node.right_child_id)
            son_node: Node
            for char2 in CHARS:
                possible_cost = son_node.S.get(char_position).get(char2) + mutation_cost(char, char2)
                if possible_cost < right_min:
                    right_min = possible_cost

            node.S.get(char_position)[char] = left_min + right_min
        ripe_nodes_ids = get_ripe_nodes()

    root_node = tree.get(0)
    root_node: Node
    minimum_parsimony_in_position = min(root_node.S.get(char_position).values())
    return minimum_parsimony_in_position


def get_ripe_nodes():
    global tree
    ripe_nodes = []
    for node_id, node in tree.items():
        node: Node
        if node.tag == 0 and tree.get(node.left_child_id).tag == 1 and tree.get(node.right_child_id).tag == 1:
            ripe_nodes.append(node_id)
    return ripe_nodes

def mutation_cost(char1, char2):
    if char1 == char2:
        return 0
    else:
        return 1

tree = {}
CHARS = ['A', 'C', 'G', 'T']

if __name__ == '__main__':
    main()
