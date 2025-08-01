from openai import OpenAI
client = OpenAI(api_key=("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"))

response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)