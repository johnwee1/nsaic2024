import g4f
import asyncio
from pathlib import Path
from g4f.client import Client
import nest_asyncio

async def runProvider(provider, prompt, text):
    client = Client(
    provider=provider
)
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt},{"role": "user", "content": text}],
)
    return response.choices[0].message.content


async def main():
    providers = [
        #  g4f.Provider.Aichat,
    g4f.Provider.ChatBase,
    g4f.Provider.Bing,
    g4f.Provider.GptGo,
    g4f.Provider.You,
    g4f.Provider.Yqcloud,
    ]

    with open("prompt.txt", "r") as file:
        prompt = file.read()

    text = "hello" ##change to the various textbooks later

    tasks = [runProvider(provider=p,prompt=prompt, text=text) for p in providers]

    responses = await asyncio.gather(*tasks)

    for provider, response in zip(providers, responses): ##response processing
        print(f"Response from {provider}: {response}")
    
if __name__ == "__main__":
    asyncio.run(main())