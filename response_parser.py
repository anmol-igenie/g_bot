import re
from typing import Any
import pandasai.pandas as pd
from pandasai.responses.response_parser import ResponseParser

class GenieResponse(ResponseParser):
    def __init__(self, context):
        super().__init__(context)

    def parse(self, result: dict) -> Any:

        if not isinstance(result, dict) or any(
            key not in result for key in ["type", "value"]
        ):
            return ""

        if result["type"] == "dataframe":
            return self.format_dataframe(result)
        else:
            return ""

    def format_dataframe(self, result: dict) -> None:
        return result['value'].to_json(orient='records')
