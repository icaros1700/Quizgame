
print("Welcome to my computer quiz!!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":   # Convierte todo lo que escribas en minusculas
    quit()

print("OK, Let's play!!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "Central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "Graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "Random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "Power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!!")
print("You got " + str((score/4) * 100) + " %")
