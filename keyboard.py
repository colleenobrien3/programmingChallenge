bank = []
input_example = "the third thing that I need to tell you is that this thing does not think thoroughly"
example_list_version = input_example.split()
candidates = []
outputs = []

for item in example_list_version:
    bank.append(item)


class Candidate():
    def __init__(self, name, confidence):
        self.name = name
        self.confidence = confidence

    def __repr__(self):
        return "% s ""(% s)" % (self.name, self.confidence)


def getWords(new_input):
    for item in bank:
        if new_input in item:
            candidates.append(item)


def getConfidences():
    used_words = []
    for item in candidates:
        counter = 0
        for other in candidates:
            if item == other:
                counter = counter + 1
        if used_words.count(item) < 1:
            outputs.append(Candidate(item, counter))
        used_words.append(item)


def train(input_value):
    input_list_version = input_value.split()
    for item in input_list_version:
        bank.append(item)


def AutocompleteProvider():
    purpose = input(
        "If you would like to train the algorithm, press a. If you would like to recieve suggestions based on an input, press b.")
    if purpose == 'a':
        input_value = input("Please input values.")
        train(input_value)
        again = input(
            "Thank you. Training complete. Enter 'y' if you are ready to search.")
        if again == 'y':
            AutocompleteProvider()
    elif purpose == 'b':
        new_input = input("Please input search.")
        getWords(new_input)
        getConfidences()
        final_answer = sorted(
            outputs, key=lambda x: x.confidence, reverse=True)
        for item in final_answer:
            print(item)
    else:
        print('Ooops. Does not compute. Try again.')
        return


AutocompleteProvider()
