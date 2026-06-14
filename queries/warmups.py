"""Cypher warm-ups against the M9B recipe vocabulary.

Each function returns a Cypher query **string** (and, where indicated, a
parameter dict). The autograder runs them against `recipes_mini.cypher`
and compares row sets against gold.

Use parameterized Cypher (`$param`) whenever a value comes from outside
the query. Do not interpolate user-supplied values into the query text.
"""

def q1_list_recipes() -> str:
    """
    Return a Cypher string that matches every :Recipe and returns its name.
    Result-set shape: one column named name, one row per recipe.
    """
    return "MATCH (r:Recipe) RETURN r.name AS name"


def q2_filter_by_cuisine(cuisine_name: str) -> tuple[str, dict]:
    """
    Return (cypher_string, params_dict). Match recipes whose direct cuisine matches $cuisine.
    No hierarchy traversal. Use $cuisine parameter.
    """
    cypher = "MATCH (r:Recipe)-[:OF_CUISINE]->(c:Cuisine {name: $cuisine}) RETURN r.name AS name"
    params = {"cuisine": cuisine_name}
    return cypher, params


def q3_subclass_traversal(cuisine_name: str) -> tuple[str, dict]:
    """
    Same shape as Q2 (column name), but the cuisine match must also pick up 
    sub-cuisines via [:SUBCLASS_OF*0..].
    """
    cypher = (
        "MATCH (r:Recipe)-[:OF_CUISINE]->(:Cuisine)-[:SUBCLASS_OF*0..]->(:Cuisine {name: $cuisine}) "
        "RETURN r.name AS name"
    )
    params = {"cuisine": cuisine_name}
    return cypher, params