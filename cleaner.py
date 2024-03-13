import re

# run this file to run a simple pattern matching to detect errors file and appends erroneouis inpits t error_qns.jsonl which we can clean up at a further date or completely regenerate

with open("sample_d2l_qns.jsonl", "r") as f:
    x = f.readlines()


def contains_pattern(text):
    pattern = r"\?\d\."
    if re.search(pattern, text):
        return True
    else:
        return False


validated = []
err = []

# performs the checks
for line in x:
    if contains_pattern(line) or len(line) > 3000:
        err.append(line)
    else:
        validated.append(line)


def pf(arr, file):
    with open(file, "a+") as f:
        f.writelines(arr)


pf(validated, "validated_qns.jsonl")
pf(err, "error_qns.jsonl")
