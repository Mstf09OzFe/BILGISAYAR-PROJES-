import math
y = int ( input ( " cismin hızını bulmak için 1 , aldığı yolu bulmak için 2 , geçen zamanı bulmak için 3 yazınız"))
if y < 2 :
    x = int ( input ( " lütfen alınan yolu giriniz " ) ) 
    t = int ( input ( " lütfen istediğiniz zamanı giriniz " ) )
    v =  x / t
    print ( v )
if  1<y<3 :
    t = int ( input ( " lütfen istediğiniz zamanı giriniz " ) )
    v = int ( input ( " lütfen cismin hızını giriniz " ) ) 
    x = v * t
    print ( x )
if y >= 3 :
    v = int ( input ( " lütfen cismin hızını giriniz " ) ) 
    x = int ( input ( " lütfen alınan yolu giriniz " ) ) 
    t = x / v
    print ( t )
