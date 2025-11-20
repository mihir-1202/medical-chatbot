from fastapi import FastAPI, Depends
from dependencies import get_retrieval_chain
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(chat_request: ChatRequest, retrieval_chain = Depends(get_retrieval_chain)):
    response = retrieval_chain.invoke({"input": chat_request.prompt})
    print(response)
    return response['answer']

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)