import openai

def record_to_en_text(record):
    text = openai.Audio.translate("whisper-1", record)["text"]
    return text


def he_to_en_text(text):
    openai.api_key = "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"
    messages = [
        {"role": "user",
         "content": "translate the following text into english, write the translation only!\nThe text:\n" + text }
    ]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response = completion.choices[0].message["content"]
    print(response)
    return response
