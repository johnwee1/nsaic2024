from g4f.client import Client
from g4f.Provider import (
    RetryProvider,
    You,  # for some reason it doesnt work on my machine anymore maybe im banned
    Gemini,
    Liaobots,
    ChatForAi,  # doesnt work
    Chatgpt4Online,
    ChatgptNext,
)
from undetected_chromedriver import Chrome, ChromeOptions
import json
import re
import g4f.debug
import time

g4f.debug.logging = True

########### Reorder this if a provider isnt working.
retryprovider = RetryProvider(
    [ChatgptNext, Liaobots, Gemini, Chatgpt4Online, You], shuffle=False
)
########### CHANGE this if you want
answerprompt = "Give a detailed answer to the following question that is asked in the context of machine learning.\n"

# change the filename to ur manually cleaned file
# txt_filename = "YOURFILENAMEHERE.txt"
with open(txt_filename, "r") as f:
    text = f.readlines()


######## YOU NEED TO CREATE A TEXT FILE WITH A NUMBER (START WITH 0) INSIDE TO MANUALLY TRACK THE LINES so u can stop and start as needed
def createResponse(provider):
    with open("FILENAME_progress.txt", "r") as f:
        line = int(f.read())

    if int(line) == len(text):
        print("Job finished")
        return False

    client = Client(provider=provider)

    response = client.chat.completions.create(
        model="",
        messages=[{"role": "user", "content": answerprompt + text[line]}],
        webdriver=webdriver,
    )
    log_to_jsonl(text[line], response.choices[0].message.content)
    line += 1
    with open("manual_progress.txt", "w") as f:
        f.write(str(line))
    # print(response.choices[0].message.content)
    return True


def log_to_jsonl(question, answer):
    answer = remove_markdown_links(answer)
    log_entry = {"instruction": question, "context": "", "response": answer}
    with open("presorted_gpt_answers.jsonl", mode="a+", encoding="utf-8") as file:
        json.dump(log_entry, file)
        file.write("\n")


def remove_markdown_links(input_string):
    # Define the regex pattern to match markdown links
    markdown_link_pattern = r"\[\[.*?\]\]\(.*?\)"

    # Use re.sub to replace all occurrences of the pattern with an empty string
    result_string = re.sub(markdown_link_pattern, "", input_string)

    return result_string


options = ChromeOptions()
options.add_argument("--incognito")
webdriver = Chrome(options=options, headless=True)
while True:
    try:
        x = createResponse(retryprovider)
    except TimeoutError:
        time.sleep(20)  # idk bruh wait like 20 seconds n try again
    time.sleep(2)
    if not x:
        break
webdriver.quit()
