def tip_splitter(bill, tip_perc, people):
    if bill.isdigit() and tip_perc.isdigit() and people.isdigit():
        tip_perc = int(tip_perc)/100
        tip = int(bill)*tip_perc
        total = int(bill) + tip
        per_person = total/int(people)
        print(f"Tip: {tip}")
        print(f"Total: {total}")
        print(f"Per person: {per_person}")
    else:
        print("Please enter a valid number")


bill = input("What is the total of your bill?: ")
tip_perc = input("What is the percentage of the tip? (Don't add '%'): ")
people = input("How many people to spit the bill?: ")
tip_splitter(bill, tip_perc, people)