from pydantic import BaseModel
from typing import Annotated
from fastapi import Form

class WorkerModel(BaseModel):
    name: str
    last_name: str

    @classmethod
    def as_form(
        cls,
        name: Annotated[str, Form(...)],
        last_name: Annotated[str, Form(...)]
    ):
        return cls(
            name=name,
            last_name=last_name
        )

class WorkerModifyModel(BaseModel):
    name: str | None = None
    last_name: str | None = None

    @classmethod
    def as_form(
        cls,
        name: Annotated[str | None, Form(...)] = None,
        last_name: Annotated[str | None, Form(...)] = None
    ):
        return cls(
            name=name,
            last_name=last_name
        )