# Määrittelydokumentti
## Opinto-ohjelma
Tietojenkäsittelytieteen kandidaatti (TKT)
## Työn aihe
Connect4-peli
## Projektin ohjelmointikieli
Python
## Vertaisarviontikielet
Python, Javascript
## Projektissa käytettävät algorytmit ja tietorakenteet
Käytän projektissa Minimax ja Alfa-beta karsintaa, koska ne toimivat hyvin tämän tyyppisissä 1v1 peleissä. Projektin tavoitteena on kehittää tekoäly, joka valitsee parhaimman mahdollisen siirron aina omalla vuorollaan.
Minimax algorytmin avulla tekoäly pystyy laskemaan parhaimman mahdollisen siirron itselleen ja täten maksimoi voittomahdollisuuden. Minimax algorytmi käy läpi kaikki mahdolliset siirrot ja valitsee niistä parhaimman.
Alpha-beta karsinnalla pyritään nopeuttaa Minimax algorytmin toimintaa karsimalla läpi käytävien siirtojen määrää. Tällöin aikavaativuudeksi voidaan parhaimmillaan saada O(b^d) jossa b tarkoittaa haarautumista ja d tarkoittaa haun syvyyttä. Pelilautani tulee olemaan kooltaan 6x7 jolloin pelipuun syvyys on 42
## Syötteet
Ohjelmassa käytetään hiirtä valitsemaan liike graafiselta käyttöliittymältä.
## Kieli
Dokumentaation kielenä käytetään suomea.
## Lähteet
[Minimax wiki](https://en.wikipedia.org/wiki/Minimax)
[Alpha-beta pruning wiki](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
[AI Course Project Document: Artificial Intelligence-Based Connect 4 Player Using Python by: Abdalaziz Sawwan](https://cis.temple.edu/~pwang/5603-AI/Project/2021S/Sawwan/AI%20Project.pdf)
Kurssin moodlesivut 
