def prime_checker(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def analyze_number(num):
    if prime_checker(num):
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")

    primes = []
    for i in range(2, num + 1):
        if prime_checker(i):
            primes.append(i)

    print(f"Prime numbers up to {num}: {primes}")

num = input("Input a number: ")
if num.isdigit():
    num = int(num)
    analyze_number(num)
else:
    print("Sorry, invalid input. Please enter a valid number")