import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

# Read the CSV file
df = pd.read_csv("Airport_Data.csv")

# Create a network graph
G = nx.Graph()

# Print the first few rows and columns to verify the data
print("DataFrame columns:", df.columns.tolist())
print("\nFirst few rows of data:")
print(df.head())

# Add nodes and edges to the graph
for _, row in df.iterrows():
    origin = f"{row['Origin_airport']}\n({row['Origin_city']})"
    dest = f"{row['Destination_airport']}\n({row['Destination_city']})"
    
    # Add nodes
    G.add_node(origin)
    G.add_node(dest)
    
    # Add edge
    G.add_edge(origin, dest)

# Create the visualization
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, k=2, iterations=50)

# Draw the network
nx.draw(G, pos,
        node_color='lightblue',
        node_size=500,
        font_size=8,
        font_weight='bold',
        with_labels=True,
        edge_color='gray',
        alpha=0.7)

# Add title
plt.title("Airport Connection Network", fontsize=16, pad=20)

# Save the plot
plt.savefig("airport_network.png", bbox_inches='tight', dpi=300)
plt.close()

# Print some basic statistics
print("\nNetwork Statistics:")
print(f"Number of Airports: {G.number_of_nodes()}")
print(f"Number of Routes: {G.number_of_edges()}")

# Print top connected airports
print("\nTop 10 Most Connected Airports:")
degrees = dict(G.degree())
sorted_airports = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:10]
for airport, connections in sorted_airports:
    print(f"{airport}: {connections} connections")