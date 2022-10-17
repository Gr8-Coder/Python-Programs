# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1 .lower()
a=lower_name1 .count("t")
b=lower_name1 .count("r")
c=lower_name1 .count("u")
d=lower_name1 .count("e")

e=lower_name1 .count("l")
f=lower_name1 .count("o")
g=lower_name1 .count("v")
h=lower_name1 .count("e")

lower_name2 = name2 .lower()
i=lower_name2 .count("t")
j=lower_name2 .count("r")
k=lower_name2 .count("u")
l=lower_name2 .count("e")

m=lower_name2 .count("l")
n=lower_name2 .count("o")
o=lower_name2 .count("v")
p=lower_name2 .count("e")

T = a + i
R = b + j
U = c + k
E = d + l
total1= T+R+U+E

L = e + m
O = f + n
V = g + o
E = h + p
total2= L+O+V+E

print(f"T occurs {T} times")
print(f"R occurs {R} times")
print(f"U occurs {U} times")
print(f"E occurs {E} times")
print(f"Total: {total1}")
print("\n")
print(f"L occurs {L} times")
print(f"O occurs {O} times")
print(f"V occurs {V} times")
print(f"E occurs {E} times")
print(f"Total: {total2}")

print("Love score = " + str(total1) + str(total2))
print("Your love score is = " + str(total1) + str(total2))

love_score = str(total1) + str(total2)
love = int(love_score)

if love<10 or love>90:
  print(f"Your score is {love}, you go together like coke and mentos.")
elif love>40 and love<50:
 print(f"Your score is {love}, you are alright together.")
else:
  print(f"Your score is {love}.")
