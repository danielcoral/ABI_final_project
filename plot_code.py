# Importing the interaction dataset:
sig_edges = open('sig_edges.txt', 'r')

# Building the nextwork as a dictionary:
network = {}
for line in sig_edges:
    entry = line.split(' ')
    vertex1 = entry[0]
    vertex2 = entry[1]
    edge_score = int(entry[2])
    if not vertex1 in network:
        network[vertex1] = [vertex2, edge_score]
    else:
        network[vertex1].append([vertex2, edge_score])

# Categorizing nodes based on node degree:
large_nodes = list()
small_nodes = list()
for node in network:
    if len(network[node]) > 100:
        large_nodes.append(node)
    else:
        small_nodes.append(node)
        
# Importing protein domains dataset:
domains = open('filtered_domains.txt', 'r')

# Counting the number of domains:
domain_count = {}
for protein in domains:
    protein_name = protein.rstrip() 
    domain_count[protein_name] = domain_count.get(protein_name, 0) + 1
    
# Assigning the counts found to each category of nodes:
large_nodes_result = []
small_nodes_result = []
for protein, n_domains in domain_count.items():
    if protein in large_nodes:
        large_nodes_result.append(n_domains)
    elif protein in small_nodes:
        small_nodes_result.append(n_domains)
    else:
        pass
result = [large_nodes_result, small_nodes_result]

# Plot of the results
import matplotlib.pyplot as plt
plt.boxplot(result, labels=[">100", "<=100"])
plt.title("Project plot")
plt.xlabel("Node degree")
plt.ylabel("Number of domains")
plt.savefig("protein_domains_vs_string_degree.png")
