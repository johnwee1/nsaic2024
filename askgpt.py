import g4f
import asyncio

############## DO NOT RUN YET

_providers = [
    g4f.Provider.Aichat,
    g4f.Provider.ChatBase,
    g4f.Provider.Bing,
    g4f.Provider.GptGo,
    g4f.Provider.You,
    g4f.Provider.Yqcloud,
]

# Note: The prompt adds to context length so don't make it too long
with open("prompt.txt", "r") as file:
    prompt = file.read()


# TODO: Find a way to deploy multiple providers
async def run_provider(provider: g4f.Provider.BaseProvider):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": "Hello"}],
            provider=provider,
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)


async def run_all():
    calls = [run_provider(provider) for provider in _providers]
    await asyncio.gather(*calls)


asyncio.run(run_all())
