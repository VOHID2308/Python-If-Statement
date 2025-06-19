oy = int(input("Oy raqamini kiriting (1-12): "))

if oy == 12 or oy == 1 or oy == 2:
    print("Qish")
elif oy == 3 or oy == 4 or oy == 5:
    print("Bahor")
elif oy == 6 or oy == 7 or oy == 8:
    print("Yoz")
elif oy == 9 or oy == 10 or oy == 11:
    print("Kuz")
else:
    print("Notogri oy raqami!")
