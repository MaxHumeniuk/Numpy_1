# generated by datamodel-codegen:
#   filename:  historical_data.json
#   timestamp: 2024-03-28T15:18:26+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Model(BaseModel):
    __root__: List[List[List[float]]]