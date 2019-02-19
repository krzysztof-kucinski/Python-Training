#BMI
print()
wzrost = float(input("How tall are you?: "))
print()
waga = int(input("How much you weigh?: "))
print()

BMI = str(waga / (wzrost ** 2)*10000)
#print("Twoje BMI wynosi:",BMI)
print("Your BMI is: ", BMI)
print()
print("Now make sure that you eat well...")
print()
wiek = int(input("How old are you?: "))
print()
#Zapotrzebowanie kaloryczne'
#PPM: 10 x masa ciała + 6.25 x wzrost w cm + 5 x wiek  + S'
#współczynnik S: dla kobiet = -161, dla mężczyzn= +5'
#Praca niefizyczna, mało aktywny tryb życia	1,4 - pomnożyć dzienne zapotrzebowanie'
s=5

PPM=((10 * waga + 6.25 * wzrost + 5 * 25 + s))

print("So... Your daily calories goal is:", PPM * 1.4,"kcal")
print("So now you could go to the gym! And no excuses!")
