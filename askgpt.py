from typing import Union
import g4f
import asyncio
import os
import time

FILE_PREFIX = "stanford_ml_notes"

# Note: The prompt adds to context length so don't make it too long
with open("prompt.txt", "r") as file:
    prompt = file.read()


# TODO: Find a way to deploy multiple instances of this on all the text files
# for some reason, it always falls back to using the You provider. the moment we crack this we can start spamming requests
async def run_provider(txt_filename, prefix):
    with open(txt_filename, "r") as f:
        text = f.read()
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.gpt_35_long,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text},
            ],
            # provider=provider
        )
        print("Response:", response)
        return response, 0
    except Exception as e:
        print("Exception:", e)
        return response, txt_filename


def buildCalls(prefix: str, retry_files=None):
    """Retrieves all the text chunks in the ./split/ directory with the prefix name."""

    dest = os.path.join(".", "split")
    files = []  # final results will NOT be sorted.
    if not retry_files:
        for filename in os.listdir(dest):
            if filename.startswith(prefix) and filename.endswith(".txt"):
                files.append(os.path.join(dest, filename))
    else:
        files = retry_files
    # debug
    # for f in files:
    #     print(f)
    calls = []
    for f in files:
        calls.append(run_provider(f, prefix))
    return calls


async def run_all(retry_files=None):
    if not retry_files:
        calls = buildCalls(FILE_PREFIX)  # make a function that builds the list of calls
    else:
        # build with only the specified files i guess?
        calls = buildCalls(FILE_PREFIX, retry_files)
    results = await asyncio.gather(*calls)
    retry_files = []
    f = open(f"{FILE_PREFIX}_qns", "w+")  # Manually open and close files
    for r, status in results:
        if isinstance(status, str):
            print(status)
            # if file has failed the first time round, retry later
            retry_files.append(status)
        else:
            f.write(r)
    f.close()
    if retry_files:
        run_all(retry_files)
    return


asyncio.run(run_all())
