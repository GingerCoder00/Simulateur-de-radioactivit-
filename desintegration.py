from random import randint
import time

dé = 1000
lancé = 0

while dé>0:
    dest = 0
    lancé = lancé+1
    for i in range(dé):
        nbr = randint(1,6)
        if nbr == 6:
            dest = dest+1
    dé = dé-dest
    print(f"Le nombre de 6 est de : {dest}")
    print(f"Il reste {dé} dé(s)")
    print(f"Lancé suivant...")
    time.sleep(1)
print(f"Les 1000 dés ont été détruit en {lancé} lancé ")