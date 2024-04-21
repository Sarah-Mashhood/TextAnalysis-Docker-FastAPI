from gradio_client import Client
def test_positive_sentiment(input_text):
  client = Client("MSarah/SentimentAnalysis")
  result = client.predict(
		  text=input_text,
		  api_name="/predict"
  )
  print(result)

def test_negative_sentiment(input_text):
  client = Client("MSarah/SentimentAnalysis")
  result = client.predict(
		  text=input_text,
		  api_name="/predict"
  )
  print(result)