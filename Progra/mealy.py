import matplotlib
matplotlib.use('TkAgg')  # O intenta 'Agg' si sigue sin funcionar
import networkx as nx
import matplotlib.pyplot as plt
def draw_mealy_machine():
    G = nx.DiGraph()

    # Estados de la máquina de Mealy (Codificación de datos)
    states = ["IDLE", "LOAD", "SHIFT", "STOP"]
    transitions = [
        ("IDLE", "LOAD", "Start/Load Data"),
        ("LOAD", "SHIFT", "Clock Pulse/Send Bit"),
        ("SHIFT", "SHIFT", "Clock Pulse/Next Bit"),
        ("SHIFT", "STOP", "Last Bit Sent"),
        ("STOP", "IDLE", "Reset"),
    ]

    # Crear el grafo de estados
    for state in states:
        G.add_node(state, shape='circle')

    for src, dst, label in transitions:
        G.add_edge(src, dst, label=label)

    # Dibujar la máquina de estados de Mealy
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="black", font_size=10, font_weight="bold")
    edge_labels = {(src, dst): label for src, dst, label in transitions}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)
    plt.title("Máquina de Mealy - Codificación de Datos")
    plt.show()
