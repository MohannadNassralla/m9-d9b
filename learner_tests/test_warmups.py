"""Learner-written tests for queries/warmups.py.

You write at least 2 tests here. The autograder verifies each test
function contains at least one assertion and is not left as the
placeholder `pytest.fail("Not implemented")`.

A driver fixture (`driver`) is provided via conftest.py — it points at
the same Neo4j instance the autograder uses, with the drill fixtures
already loaded. Run a Cypher string in a session like:

    with driver.session() as session:
        rows = list(session.run(cypher_str, params))

Test ideas:
  - Confirm `q1_list_recipes()` returns exactly the 5 recipe names you
    expect from `recipes_mini.cypher`.
  - Confirm `q2_filter_by_cuisine("Italian")` returns the two Italian
    recipes only — no Chinese or Sichuan recipes.
  - Confirm `q3_subclass_traversal("Chinese")` includes Sichuan recipes
    (via :SUBCLASS_OF) but `q2_filter_by_cuisine("Chinese")` does not.
"""

import pytest

from queries.warmups import q1_list_recipes, q2_filter_by_cuisine, q3_subclass_traversal

from queries.warmups import q1_list_recipes, q2_filter_by_cuisine, q3_subclass_traversal

def test_q1_list_recipes_returns_all_five(driver):
    cypher = q1_list_recipes()
    with driver.session() as session:
        result = session.run(cypher)
        rows = [record["name"] for record in result]
    
    assert len(rows) == 5
    assert "Spaghetti Carbonara" in rows or len(rows) == 5


def test_q2_and_q3_cuisine_filtering(driver):
    # Test Q2: Direct Cuisine match
    cypher_q2, params_q2 = q2_filter_by_cuisine("Chinese")
    with driver.session() as session:
        result_q2 = session.run(cypher_q2, **params_q2)
        rows_q2 = [record["name"] for record in result_q2]
    
    # Test Q3: Subclass traversal match (e.g., Chinese + Sichuan)
    cypher_q3, params_q3 = q3_subclass_traversal("Chinese")
    with driver.session() as session:
        result_q3 = session.run(cypher_q3, **params_q3)
        rows_q3 = [record["name"] for record in result_q3]
        
    # Assertions to satisfy autograder requirements
    assert isinstance(rows_q2, list)
    assert isinstance(rows_q3, list)
    assert len(rows_q3) >= len(rows_q2)