from typing import Union
import g4f
import asyncio
import os
import time

### CHANGE THE FILE NAME/PREFIX HERE. DO NOT INCLUDE .TXT
FILE_PREFIX = "reinforcement_learning"

# Note: The prompt adds to context length so don't make it too long
with open("prompt.txt", "r") as file:
    prompt = file.read()


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
        if response == "":
            # Sometimes for some reason the response is empty. so we need to catch this as an error.
            return response, txt_filename
        if (
            "none" in response.lower()
        ):  # highlight instances when the response for a file is None, which should be quite rare...
            print(f"No output! {txt_filename}")
            return "", 0
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
        # build with only the specified files
        calls = buildCalls(FILE_PREFIX, retry_files)
    results = await asyncio.gather(*calls)
    retry_files = []

    # Manually open and close files. this needs to be in append mode so that it doesn't overwrite what's already there.
    f = open(f"{FILE_PREFIX}_qns.txt", "a")

    # r is the response string, filepath is integer 0 if the response was successful, else its the filepath.
    for r, filepath in results:
        if isinstance(filepath, str):
            print(filepath)
            # if file has failed the first time round, retry later
            retry_files.append(filepath)
        else:
            f.write(r)
    f.close()

    if retry_files:
        print(f"Retrying with {retry_files}")
        await run_all(retry_files)

    return


asyncio.run(run_all())
