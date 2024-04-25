# Programsko rješenje Red Cat Mutlimedia zadatka.

Program se pokreće izvršavanjem `__main__` funkcije u _main.py_ datoteci. U `input/` direktoriju se nalaze dva primjera
ulaza koji su dostavljeni kao dodatak zadatku, a kako biste promijenili ulaz programa potrebno je promijeniti parametar
objekta "Driver" klase.

## Zadatak

Napravite program koji će za ulaz primiti 2D koordinate točaka A, B, C i X. Neka se koordinate učitavaju iz datoteke. Program treba:
1. provjeriti mogu li te tri točke biti vrhovi pravokutnika. Ukoliko ne mogu, program mora kontrolirano prestati s radom te obavijestiti korisnika o pogrešci,
2. provjeriti nalazi li se točka X unutar pravokutnika ABC te obavijestiti korisnika o rezultatu,
3. izračunati dijagonalu lika.

### Dodatak
• ovisno o točkama A, B i C, program treba prepoznati o kojoj se vrsti pravokutnika radi (pravokutnik ili kvadar) te za svoje izvršavanje treba dinamički odrediti koje će se klase ili funkcije pozvati
• proširite program da moze podržavati unos točaka A, B, C, D i X od kojih svaka ima po 3 dimenzije. Neka program provjerava mogu li točke A, B, C i D biti vrhovi jednog kvadra. Neka provjeri nalazi li se točka X unutar kvadra ABCD. Neka izračuna prostornu dijagonalu.
• napravite da program radi s arbitrarnim brojem dimenzija sve iz prethodnog zadatka

### Input / Output
Ulaz:
0, 0
5, 0
0, 5
2, 2
Izlaz:
True

Ulaz:
0, 0, 0
5, 0, 0
0, 3, 0
0, 0, 1
1, 1, 2
Izlaz:
False