from sqlfluff.core import Linter

linter = Linter(dialect="databricks")
sql_code = "SELECT * FROM my_table WHERE id = 1"
result = linter.lint_string(sql_code)

# Get list of linting violations
violations = result.get_violations()
for v in violations:
    print(f"Line {v.line_no}, Col {v.line_pos}: {v.desc}")
