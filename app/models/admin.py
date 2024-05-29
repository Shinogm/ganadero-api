from pydantic import BaseModel
from typing import Annotated
from fastapi import Form

class AdminModel(BaseModel):
    name: str
    last_name: str
    password: str
    email: str

    @classmethod
    def as_form(
        cls,
        name: Annotated[str, Form(...)],
        last_name: Annotated[str, Form(...)],
        password: Annotated[str, Form(...)],
        email: Annotated[str, Form(...)]
    ):
        return cls(
            name=name,
            last_name=last_name,
            password=password,
            email=email
        )

class AdminModifyModel(BaseModel):
    name: str | None = None
    last_name: str | None = None
    password: str | None = None
    email: str | None = None

    @classmethod
    def as_form(
        cls,
        name: Annotated[str | None, Form(...)] = None,
        last_name: Annotated[str | None, Form(...)] = None,
        password: Annotated[str | None, Form(...)] = None,
        email: Annotated[str | None, Form(...)] = None
    ):
        return cls(
            name=name,
            last_name=last_name,
            password=password,
            email=email
        )