F = int(input(" Lütfen uygulayacağınız kuvveti newton cinsinden yazınız "))
S1= int(input(" Lütfen uygulanacak kuvvetin zemin alanını m² cinsinden yazın "))
m = int(input(" Lütfen cismin ağırlığıını kilogram cinsinden yazınız "))
S2= int(input(" Lütfen cismin koyulacak yerin alanını m² cinsinden yazınız "))
if F/S1 > m*10/S2 :
    print ( "cisim kaldırıldı")
else :
    print (" cisim kaldırılamadı")