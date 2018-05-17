i = 0

def add(quest):
    global i
    userInput = input(quest)
    i = i + int(userInput)
    print("the running total is", int(i))

def minus(question):
    global i
    userInput = input(question)
    i = i - int(userInput)

add("what is the first number?")
minus("what would you like to subtract?")
print("the FINAL number is", int(i))
