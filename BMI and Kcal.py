#BMI
print()
wzrost = float(input("How tall are you?: "))
print()
waga = float(input("How much you weigh?: "))
print()

BMI = float(waga / (wzrost ** 2)*10000)
#print("Twoje BMI wynosi:",BMI)
print("Twoje BMI jest równe: ", round(BMI,2))
print()
print("Now make sure that you eat well...")
print()
wiek = str(input("How old are you?: "))
print()
#Zapotrzebowanie kaloryczne'
#PPM: 10 x masa ciała + 6.25 x wzrost w cm + 5 x wiek  + S'
#współczynnik S: dla kobiet = -161, dla mężczyzn= +5'
#Praca niefizyczna, mało aktywny tryb życia	1,4 - pomnożyć dzienne zapotrzebowanie'
s=5

PPM=float(((10 * waga + 6.25 * wzrost + 5 * 25 + s)))

print("So... Your daily calories goal is:", round(PPM * 1.4,2),"kcal")
print("So now you could go to the gym! And no excuses!")
