
import ipycytoscape as ipycytoscape
import rdflib.graph
from rich.table import Table


def parse_graph(turtle_contents:str) -> rdflib.graph.Graph:
    g = rdflib.graph.Graph()
    g.parse(data=turtle_contents, format="turtle")
    return g


def print_sparql_results(graph:rdflib.graph.Graph, query:str) -> list:
    from rich.jupyter import print
    table = Table(show_header=True, header_style="bold magenta")
    results = list(graph.query(query).bindings)
    for name in results[0].keys():
        table.add_column(name)
    for res in results:
        table.add_row(*res.values())
    print(table)


def visualize_graph(graph:rdflib.graph.Graph) -> ipycytoscape.CytoscapeWidget:
    cytoscape_obj = ipycytoscape.CytoscapeWidget()
    from rdflib.extras.external_graph_libs import rdflib_to_networkx_digraph
    nx = rdflib_to_networkx_digraph(graph)
    cytoscape_obj.graph.add_graph_from_networkx(nx)
    return cytoscape_obj