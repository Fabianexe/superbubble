from LSD.hashed_list import HashedList
from math import inf

def check_pre(v, g, order):
    """Check if all predecessors have already been placed."""
    if order.index(v) > -2:
        return False
    for v2 in g.predecessors(v):
        if order.index(v2) == -2:
            return False
    return True


def toposort(g):
    """Do a topological ordering of the graph.
    It does a lineare version of a deep first search.
    The recusive version of the same algorithm would look like this::
    
        def toposort(g):
            order = Order(g.a, g.b)
            rec_call(g.a, order, g, lambda v: check_pre(v, g, order))
            return order
    
            
        def rec_call(v, order, g, check_predecessor):
            for child in g.successors(v):
                if check_predecessor(child):
                    order.add(child)
                    rec_call(child, order, g, check_predecessor)
    
    """
    order = HashedList()
    order.add_pseudo_revers(g.a, -1)
    order.add_pseudo_revers(g.b, inf)
    stack = [iter(g.successors(g.a))]
    while stack:
        children = stack[-1]
        try:
            child = next(children)
            if check_pre(child, g, order):
                order.append(child)
                stack.append(iter(g.successors(child)))
        except StopIteration:
            stack.pop()
    return order




