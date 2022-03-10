#   Examen LFA - exercitiul 2
#     Echipa:
# 1.Filote Petre Serban (grupa 144)
# 2.Contor Flavius Andrei (grupa 144)
# 3.Soare Cristian Alexandru (grupa 144)
#
# Note pentru configuration file pentru TM:
# 1. Fisierul trebuie numit "tm_config_file.txt"
# 2. Fisierul trebuie impartit in 7 parti, care incep cu un string specific urmat de "\n" si se termina cu "End":
#     + "States:" - in care vor fi introduse starile
#     + "Input alphabet:" - in care va fi introdus literele din alfabetul pentru TM, introduse cate 1 pe linie
#     + "Tape alphabet:" - in care va fi introdus literele din alfabetul pentru banda, introduse cate 1 pe linie
#     + "Transitions:" - in care vor fi introduse tranzitiile, cate 1 pe fiecare linie, fiecare element din tranzitie fiind delimitat de celelalte print ","
#     + "Start state:", "Accept state:", "Reject state:" - care vor contine o singura stare
# 3. In tranzitii, daca se doreste ca banda sa nu fie modificata la pozitia curenta, se va introduce simbolul "e"
# 4. Ordinea elementelor din tranzitii este urmatoare:
#     - starea actuala
#     - starea viitoare
#     - simbolul citit de primul head
#     - simbolul citit de al doilea head
#     - simbolul scris pe primul head
#     - simbolul scris pe al doilea head
#     - actiunea pentru primul head: "R" = move right, "L" = move left, "S" = stay
#     - actiunea pentru al doilea head: "R" = move right, "L" = move left, "S" = stay
# 5. Se pot introduce linii goale si spatii pentru indentare, fara caractere suplimentare
# 6. Simbolul blank este "_"



#Procesarea configuration file-ului
# f = open("adding_numbers.txt", "rt")
f = open("check_prefix.txt", "rt")
fisier = f.read()
f.close()

lista_linii = [x for x in fisier.split('\n')]

for i in range(len(lista_linii)):
    lista_linii[i] = lista_linii[i].strip()

states = list()
sigma = list()
gama = list()
transitions = list()
start_state = list()
accept_state = list()
reject_state = list()

#Organizarea corespunzatoare a elementelor din fisier
for i in range(len(lista_linii)):
    if lista_linii[i] == "States:":
        i += 1 #Se trece la linia urmatoarea dupa ce am citit deja una, analog si la urmatoarele if-uri
        while lista_linii[i] != "End":
            if lista_linii[i] != "": #Se adauga in lista cat timp linia citita este diferita de "End" si de stringul vid, analog si la urmatoarele if-uri
                states.append(lista_linii[i])
            i += 1
    if lista_linii[i] == "Input alphabet:":
        i += 1
        while lista_linii[i] != "End":
            if lista_linii[i] != "":
                sigma.append(lista_linii[i])
            i += 1
    if lista_linii[i] == "Tape alphabet:":
        i += 1
        while lista_linii[i] != "End":
            if lista_linii[i] != "":
                gama.append(lista_linii[i])
            i += 1
    if lista_linii[i] == "Transitions:":
        i += 1
        while lista_linii[i] != "End":
            if lista_linii[i] != '':
                transitions.append(lista_linii[i].split(','))
            i += 1
    if lista_linii[i] == "Start state:":
        i += 1
        while lista_linii[i] != "End":
            if lista_linii[i] != "":
                start_state.append(lista_linii[i])
            i += 1
    if lista_linii[i] == "Accept state:":
        i += 1
        while lista_linii[i] != "End":
            if lista_linii[i] != "":
                accept_state.append(lista_linii[i])
            i += 1
    if lista_linii[i] == "Reject state:":
        i += 1
        while lista_linii[i] != "End":
            if lista_linii[i] != "":
                reject_state.append(lista_linii[i])
            i += 1

states = set(states)
sigma = set(sigma)
gama = set(gama)
#Listele se fac multimi pentru a nu se repeta, din greseala, simbolurile.
#Nu se considera invalid input-ul daca se repeta acelasi simbol


ok = 1 #Se retine o variabila de tip bool pentru a nu verifica restrictiile daca deja input-ul este invalid
if len(start_state) > 1:
    ok = 0
else:
    start_state = start_state[0]

if len(accept_state) > 1 and ok != 0:
    ok = 0
else:
    accept_state = accept_state[0]

if len(reject_state) > 1 and ok != 0:
    ok = 0
else:
    reject_state = reject_state[0]
#Se verifica sa nu fie mai multe stari de inceput, acceptare sau respingere

if ok != 0:
    if start_state not in states:
        ok = 0
    if accept_state not in states:
        ok = 0
    if reject_state not in states:
        ok = 0
#Se verifica sa fie starile de start, acceptare si respingere in multimea starilor

if ok != 0:
    if accept_state == reject_state:
        ok = 0
#Se verifica sa fie starile de acceptare si respingere diferite

if ok != 0:
    if "_" in sigma:
        ok = 0
#Se verifica sa nu fie blank("_") in sigma

if ok != 0:
    for x in sigma:
        if x not in gama:
            ok = 0
            break
#Se verifica sa fie sigma in gama

if ok != 0:
    if "_" not in gama:
        ok = 0
#Se verifica sa fie simbolul blank ("_") in gama

if ok != 0:
    for linie in transitions:
        if len(linie) != 8: # Tranzitiile trebuie sa aiba exact 8 elemente
            ok = 0
        else:
            if linie[0] not in states or linie[1] not in states: # Se verifica starile din tranzitii sa fie si in multimea de stari
                ok = 0
                break
            if linie[2] not in gama or linie[3] not in gama: # Se verifica simbolurile din tranzitii sa fie si in alfabetul benzii
                ok = 0
                break
            if linie[4] not in gama and linie[4] != "e": # Se verifica simbolurile din tranzitii sa fie si in alfabetul benzii sau sa fie simbolul care nu schimba nimic ("e")
                ok = 0
                break
            if linie[5] not in gama and linie[5] != "e": # Se verifica simbolurile din tranzitii sa fie si in alfabetul benzii sau sa fie simbolul care nu schimba nimic ("e")
                ok = 0
                break
            if linie[6] not in {"L", "R", "S"} or linie[7] not in {"L", "R", "S"}: # Se verifica simbolurile pentru actiunile celor 2 capete sa fie corespunzatoare
                ok = 0
                break

if ok == 0:
    print("Invalid input")
else:
    print("Valid input")

#Simulator
if ok == 1: #ruleaza doar daca input-ul este valid
    tape = list(input("Tape input: "))
    for i in range(1000): #Se completeaza cu spatii la final-ul tape-ului - in mod normal o infinitate, din motive de memorie, am pus doar 1000, se poate mari totusi
        tape.append("_")
    for x in tape:
        if x not in gama: #Se verifica elementele introduse in tape sa fie si in gama
            ok = 0
            break
    head1 = 0
    head2 = 0
    actual_state = start_state
    while actual_state not in {accept_state, reject_state} and ok == 1: #While-ul ruleaza cat timp starea in care se afla TM-ul nu este de acceptare sau respingere, astfel, poate rula la infinit daca TM-ul este conceput astfel
        for i in range(len(transitions)):
            if actual_state == transitions[i][0] and transitions[i][2] == tape[head1] and transitions[i][3] == tape[head2]: #se verifica sa avem o tranzitie valabila pentru starea actuala si pentru cele 2 head-uri
                if transitions[i][4] != "e": #Se verifica sa nu fie simbolul care trebuie scris "e", caz in care nu se scrie nimic
                    tape[head1] = transitions[i][4]
                if transitions[i][5] != "e": #Se verifica sa nu fie simbolul care trebuie scris "e", caz in care nu se scrie nimic
                    tape[head2] = transitions[i][5]
                if transitions[i][6] == 'L':
                    if head1 != 0: #Se verifica sa nu fie head1 = 0, caz in care ramane pe loc
                        head1 -= 1 #Head1 se muta in stanga
                elif transitions[i][6] == 'R':
                    head1 += 1 #Head2 se muta in dreapta
                if transitions[i][7] == 'L':
                    if head2 != 0: #Se verifica sa nu fie head2 = 0, caz in care ramane pe loc
                        head2 -= 1 #Head2 se muta in stanga
                elif transitions[i][7] == 'R':
                    head2 += 1 #Head2 se muta in dreapta
                actual_state = transitions[i][1]
                break #Cand gaseste o tranzitie valabila, iese din for pentru ca am gandit un TM determinist

    if actual_state == accept_state: #Daca starea actuala, la finalul while-ului, este cea de acceptare, se afiseaza accepted
        print("Tape input accepted!\nOutput:")
        print(*tape)
    elif actual_state == reject_state: #altfel rejected
        print("Tape input rejected!")
    elif ok == 0:
        print("Tape input invalid!")
