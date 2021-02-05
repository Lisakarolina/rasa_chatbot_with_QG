import ast

with open("qa_new.txt", "r") as file:   # open file with the questions and answers for the chatbot
    gesamt = [line.strip() for line in file]

gesamt = [ast.literal_eval(elem) for elem in gesamt]  # convert string to dictionary

fragen = [elem["question"] for elem in gesamt]
antw = [elem["answer"] for elem in gesamt]
retr_intent = "faq"

res_a = ""   # string that will be written into nlu.yml
res_b = ""   # string that will be written into domain.yml

# bring questions in appropriate format for nlu.yml
for index, frage in enumerate(fragen):
    res_a += "\n" + \
    f"- intent: {retr_intent}/{index}" + \
    "\n" + \
    "  examples: |" + \
    "\n" + \
    f"    - {frage}" + \
    "\n"

with open("data/nlu.yml", "a") as f:
    f.write(res_a)


# bring answers in appropriate format for domain.yml
for index, antwort in enumerate(antw):
    # antwort = f"{antwort}"
    res_b += "\n" + \
    f"  utter_{retr_intent}/{index}:" + \
    "\n" + \
    f"  - text: \"{antwort}\"" + \
    "\n"

with open("domain.yml", "a") as f:
    f.write(res_b)
