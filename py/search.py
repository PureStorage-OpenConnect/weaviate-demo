import weaviate
import json
import os

weaviate_key = os.getenv('WEAVIATE_KEY')
open_ai_key = os.getenv('OPENAI_KEY')

client = weaviate.Client(
    url = "http://10.21.100.220",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_key),  # Replace w/ your Weaviate instance API key
    additional_headers = {
        "X-OpenAI-Api-Key": open_ai_key  # Replace with your inference API key
    }
)

response = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text({"concepts": ["biology"]})
    .with_generate(grouped_task="Write a tweet with emojis about these facts.")
    .with_limit(2)
    .do()
)

print(json.dumps(response, indent=4))