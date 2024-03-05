import re
import os

"""Helper script to sanitize the output from gpt files. idk how useful this will be but whatevs"""

### the .txt suffix IS NEEDED HERE!
FILENAME = "deeplearning1_qns.txt"


def parse_text_file(input_file, output_file):
    with open(input_file, "r", errors='replace') as infile, open(output_file, "w+", errors='replace') as outfile:
        for line in infile:
            line = line.replace("*", "")
            # Use regular expressions to check if the line starts with a number or a bullet point
            number_match = re.match(r"^\d+\.", line)
            bullet_point_match = re.match(r"^\s*-", line)

            if number_match:
                # If the line starts with a number, write the text without the number prefix
                outfile.write(re.sub(r"^\d+\.\s*", "", line))
            elif bullet_point_match:
                # If the line starts with a bullet point, write the text without the bullet point prefix
                outfile.write(re.sub(r"^\s*-\s*", "", line))


def strp_refs(input_file, output_file):
    """deletes [[x]] where x is a number"""
    with open(input_file, "r", errors='replace') as infile, open(output_file, "w+", errors='replace') as outfile:
        for line in infile:
            if re.search(r"\[\[\d+\]\]$", line):
                # If the line ends with a pattern like [[x]], remove it
                outfile.write(re.sub(r"\[\[\d+\]\]$", "", line))
            else:
                outfile.write(line)


def questionize(input_file, output_file):
    """
    Turns a statement, "Support vector machine" into a question:
    'What is the concept of Support vector machine?'"""
    with open(input_file, "r", errors='replace') as infile, open(output_file, "w+", errors='replace') as outfile:
        for line in infile:
            if not line.strip().endswith("?"):
                # If the line ends with a question mark, replace it with the modified question format
                outfile.write(f"What is the concept of '{line.strip()}'?\n")
            else:
                outfile.write(line)


def sanitize(input):
    output = f"sanitized_{input}"
    parse_text_file(input, "temp1.txt")
    strp_refs("temp1.txt", "temp2.txt")
    questionize("temp2.txt", output)
    os.remove("temp1.txt")
    os.remove("temp2.txt")


# NOTE: CHANGE THE FILE NAMES FOR DIFFERENT FILES!
sanitize(FILENAME)

# if it looks good to you, u can delete the pre-sanitized output and just keep the cleaned up one.
