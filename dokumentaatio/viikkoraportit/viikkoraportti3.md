# Viikko3
Viikon työaika ~10h

Tällä viikolla keskityin tekoälyn kehittämiseen, mutta en saanut sitä vielä täysin toimimaan. Olen rakentanut minimax-algoritmia käyttäen alpha-beta-karsintaa, mutta törmäsin ongelmiin erityisesti pelilaudan kopioinnin ja pelin tilan hallinnan kanssa. AI
pitäisi pystyä laskemaan optimaalisin siirto ja pelaamaan vastustajaa vastaan, mutta tällä hetkellä saan virheitä pelilaudan käsittelyn (list vs. Board-olio) ja tilan seuraamisen kanssa.

ai.py-tiedostossa AI yrittää tehdä päätöksiä minimax-algoritmin pohjalta, mutta tämä logiikka ei vielä toimi halutulla tavalla. Olen lisännyt heuristisen arvion, jonka avulla AI
pitäisi arvioida siirtojensa hyödyt, mutta sitä täytyy vielä hienosäätää. Pelin pääohjelmassa (connect4.py) pystyn edelleen asettamaan pelinappulat laudalle manuaalisesti, mutta AI
pelaaminen ei ole vielä toimivaa.

Testauksen kanssa en edennyt tällä viikolla, koska suurin osa ajastani meni AI
rakentamiseen. En saanut ratkaistua ongelmaa, jossa testit eivät löydä Board-luokkaa test_board.py-tiedostossa.

Seuraavaksi aion keskittyä minimax-algoritmin ja alpha-beta-karsinnan toimivuuden korjaamiseen, jotta AI pystyy pelaamaan peliä järkevästi. Lisäksi yritän ratkaista testien ongelmat ja varmistaa, että peli toimii odotetusti.