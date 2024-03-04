from pathlib import Path
import os


def text_spliter(filename):
    # 1 chat gpt token roughly 4 chars.

    # retrieve length of prompt to dynamically size chunks
    with open("prompt.txt", "r", errors="replace") as f:
        prompt_chars = len(f.read())

    raw_file_path = Path("raws") / f"{filename}.txt"
    with raw_file_path.open("r", errors="replace") as f:
        full_file = f.read()

    # Split the text into smaller chunks of 16000 characters - prompt_chars
    chunksize = 16000 - prompt_chars - 100  # offset 100 in case
    chunks = [full_file[i : i + chunksize] for i in range(0, len(full_file), chunksize)]

    # mkdir split if it doesn't exist
    split_dir = Path("split")
    split_dir.mkdir(exist_ok=True)

    # Write the individual chunks into directory "split/{filename}_chunk{i}.txt"
    for i, chunk in enumerate(chunks):
        chunk_file_path = split_dir / f"{filename}_chunk{i}.txt"
        with chunk_file_path.open("w+") as file:
            file.write(chunk)


text_spliter("reinforcement_learning")
