import math
y = int ( input ( " cismin hızını bulmak için 1 , aldığı yolu bulmak için 2 , geçen zamanı bulmak için 3 yazınız"))
if  y == 1 :
    x = int ( input ( " lütfen alınan yolu metre olarak giriniz  " ) ) 
    t = int ( input ( " lütfen istediğiniz zamanı saniye olarak giriniz " ) )
    v =  x / t
    print ( v )
if  y == 2 :
    t = int ( input ( " lütfen istediğiniz zamanı saniye olarak giriniz " ) )
    v = int ( input ( " lütfen cismin hızını m/s olarak giriniz " ) ) 
    x = v * t
    print ( x )
if  y == 3 :
    v = int ( input ( " lütfen cismin hızını m/s olarak giriniz " ) ) 
    x = int ( input ( " lütfen alınan yolu metre olarak giriniz " ) ) 
    t = x / v
    print ( t )  
