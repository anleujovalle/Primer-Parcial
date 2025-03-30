import matplotlib
matplotlib.use('TkAgg')  # O intenta 'Agg' si sigue sin funcionar
import matplotlib.pyplot as plt
import networkx as nx

def draw_moore_machine():
    G = nx.DiGraph()

    # Estados de la máquina de Moore (Decodificación de datos)
    states = ["WAIT", "RECEIVE", "VERIFY", "DISPLAY"]
    transitions = [
        ("WAIT", "RECEIVE", "Start Bit Received"),
        ("RECEIVE", "RECEIVE", "Clock Pulse/Next Bit"),
        ("RECEIVE", "VERIFY", "Last Bit Received"),
        ("VERIFY", "DISPLAY", "Data Verified"),
        ("DISPLAY", "WAIT", "Timeout/Reset"),
    ]

    # Crear el grafo de estados
    for state in states:
        G.add_node(state, shape='circle')

    for src, dst, label in transitions:
        G.add_edge(src, dst, label=label)

    # Dibujar la máquina de estados de Moore
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=24)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgreen", edge_color="black", font_size=10, font_weight="bold")
    edge_labels = {(src, dst): label for src, dst, label in transitions}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)
    plt.title("Máquina de Moore - Decodificación de Datos")
    plt.show()
