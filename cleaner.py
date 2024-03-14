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


def replace_escaped_unicode_backslash_with_space(input_string):
    # Use regex to find escaped Unicode characters
    escaped_unicode_regex = r"\\u([0-9a-fA-F]{4})"
    matches = re.finditer(escaped_unicode_regex, input_string)

    # Replace the backslash with a space for each match
    cleaned_string = input_string
    for match in matches:
        escaped_unicode = match.group(0)
        cleaned_string = cleaned_string.replace(
            escaped_unicode, " " + escaped_unicode[1:]
        )

    return cleaned_string


validated = []
err = []

# performs the checks
for line in x:
    line = replace_escaped_unicode_backslash_with_space(line)
    if contains_pattern(line) or len(line) > 7800:
        print(line)
        err.append(line)
    else:
        validated.append(line)


# THIS OVERRIDES THE CURRENT FILE!
def pf(arr, file):
    with open(file, "w+") as f:
        f.writelines(arr)


pf(validated, "validated_qns.jsonl")
pf(err, "error_qns.jsonl")
