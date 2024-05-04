import matplotlib.pyplot as plt
import networkx as nx

def PlotGraph(G):
    """
    This function plots the given graph G using a circular layout.
    Nodes are labeled, and edge weights are displayed.
    """
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def PlotShortestPaths(G):
    """
    This function displays the shortest paths from node '4' to all other nodes in the graph G using Dijkstra's algorithm.
    Paths are highlighted in red. The process repeats for nodes 0 to 3, and each path is shown in a separate plot.
    """
    for j in range(4):
        node = '{}'.format(j)
        if G.has_node(node) and nx.has_path(G, '4', node):
            shortest_path = nx.dijkstra_path(G, '4', node)
            shortest_path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]

            fig, ax = plt.subplots()
            pos = nx.circular_layout(G)
            nx.draw(G, pos=pos, ax=ax, with_labels=True)
            nx.draw_networkx_edges(G, pos=pos, ax=ax, edgelist=shortest_path_edges, edge_color='r', width=3)
            edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
            nx.draw_networkx_edge_labels(G, pos=pos, ax=ax, edge_labels=edge_labels)
            plt.show()

def main():
    """
    Main function to create a directed graph, add edges with weights, and visualize the graph.
    After initial visualizations, node '2' is removed, and the graph and shortest paths are visualized again without node '2'.
    """
    G = nx.DiGraph()
    G.add_edge('0', '1', weight=5)
    G.add_edge('0', '2', weight=3)
    G.add_edge('0', '4', weight=2)
    G.add_edge('1', '2', weight=2)
    G.add_edge('1', '3', weight=6)
    G.add_edge('2', '1', weight=1)
    G.add_edge('2', '3', weight=2)
    G.add_edge('4', '3', weight=4)
    G.add_edge('4', '2', weight=10)
    G.add_edge('4', '1', weight=6)

    PlotGraph(G)
    PlotShortestPaths(G)
    
    G.remove_node('2')
    PlotGraph(G)
    PlotShortestPaths(G)

main()
