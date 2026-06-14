"""SPARQL -> Cypher Translation Task.

Each function returns a Cypher **string** whose executed result is
equivalent to the corresponding W9A SPARQL query (see the W9A drill at
`drill-9a-sparql/starter/queries/drill.py`). Equivalence is asserted by
the autograder as set-of-tuples equality on the named result columns,
ignoring row order (except where ORDER BY is part of the contract).

Run against the books mini-graph in `data/books_kg.cypher`.
"""
def q1() -> str:
    """
    SPARQL: SELECT ?book ?title WHERE { ?book a :Book ; :title ?title . }
    Columns: book (id string), title (string)
    """
    return "MATCH (b:Book) RETURN b.id AS book, b.title AS title"


def q2() -> str:
    """
    SPARQL: FILTER (?year > 2010)
    Columns: book (id string), year (int)
    """
    return "MATCH (b:Book) WHERE b.year > 2010 RETURN b.id AS book, b.year AS year"


def q3() -> str:
    """
    SPARQL: Multi-row join with Author
    Columns: book (id string), author_name (string)
    """
    return "MATCH (b:Book)-[:AUTHORED_BY]->(a:Author) RETURN b.id AS book, a.name AS author_name"


def q4() -> str:
    """
    SPARQL: OPTIONAL { ?book :topic ?topic }
    Columns: book (id string), topic (string or NULL)
    """
    return "MATCH (b:Book) OPTIONAL MATCH (b)-[:ON_TOPIC]->(t:Topic) RETURN b.id AS book, t.name AS topic"


def q5() -> str:
    """
    SPARQL: ASK { ?b :authored_by ?a1, ?a2 . FILTER (?a1 != ?a2) }
    Columns: result (boolean)
    """
    return """
    MATCH (b:Book)-[:AUTHORED_BY]->(a1:Author), (b)-[:AUTHORED_BY]->(a2:Author)
    WHERE id(a1) < id(a2)
    RETURN count(b) > 0 AS result
    """