from dataclasses import dataclass
from typing import Any
from sqlfluff.core import Linter
import sqlfluff


class SQLLinter:
    def __init__(self, dialect: str = "databricks"):
        self.linter = Linter(dialect=dialect)

    def lint_sql(self, sql_code: str) -> str:
        return sqlfluff.fix(sql_code)
