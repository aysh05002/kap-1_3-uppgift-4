pris=int(input("Ordinarie pris "))
rabat=int(input("Rabat "))
rabat1=1-(rabat/100)
extra_pris=pris*rabat1
print("Du kommer att betala istallet", extra_pris, "kr")
