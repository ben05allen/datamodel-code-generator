# generated by datamodel-codegen:
#   filename:  bar.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class JobRun(BaseModel):
    enabled: Optional[bool] = Field(False, description='If Live Execution is Enabled.')