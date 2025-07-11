from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  prompt={
    "id": "pmpt_686a083a208081908a71aae29d1462c60fd994a3c90371fb",
    "version": "1"
  }
)
