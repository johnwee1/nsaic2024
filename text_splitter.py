import os


def text_spliter(filename):
    # 1 chat gpt token roughly 4 chars.

    # retrieve length of prompt to dynamically size chunks
    with open("prompt.txt", "r") as f:
        prompt_chars = len(f.read())
    with open(f"raws/{filename}.txt", "r") as file:
        full_file = file.read()
    # Split the text into smaller chunks of 16000 characters - prompt_chars
    chunksize = 16000 - prompt_chars - 100  # offset 100 in case
    chunks = [full_file[i : i + chunksize] for i in range(0, len(full_file), chunksize)]

    # mkdir split if it doesn't exist
    if not os.path.exists("split"):
        os.makedirs("split")

    # Write the individual chunks into directory "split/{filename}_chunk{i}.txt"
    for i, chunk in enumerate(chunks):
        with open(f"split/{filename}_chunk{i}.txt", "w+") as file:
            file.write(chunk)


text_spliter("stanford_ml_notes")
