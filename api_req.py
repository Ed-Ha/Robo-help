import openai

try:
    with open('api_key.txt', 'r') as file:
        api_key = file.read().strip()
except Exception as e:
    print(f"An error occurred while reading the 'api_key.txt' file: {e}")

openai.api_key = api_key

def handle_API_request(messages):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        response = completion.choices[0].message["content"]
        messages.append({"role": "assistant", "content": response})
        return messages
