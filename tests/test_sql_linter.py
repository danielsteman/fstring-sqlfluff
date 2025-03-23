import pytest
from fstringsqlfluff.sql_linter import SQLLinter


@pytest.fixture
def linter():
    return SQLLinter()


def test_lint_sql(linter):
    sql_code = """
SELeCT
a,
b,
c FROM my_table WHeRE id = 1 LIMIT 10
    """
    result = linter.lint_sql(sql_code)
    expected = """SELECT
    a,
    b,
    c
FROM my_table
WHERE id = 1 LIMIT 10
"""
    assert result == expected
