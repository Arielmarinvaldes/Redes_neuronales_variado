import openai

openai.api_key = "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"

while True:
    prompt = input("\nIntroduce una pregunta: ")
    if prompt == "exit":
        break
    
    completion = openai.Completion.create(engine="text-davinci-003",
                            prompt=prompt,
                            max_tokens=2048)

print(completion.choices[0].text)