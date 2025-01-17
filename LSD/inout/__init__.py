import networkx as nx


def load(path, f="edgelist"):
    if path == "-":
        from sys import stdin
        path = stdin.buffer
    g = None
    if f == "edgelist":
        g = load_edgelist(path)
    elif f == "adjlist":
        g = load_adjlist(path)
    elif f == "gexf":
        g = load_gexf(path)
    elif f == "gml":
        g = load_gml(path)
    elif f == "gpickle":
        g = load_gpickle(path)
    elif f == "graph6":
        g = load_graph6(path)
    elif f == "graphml":
        g = load_graphml(path)
    elif f == "leda":
        g = load_leda(path)
    elif f == "pajek":
        g = load_pajek(path)
    elif f == "sparse6":
        g = load_sparse6(path)
    elif f == "yaml":
        g = load_yaml(path)
    return g


def load_edgelist(path):
    return nx.read_edgelist(path, create_using=nx.DiGraph())


def load_adjlist(path):
    return nx.read_adjlist(path, create_using=nx.DiGraph())


def load_gexf(path):
    return nx.read_gexf(path, create_using=nx.DiGraph())


def load_gml(path):
    return nx.read_gml


def load_gpickle(path):
    return nx.read_gpickle


def load_graph6(path):
    return nx.read_graph6


def load_graphml(path):
    return nx.read_graphml


def load_leda(path):
    return nx.read_leda


def load_pajek(path):
    return nx.read_pajek


def load_sparse6(path):
    return nx.read_sparse6


def load_yaml(path):
    return nx.read_yaml
