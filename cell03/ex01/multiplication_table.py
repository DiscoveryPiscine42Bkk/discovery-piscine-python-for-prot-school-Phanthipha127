number = int(input("Enter a number to generate ist multiplication table:"))
print(f"Mltiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = { number * i}")