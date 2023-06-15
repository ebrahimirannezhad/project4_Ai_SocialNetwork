import random
import matplotlib.pyplot as plt

def generate_random_network(b, height, k, alpha):
    network = {}
    nodes = [0]
    for level in range(1, height + 1):
        new_nodes = []
        for parent in nodes:
            for child in range(b):
                node = (parent * b) + child + 1
                new_nodes.append(node)
                network[node] = []
                prob = pow(b, -alpha * (height - level))
                for neighbor in random.sample(nodes, min(k, len(nodes))):
                    network[node].append((neighbor, prob))
        nodes = new_nodes
    return network

def decentralized_search(network, start_node, target_node):
    current_node = start_node
    while True:
        if current_node not in network:
            return False
        neighbors = network[current_node]
        neighbors.sort(key=lambda x: h(x[0], target_node))
        closest_node = neighbors[0][0]
        if closest_node == target_node:
            return True
        if h(current_node, target_node) > h(closest_node, target_node):
            current_node = closest_node
        else:
            return False


def average_path_length(network, pairs):
    total_length = 0
    for pair in pairs:
        start_node, target_node = pair
        if decentralized_search(network, start_node, target_node):
            total_length += h(start_node, target_node)
    return total_length / len(pairs)

def calculate_success_probability(network, pairs):
    success_count = 0
    for pair in pairs:
        start_node, target_node = pair
        if decentralized_search(network, start_node, target_node):
            success_count += 1
    return success_count / len(pairs)

def h(v, w):
    return calculate_height(w) - calculate_height(lowest_common_ancestor(v, w))

def calculate_height(node):
    return (node - 1).bit_length()

def lowest_common_ancestor(v, w):
    while v != w:
        if v > w:
            v = parent(v)
        else:
            w = parent(w)
    return v

def parent(node):
    return (node - 1) // 2

# Parameters
b = 2
height = 10
k = 5
alphas = [0.1, 0.2, 0.3, 0.4, 0.5, 1, 2, 5, 10]
sample_size = 1000

average_lengths = []
success_probabilities = []

for alpha in alphas:
    network = generate_random_network(b, height, k, alpha)
    pairs = [(random.randint(0, b**height - 1), random.randint(0, b**height - 1)) for _ in range(sample_size)]
    average_length = average_path_length(network, pairs)
    success_probability = calculate_success_probability(network, pairs)
    average_lengths.append(average_length)
    success_probabilities.append(success_probability)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(alphas, average_lengths, marker='o')
plt.xlabel('Alpha')
plt.ylabel('Average Path Length')
plt.title('Average Path Length vs. Alpha')

plt.subplot(1, 2, 2)
plt.plot(alphas, success_probabilities, marker='o')
plt.xlabel('Alpha')
plt.ylabel('Success Probability')
plt.title('Success Probability vs. Alpha')

plt.tight_layout()
plt.show()
