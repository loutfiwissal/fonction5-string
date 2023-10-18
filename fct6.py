A=str(input("entre une chaine de caractere: "))
B=A[::-1]
if B==A:
    print("c'est une chaine palindrome" )
else:
    print("non palindrome")