# Proiect-Aplicatie-pentru-conversie-de-unitati-de-masura-
Descriere generală:

Convertor Universal Pro este o aplicație desktop realizată în Python, cu interfață grafică bazată pe Tkinter, care permite conversii rapide între diferite unități de măsură.
Aplicația suportă mai multe categorii de conversii și salvează automat istoricul operațiilor efectuate.

Funcționalități:

În această aplicație se poate face conversie intre unități de lungime, de greutate, de temperatură, de volum, de viteză, interfață grafică intuitivă, validare input utilizator, salvarea automată a istoricului conversiilor într-un fișier și structură modulară (logică, istoric, UI).

Structura proiectului:

project/
│
├── main.py        
├── history.log    
└── README.md

Cum rulezi aplicația:

Rulare:
1.Deschide un terminal în directorul proiectului.
2.Rulează comanda: "python main.py".
3.Se va deschide fereastra aplicației grafice.

Utilizare:
1.Selectează categoria.
2.Introdu valoarea numerică.
3.Alege unitatea inițială și unitatea finală.
4.Apasă CALCULEAZĂ.
5.Rezultatul apare pe ecran și este salvat în history.log.

Tratarea erorilor

Dacă valoarea introdusă nu este numerică, aplicația afișează un mesaj de eroare.
Separatorul zecimal acceptat: "." sau ",".
