#viet ham tinh giai thua theo giai thuat de qui
def giai_thua(n):
    if n==1:
        return 1
    else:
        return (n*giai_thua(n-1))
number1 = 5
number2 = int(input('nhap so can tinh giai thua: '))
print('gia thua cua', number1, 'la:', giai_thua(number1))
print('gia tri cua', number2, 'la',giai_thua(number2))
