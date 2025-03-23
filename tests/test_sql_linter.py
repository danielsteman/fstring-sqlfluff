import pytest
from fstringsqlfluff.sql_linter import SQLLinter


@pytest.fixture
def linter():
    return SQLLinter()


def test_lint_sql(linter):
    sql_code = """
SELECT
    a,
    b
FROM my_table
WHERE id = 1 LIMIT 10
    """
    result = linter.lint_sql(sql_code)
    violations = result.violations
    print(violations)
    assert isinstance(violations, list)
    for v in violations:
        assert isinstance(v, dict)
        assert "line" in v
        assert "column" in v
        assert "description" in v
