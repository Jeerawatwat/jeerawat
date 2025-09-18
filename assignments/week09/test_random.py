import random

def test_random():
    random_number = random.randint(1, 10)
    Totalrandom = int(input("EnterNumber ="))
    if random_number == Totalrandom:
        print("correct")
    else :
        print("Not Number")   
    print(random_number)
    
test_random()