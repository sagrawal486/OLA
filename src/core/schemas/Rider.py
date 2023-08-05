from pydantic import BaseModel

class Rider(BaseModel):
    id: str
    name: str

    def __init__(self,id,name ) -> None:
        super().__init__(id = id, name = name)
