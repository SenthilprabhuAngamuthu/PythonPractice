def cal_bmi(wt, ht):
    bmi = weight/pow(height,2)
    return bmi

weight = float(input("Enter the Weight : "))
height = float(input("Enter the height in cm: "))
print("your BMI: " +"{}".format(cal_bmi(weight, height)))


