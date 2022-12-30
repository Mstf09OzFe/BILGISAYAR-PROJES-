run = True
while run :
   m=int(input("lütfen cizmin ağırlığını kilogram cinsinden giriniz"))
   f=int(input("lütfenuygulanacak kuvveti newton cinsinden giriniz"))
   L=int(input("lütfen kadıracın uzunluğunu giriniz"))
   x=int(input("lütfen kaldıracın destek noktasının cisme uzaklığını giriniz"))
   if  f * (L-x) >= m * x * 10 :
        print("cisim kaldırıldı ✓✓✓✓")
   if  f * (L-x) < m * x * 10 :
        print("cisim kaldırılamadı  × × × × ")
