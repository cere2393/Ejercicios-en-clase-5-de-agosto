nota1=int(input("ingrese nota1:"))
nota2=int(input("ingrese nota2:"))
nota3=int(input("ingrese nota3:"))
nota4=int(input("ingrese nota4:"))
media= ((nota1+nota2+nota3+nota4)/4)

if media>89 and media<101:
    print("A")
elif media>79 and media< 90:
    print("B")
elif media>69 and media< 80:
    print("C")
elif media>59 and media< 70:
    print("D")
else:
    print("E")

