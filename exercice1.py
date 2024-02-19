import random

NOMBRE_MIN = 1
NOMBRE_MAX = 100
NB_QUESTIONS = 10

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0,1) 
            # 0->+ et 1->*
    operateur_str = "+"
  
    if o == 1:
        operateur_str = "*"
       

    reponse_str = input(f"Calculer: {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)

    calcul = a+b
    if o == 1:
        calcul = a*b

    if reponse_int == calcul:
        # print("Reponse correct")
        return True
    # else:
        # print("reponse incorrect")
    return False

nb_points = 0
for i in range(0, NB_QUESTIONS):
    print(f"Question n°{i+1} sur {NB_QUESTIONS} : ")
    if poser_question():
        print("Reponse correct")
        nb_points += 1
    else:
        print("Reponse incorrect")
    print()

# affichage de notes
print(f"Votre note est : {nb_points}/{NB_QUESTIONS}")

# appreciation
moyenne = NB_QUESTIONS/2
if nb_points == NB_QUESTIONS:
    print("Excelent !")
elif nb_points == 0:
    print("Reviser vos maths !")
elif nb_points > moyenne :
    print("Pas mal")
else:
    print("peut mieux faire")