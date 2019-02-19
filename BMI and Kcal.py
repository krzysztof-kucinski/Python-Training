#BMI
wzrost = 1.98
waga = 105
BMI = waga / (wzrost ** 2)
#print("Twoje BMI wynosi:",BMI)
print("Your BMI is: ", 105 / 1.98**2)

#Zapotrzebowanie kaloryczne'
#PPM: 10 x masa ciała + 6.25 x wzrost w cm – 5 x wiek  + S'
#współczynnik S: dla kobiet = -161, dla mężczyzn= +5'
#Praca niefizyczna, mało aktywny tryb życia	1,4 - pomnożyć dzienne zapotrzebowanie'
print()
s= 5
waga=105
wzrost=198
wiek=26
PPM=10*waga+6.25*wzrost+5*25+s
print("Your daily calories goal is:", PPM * 1.4,"kcal")
print()
print("So now you could go to the gym!")