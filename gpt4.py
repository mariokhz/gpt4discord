# Chat with an intelligent assistant in your terminal
from openai import Client, OpenAI
from openai.lib.azure import API_KEY_SENTINEL

# Point to the local server

def setopenai(openaitoken):
    global api_key
    api_key = openaitoken
    global client
    client = OpenAI(api_key=api_key)
def setsystem(system, modelo):
    global history
    history = [{"role": "system", "content": system}]
    global model
    model = modelo
    return True

def generar(text):
#while True:
    history.append({"role": "user", "content": [{"type" : "text", "text": text}]}) #{"type": "image_url", "image_url" : {"url" : "https://media.discordapp.net/attachments/1203797000164876348/1214659619998269500/Imagen06.png?ex=65f9eaec&is=65e775ec&hm=8bac92c3e2d85833456afdee8652a16ca7b79dd77807396747caf2e0988426c9&=&format=webp&quality=lossless&width=930&height=468"}}]})
    completion = client.chat.completions.create(
        model=model, # this field is currently unused
        messages=history,
        temperature=0.7,
        stream=True,
        max_tokens=1000,
    )

    new_message = {"role": "assistant", "content": ""}

    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)

    # Uncomment to see chat history
    # import json
    # gray_color = "\033[90m"
    # reset_color = "\033[0m"
    # print(f"{gray_color}\n{'-'*20} History dump {'-'*20}\n")
    # print(json.dumps(history, indent=2))
    # print(f"\n{'-'*55}\n{reset_color}")

    print()
    history.append({"role": "user", "content": text})
    return(new_message["content"])
