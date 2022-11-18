v0=int(input("ilk hızı giriniz"))
t= int(input("girdiğiniz hızın 1/5'ini geçmeyecek bir saniye girirniz"))
g=10
if t>v0*1/5:
    print("daha küçük bir saniyr değeri yazın")
    t= int(input("girdiğiniz hızın 1/5'ini geçmeyecek bir saniye girirniz"))
h= v0 * t-(1/2)*g*t**2
print(h)