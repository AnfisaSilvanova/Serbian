import random

# list of verbs
serbian_verbs = [
    "raditi",     # to work
    "učiti",      # to study
    "čitati",     # to read
    "gledati",    # to watch / to see
    "slušati",    # to listen
    "igrati",     # to play
    "voziti",     # to drive
    "nositi",     # to carry / to wear
    "pevati",     # to sing
    "živeti"      # to live
]

# dictionary of meanings
meanings = {
    "raditi": "to work",
    "učiti": "to study",
    "čitati": "to read",
    "gledati": "to watch / to see",
    "slušati": "to listen",
    "igrati": "to play",
    "voziti": "to drive",
    "nositi": "to carry / to wear",
    "pevati": "to sing",
    "živeti": "to live"
}

# Serbian pronouns
pronouns = {
    "1s": ["ja"],         # I
    "2s": ["ti"],         # you (singular)
    "3s": ["on", "ona", "ono"],   # he, she, it
    "1p": ["mi"],         # we
    "2p": ["vi"],         # you (plural)
    "3p": ["oni", "one", "ona"]   # they (m, f, n)
}

# random selections
pronoun_group = random.choice(list(pronouns.keys()))
pronoun = random.choice(pronouns[pronoun_group])
verb = random.choice(serbian_verbs)

last_letter = verb[-3]

# correct answer
if pronoun_group == "1s":
    answer = verb[:-2] + "m"
elif pronoun_group == "2s":
    answer = verb[:-2] + "š"
elif pronoun_group == "3s":
    answer = verb[:-2]
elif pronoun_group == "1p":
    answer = verb[:-2] + "mo"
elif pronoun_group == "2p":
    answer = verb[:-2] + "te"
elif pronoun_group == "3p":
    if last_letter == "a":
        answer = verb[:-3] + "aju"
    elif last_letter == "i":
        answer = verb[:-3] + "e"
    elif last_letter == "e":
        answer = verb[:-3] + "u"
    else:
        answer = "erro"  # or some fallback logic
else:
    answer = "The answer is incorrect"

print(f"Group: {pronoun_group} | Pronoun: {pronoun} | Verb: {verb}")
print(pronoun, verb)
user_input = input("Type your answer: ")

if user_input.strip() == f"{answer}":
    print("✅ Correct!")
else:
    print(f"❌ Incorrect. The right answer is: {pronoun} {answer}")

print(f"The correct answer is: {pronoun} {answer}")
print(f"By the way, {verb} means: {meanings[verb]}")
