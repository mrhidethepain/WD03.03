import sys
# a= 56
# print(a)
# print(type(a))
# b= 5.5
# print(b)
# print(type(b))
# zmienna_tekstowa = 'wizualizacja danych'
# print(zmienna_tekstowa)
# print(type(zmienna_tekstowa))
#
# x=6.55
# y=3
# z=x+y
# print(z)
# q=x-y
# print(q)
# e=y//x
# print(e)
# f=x//y
# print(f)
# g= x**2
# print(g)
# h=pow(x,2)
# print(h)
# i=6**(1/2)
# j=pow(6,1/2)
# print(i)
# print(j)
# k='wizaulizacja danych'
# l=' grupa '
# m=1
# print(k + l + str(m))
# print('liczba x jest rowna {:.2f}, liczba y jest rowna {:.3f}'.format(x,y))
#
# a1=input('Wprowadz liczbe: ')
# print(a1)
# print(type(a1))
# a1=int(a1)
# print(a1*5)
# print(type(a1))
# sys.stdout.write('Wprowadz liczbe: ')
# b1 = sys.stdin.readline()
# print (b1)
# print(type(b1))
#
# lista=[5,6.6,34,'a','b',[2,3,4],'ab']
# print(lista)
# lista.append(67)
# print(lista)
# lista.insert(2,'c')
# print(lista)
# lista.extend([20,21,22])
# print(lista)
# lista.pop()
# print(lista)
# lista.pop(2)
# print(lista)
# lista.remove([2,3,4])
# print(lista)
# del lista[1]
# print(lista)
# del lista
# lista=[6,34,2,5]
# lista.reverse()
# print(lista)
# lista.sort()
# print(lista)
#
# slownik={'klucz':'wartosc',1:2,'a':5,4:'b'}
# print(slownik)
# print(slownik[4])
# slownik[6]=45
# print (slownik)
# slownik.pop(1)
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# del slownik[6]
# a=8
# b=8
# if a>b:
#     print("a is greater than b")
# elif b<a:
#     print("b is greater than a")
# else:
#     print("a is equal to b")

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if(a>b)|(c>d):
#     print(a,c)
# else:
#     print(b,d)
# for i in range(1,8,2):
#     print(i)
# else:
#     print('koniec')
# for i in lista:
#     print(i)
# for i in range(0,5):
#     for j in range(0,5):
#         result=i+j
#         print(result)
#     print('')
# licznik=0
# while licznik<len(lista):
#     print(lista[licznik])
#     licznik+=1
# else:
#     print('koniec')
# while licznik!=10:
#     if licznik==7:
#         print(licznik)
#         break
#     else:
#         licznik+=1
# else:
#     print('licznik')

lista=[10,4,3,12,6,2,8,3,5]
sys.stdout.write('Wprowadz liczbe: ')
a = sys.stdin.readline()
a=int(a)
i=0
while i<len(lista):
    if a-int(lista[i])==0:
        print(i, lista[i])
        break
    else:
        i+=1
else:
    print('koniec, nie ma takiej liczby')

