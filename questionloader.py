import json


# write a function that loads in a jsonl file and appends to a text file called "questions.txt"
def load_questions(jsonl_file, txt_file):
    with open(jsonl_file, "r") as file:
        with open(txt_file, "a") as txt:
            for line in file:
                data = json.loads(line)
                txt.write(data["instruction"] + "\n")


load_questions("aws-lol-samples/sample1/train.jsonl", "questions.txt")
load_questions("aws-lol-samples/sample2/train.jsonl", "questions.txt")
load_questions("aws-lol-samples/sample3/train.jsonl", "questions.txt")
