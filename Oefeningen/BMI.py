bmi = float(input("BMI"))

if bmi < 18.5:
    print("Ondergewicht") 
elif bmi >= 18.5 or bmi <= 24.9:
    print("Gezond gewicht")
elif bmi >= 25 or bmi <= 29.9:
    print("Overgewicht")
elif bmi >= 30 or bmi <= 34.9:
    print("Obesita")
else:
    print("Exteme obesitas")


#volgorde belangrijk
#Elinatie