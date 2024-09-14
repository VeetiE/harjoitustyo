# Viikko2
Viikon työaika ~10h

Aluksi tutustuin lisää minimax algorytmiin mutta jonkin aikaa pohdittuani en ihan vielä ymmärtänyt miten sitä lähtisi tekemään. Tämän saattamana päätin että aloitan sitten itse pelin koodaamisesta. Aloitin luomalla projektiin liittyviä tiedostoja kuten `board.py` sekä `connect4.py`. `board.py` tiedostoon loin luokan joka hallitsee pelilautaa eri methodien avulla.

Pelin pääohjelmana toimii `connect4.py` en saanut vielä toimivaa connect4 peli valmiiksi. Peliä ei voi tällä hetkellä voittaa mitenkään mutta pelinappuloiden asettaminen laudalle onnistuu.

`board.py` tiedostoon loin Board luokan, joka alustaa laudan sekä päivittää sitä. Loin myös function joka tarkistaa onko voittoa tullut. Tämä functio ei kuitenkaan vielä toimi.

Loin myös unittestejä `board.py` kansiolle mutta en saanut niitäkään toimimaan koska `test_board.py` tiedosto ei löydä Board luokkaa vaikka kuinka yritin importata sitä.

Seuraavalla viikolla yritän saada testauksen toimimaan sekä pelin toimimaan halutulla tavalla. Yritän myös saada AI vastuksen toimimaan.

Minulla on jonkin verran vaikeuksia minimax algorytmin pseudokoodin ymmärtämisessä, jonka takia en päässytkään sitä toteuttamaan vielä tällä viikolla. Jos on jotain vinkkejä antaa nii olisin kiitollinen.