# Changelog

## Viikko 3

- Pelaajat voivat vuorotellen lisätä x:n tai o:n 3x3 -ruudukkoon hiiren avulla.
- Luotu luokka Grid, joka vastaa sovelluslogiikasta.
- Testattu, että x:n lisäys päivittää Grid luokan grid-muuttujaa oikein.

## Viikko 4

- Peli päättyy, kun voiton ehto täyttyy eli kun kolmesta saman pelaajan merkistä muodostuu katkeamaton suora.
- Peli päättyy niin, että voiton aiheuttava suora muuttuu punaiseksi ja siirtoja ei voi enää tehdä.
- Testattu hieman voiton tarkistavia funktioita ja unnormalize -funktiota.

## Viikko 5

- Tehty tuki vapaavalintaiselle ruudukkokoolle ja vapaavalintaiselle voittosuoran pituudelle.
- Oletuksena ruudukon koko on nyt 13 x 13 ja voittosuoran pituus on nyt 5.
- Voittoehdon tarkistavia funktioita on muutettu niin, että ne nyt hyödyntävät tietoa juuri lisätyn merkin sijainnista, ja testit on päivitetty tämän mukaan.
- Tehty lisää testejä voiton tarkistaville funktioille.
- Päivitetty sovelluksen rakennetta luomalla käyttöliittymäluokkia, joita hyödynnetään koodissa.

## Viikko 6

- Lisätty tuki myös kolmelle ja neljälle pelaajalle. Tämän voi valita muuttamalla ympäristömuuttujaa PLAYERS käynnistyksen yhteydessä.
- Tehty docstringejä.

## Viikko 7

- Lisätty toiminnallisuus pelin aloittamiseksi alusta painamalla F2-näppäintä.