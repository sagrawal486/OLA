from pydantic import BaseModel

class PostResponse(BaseModel):
    status: str
    message: str
    OK_RESPONSE = 'ok'
    ERROR_RESPONSE = 'error'

    def __init__(self,status,message):
        super().__init__(status=status, message=message)

    def ok(self):
        return PostResponse(self.OK_RESPONSE,None)

    def error(self):
        return PostResponse(self.ERROR_RESPONSE,None)
