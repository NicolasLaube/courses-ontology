"""This modules define utility functions for the Prolog reasoner"""

import pyswip


def export_predicated_to_prolog(onto, prolog, verbose=False):
    """This function exports all the ontology predicates to Prolog"""
    for i in onto.individuals():
        for c in i.is_a:
            if verbose:
                print(f"{c.name.lower()}('{i.name}')")
            prolog.assertz(f"{c.name.lower()}('{i.name}')")
    for p in onto.object_properties():
        for o1, o2 in p.get_relations():
            if verbose:
                print(f"{p.name.lower()}('{o1.name}', '{o2.name}')")
            prolog.assertz(f"{p.name.lower()}('{o1.name}', '{o2.name}')")


def pyswip_output_to_str(inp):
    """This function transforms an output of Prolog to a string"""
    if type(inp) is bytes:
        # inp: bytes
        return f'"{inp.decode("utf-8")}"'
    elif type(inp) is int:
        # inp: int
        return str(inp)
    elif type(inp) is pyswip.easy.Variable:
        # inp: pyswip.easy.Variable
        if inp.chars is None:
            return f"_{inp.handle}"
        else:
            return inp.chars
    elif type(inp) is pyswip.easy.Atom:
        # inp: pyswip.easy.Atom
        return f"{inp.value}"
    elif type(inp) is pyswip.easy.Functor:
        return (
            f"{inp.name}("
            + ",".join([pyswip_output_to_str(arg) for arg in inp.args])
            + ")"
        )
    elif type(inp) is list:
        # inp: pyswip.easy.List
        return "[" + ",".join(pyswip_output_to_str(child) for child in inp) + "]"
    else:
        return inp


def pyswip_to_str(results):
    """This function transforms a result from a Prolog query to a string"""
    all_results = []
    for result in results:
        all_results.append({})
        for k, v in result.items():
            all_results[-1][k] = pyswip_output_to_str(v)
    return all_results
