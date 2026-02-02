acceptable_answers = ["A", "B", "C", "D"]

def grade_quiz(key, answers):
    invalid = []

    correct = 0
    for i in range(len(answers)):
        if answers[i] not in acceptable_answers:
            invalid.append(answers[i])
        elif answers[i] == key[i]:
            correct += 1

    if invalid:
        print("Invalid input. Please only use letters A–D.")
    else:
        score = (correct / len(key)) * 100
        print(f"Score: {score}% ({correct}/{len(key)} correct)")


key = input("Enter answer key (comma separated): ").upper().split(",")
answers = input("Enter answers (comma separated): ").upper().split(",")
key = [k.strip() for k in key]
answers = [a.strip() for a in answers]

if len(key) == len(answers):
    grade_quiz(key, answers)
else:
    print(f"Sorry, the quiz has {len(key)} questions. You entered {len(answers)} answers.")
