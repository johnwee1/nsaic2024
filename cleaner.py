import re

with open("gpt_answers.jsonl", "r") as f:
    x = f.readlines()


def contains_pattern(text):
    pattern = r"\?\d\."
    if re.search(pattern, text):
        return True
    else:
        return False


validated = []
err = []

for line in x:
    if contains_pattern(line):
        err.append(line)
    else:
        validated.append(line)


def pf(arr, file):
    with open(file, "a+") as f:
        f.writelines(arr)


pf(validated, "validated_qns.jsonl")
pf(err, "error_qns.jsonl")
