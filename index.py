import random


def update(alphabet, display, quizword):

    for i in range(len(quizword)):
        if quizword[i] == alphabet:
            display[i] = alphabet
            print(display)
    if alphabet not in quizword:
        print("OH no! its not there")
    return display


def check(res, quizword):
    st = ""
    for i in res:
        st = st+i
    if st == quizword:
        return 1
    else:
        return 0


words = ["apple", "banana", "orange", "sweetpotato", "fig","guava","mangosteen","strawberry"]
quizword = random.choice(words)

display = []
for item in quizword:
    display.append("_")
print("Guess the Word! you have 6 chances")
print(display)
n = 6
while n:
    print("Enter an alphabet:")
    sub = input()
    res = update(sub, display, quizword)
    if check(res, quizword):
        print("YES!! you Win")
        break
    elif sub not in quizword:
        n -= 1
        print(res)
        print(f"Try Again!you have {n} chances")
if n==0:
    print("You Loss!cant make in 6 chances. Better luck next time.")
