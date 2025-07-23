decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]  # Remove the '0b' prefix
print(f"Binary equivalent: {binary}")
