from sqlfluff.core import Linter


class SQLLinter:
    def __init__(self, dialect: str = "databricks"):
        self.linter = Linter(dialect=dialect)

    def lint_sql(self, sql_code: str):
        """Lints the given SQL code and returns a list of violations."""
        result = self.linter.lint_string(sql_code)
        violations = [
            {
                "line": v.line_no,
                "column": v.line_pos,
                "description": v.desc,
            }
            for v in result.get_violations()
        ]
        fixed_sql_code = result.fix_string()
        print(fixed_sql_code)
        return violations
