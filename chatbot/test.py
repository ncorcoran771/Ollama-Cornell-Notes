import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        mode = "gpt-3.5-turbo",
        messages = [{"role": "user", "content":prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        userInput = input("You: ")
        if userInput.lower() in ["quit","exit","bye"]:
            break

        response = chat_with_gpt(userInput)
        print("AI: ", response)