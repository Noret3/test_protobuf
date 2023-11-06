from fastapi import FastAPI, Response
from person_pb2 import Person

app = FastAPI()


class OctetStreamResponse(Response):
    media_type = "application/octet-stream"


@app.get('/', response_class=OctetStreamResponse)
def hello(data: Person):
    print(data)
    response = b'\n\x05Alice\x10\x1e'
    return Response(content=response, media_type="application/octet-stream")
