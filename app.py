from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

sentiment_pipe = pipeline("sentiment-analysis")

app = FastAPI()

print(sentiment_pipe("I am having a bad day"))

class RequestModel(BaseModel):
    input_string: str

@app.post('/analyze')
def func(request: RequestModel):

    input_string = request.input_string

    sentiment = sentiment_pipe(input_string)
    return {"result":
            {"sentiment category" : sentiment[0]["label"],
            "score for sentiment" : sentiment[0]["score"]}
            }
