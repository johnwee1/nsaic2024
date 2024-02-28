# A synchronous version of the askgpt.py file that tests API responses

from pathlib import Path
from g4f.client import Client
import g4f.debug
import long_text_splitter

g4f.debug.logging = True

long_text_splitter.text_spliter("stanford_ml_notes")


TEST_FILEPATH = Path("split") / "stanford_ml_notes_chunk0.txt"

with open("prompt.txt", "r") as f:
    prompt = f.read()

with open(TEST_FILEPATH, "r") as f:
    text = f.read()


client = Client()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": prompt}, {"role": "user", "content": text}],
)
print(response.choices[0].message.content)

# Log response in test.log
with open(f"{__name__}.log", "w+") as f:
    f.write(response.choices[0].message.content)
