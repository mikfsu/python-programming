high_income = True
good_credit = False
student = False

if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Is not eligible for loan")
