import requests

url = 'http://localhost:8000/candidates'

# myobj = {'name': 'test'}

# x = requests.post(url, data=myobj)

# print(x.text)

# PARAMS = {'name': 'test'}
# r = requests.get(url, params=PARAMS)
# data = r.json()
# print(len(data))


class Candidate():
    def __init__(self, name, confidence):
        self.name = name
        self.confidence = confidence

    def __repr__(self):
        return "% s ""(% s)" % (self.name, self.confidence)


def train(input_word):
    # train_input = input("Please enter words.")
    train_input_list = input_word.split()
    for item in train_input_list:
        myObj = {'name': item}
        r = requests.post(url, data=myObj)
        print(r.text)


def train_general():
    train_input = input_word.split()

# def getWords(new_input):
#     for item in bank:
#         if new_input in item:
#             candidates.append(item)


candidates = []
outputs = []


def getConfidence():
    used_words = []
    for item in candidates:
        counter = 0
        for other in candidates:
            if item == other:
                counter = counter + 1
        if used_words.count(item) < 1:
            outputs.append(Candidate(item, counter))
        used_words.append(item)
    final_answer = sorted(
        outputs, key=lambda x: x.confidence, reverse=True)
    for item in final_answer:
        print(item)


def autocomplete_provider(input_word):
    # input_word = input("Please enter fragment")
    r = requests.get(url)
    data = r.json()
    for item in data:
        if input_word in item['name']:
            candidates.append(item['name'])
    # used = []
    # for item in candidates:
    #     if used.count(item) < 1:
    #         print(item and candidates.count(item))
    #         used.append(item)
    getConfidence()
    train(input_word)


def runProgram():
    purpose = input(
        "If you would like to train, press a. If you would like to see autocomplete options, press b.")
    if purpose == ('a'):
        input_word = input("Please enter words.")
        train(input_word)
    if purpose == ('b'):
        input_word = input("Please enter fragment.")
        autocomplete_provider(input_word)


runProgram()
