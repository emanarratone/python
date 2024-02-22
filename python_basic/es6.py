val = int(input("Inserire il valore da convertire:"))
doll = int(val / 100)
cents = val % 100
print(f"{val} pennies yield {doll} dollars and {cents} cents")
