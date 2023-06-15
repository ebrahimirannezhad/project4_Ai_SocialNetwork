import urllib.request
import gzip
import networkx as nx
import matplotlib.pyplot as plt

# Download the dataset
url = "https://snap.stanford.edu/data/bigdata/communities/com-friendster.ungraph.txt.gz"
dataset_path = "com-friendster.ungraph.txt.gz"

urllib.request.urlretrieve(url, dataset_path)

# Extract the dataset
with gzip.open(dataset_path, "rb") as file_in:
    with open("com-friendster.ungraph.txt", "wb") as file_out:
        file_out.write(file_in.read())

# Read the dataset and generate the graph
graph = nx.read_edgelist("com-friendster.ungraph.txt")


# Print some basic information about the graph
print("Number of nodes:", graph.number_of_nodes())
print("Number of edges:", graph.number_of_edges())

# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 39 :
# 39 Degree distribution
# Calculate the degree of each node
degrees = [graph.degree(node) for node in graph.nodes()]

# Plot the degree distribution
plt.hist(degrees, bins=30, edgecolor='black')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.show()

# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 40 :
# 40 Path length distribution
# Calculate the shortest path lengths between all pairs of nodes
path_lengths = dict(nx.all_pairs_shortest_path_length(graph))

# Flatten the path lengths dictionary
all_lengths = [length for source_lengths in path_lengths.values() for length in source_lengths.values()]

# Plot the path length distribution
plt.hist(all_lengths, bins=30, edgecolor='black')
plt.xlabel('Path Length')
plt.ylabel('Frequency')
plt.title('Path Length Distribution')
plt.show()


# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 41 :
# 41 WCC size distribution
# Find the weakly connected components
wcc_sizes = [len(wcc) for wcc in nx.weakly_connected_components(graph)]

# Plot the WCC size distribution
plt.hist(wcc_sizes, bins=30, edgecolor='black')
plt.xlabel('WCC Size')
plt.ylabel('Frequency')
plt.title('WCC Size Distribution')
plt.show()


# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 42 :
# 42 Clustering coefficient distribution
# Find the weakly connected components
clustering_coefficients = nx.clustering(graph)

# Plot the clustering coefficient distribution
plt.hist(list(clustering_coefficients.values()), bins=30, edgecolor='black')
plt.xlabel('Clustering Coefficient')
plt.ylabel('Frequency')
plt.title('Clustering Coefficient Distribution')
plt.show()


# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 43 :
# 43 k-core node size distribution
# Compute the k-core decomposition
k_cores = nx.core_number(graph)

# Count the frequency of each core size
core_sizes = list(k_cores.values())
core_size_counts = {core_size: core_sizes.count(core_size) for core_size in set(core_sizes)}

# Sort the core sizes
sorted_core_sizes = sorted(core_size_counts.keys())

# Plot the k-core size distribution
plt.bar(sorted_core_sizes, [core_size_counts[core_size] for core_size in sorted_core_sizes])
plt.xlabel('K-Core Size')
plt.ylabel('Frequency')
plt.title('K-Core Size Distribution')
plt.show()


# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 44 :
# 44 Average friends-of-friends distribution
# Compute the average friends-of-friends for each node
avg_friends_of_friends = {}
for node in graph.nodes():
    friends = set(graph.neighbors(node))
    friends_of_friends = set()
    for friend in friends:
        friends_of_friends.update(graph.neighbors(friend))
    friends_of_friends -= friends
    avg_friends_of_friends[node] = len(friends_of_friends) / len(friends) if len(friends) > 0 else 0

# Count the frequency of each average friends-of-friends value
avg_friends_of_friends_values = list(avg_friends_of_friends.values())
avg_friends_of_friends_counts = {value: avg_friends_of_friends_values.count(value) for value in set(avg_friends_of_friends_values)}

# Sort the average friends-of-friends values
sorted_avg_friends_of_friends = sorted(avg_friends_of_friends_counts.keys())

# Plot the average friends-of-friends distribution
plt.bar(sorted_avg_friends_of_friends, [avg_friends_of_friends_counts[value] for value in sorted_avg_friends_of_friends])
plt.xlabel('Average Friends-of-Friends')
plt.ylabel('Frequency')
plt.title('Average Friends-of-Friends Distribution')
plt.show()


# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 45 :
# 45 Average neighbour degree distribution
# Compute the average neighbour degree for each node
avg_neighbour_degree = {}
for node in graph.nodes():
    neighbours = list(graph.neighbors(node))
    neighbour_degrees = [graph.degree(neighbour) for neighbour in neighbours]
    avg_neighbour_degree[node] = sum(neighbour_degrees) / len(neighbour_degrees) if len(neighbour_degrees) > 0 else 0

# Count the frequency of each average neighbour degree value
avg_neighbour_degree_values = list(avg_neighbour_degree.values())
avg_neighbour_degree_counts = {value: avg_neighbour_degree_values.count(value) for value in set(avg_neighbour_degree_values)}

# Sort the average neighbour degree values
sorted_avg_neighbour_degree = sorted(avg_neighbour_degree_counts.keys())

# Plot the average neighbour degree distribution
plt.bar(sorted_avg_neighbour_degree, [avg_neighbour_degree_counts[value] for value in sorted_avg_neighbour_degree])
plt.xlabel('Average Neighbour Degree')
plt.ylabel('Frequency')
plt.title('Average Neighbour Degree Distribution')
plt.show()