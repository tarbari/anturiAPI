# AnturiAPI loppuraportti

## Resurssit ja datan rakenne

Annetun kuvauksen perusteella mielestäni oli selkeintä jakaa resurssit kolmeen eri luokkaan:

- Anturit
- Mittaukset
- Virheet

Pohdin suunnitteluvaiheessa pitäisikö lohkot olla myös oma resurssinsa, mutta mielestäni se olisi monimutkaistanut
projektia ilman, että se olisi tuonut mitään lisäarvoa. Esimerkkinä monimutkaistamisesta on se, että kun viimeinen
anturi poistetaan lohkosta, niin lohko täytyisi erikseen tuhota. Nykyisessä ratkaisussa lohkoja ei ole ollenkaan
olemassa ilman anturia, joten erillistä mekanismia tuhoamiselle ei tarvita.

Datan rakennetta suunnitellessani halusin, että tulevaisuudessa olisi mahdollisimman helppo lisätä eri tyyppisiä
antureita ja että mittaustulosten tyypit olisi helppo erotella toisistaan. Tämän vuoksi sensoreihin ja mittaustuloksiin
on lisätty arvo "type", jonka avulla järjestelmää voidaan laajentaa esimerkiksi mittaamaan ilmankosteutta. Tämä ajatus
ohjasi myös nimeämiskäytäntöjen määrittelyä.

Puutteena pitäisin sitä, että tietokannan toteutuksessa ei ole käytetty relaatioita. Esimerkiksi anturin nimi
mittaustuloksia lähetettäessä tarkistetaan käsin. Uskoisin, että tämän voisi hoitaa jotenkin fiksumminkin. Tämä on
toteutuksessa jätetty pois, sillä koin että tämä ei ole kurssin tavoitteiden kannalta olennaista.

---

## Polkujen suunnittelu

Polkujen suunnittelussa lähdin liikkeelle siitä, että käyttöliittymän toteuttajalla olisi mahdollisimman helppo
toteuttaa kuvauksessa mainitut ominaisuudet. Käytännössä kaikille määrittelyissä mainituille ominaisuuksille on oma
polku. Päätin jättää paluuarvot pois sellaisista poluista joita anturit käyttävät. Tämä sen vuoksi, että määrittelyssä
ei ole mainittu esimerkiksi mittausten aikaväliä. Kovin lyhyellä mittausvälillä ja suurella määrällä antureita saattaisi
verkon kapasiteetti tulla vastaan. En usko, että tämä todellisuudessa muodostuisi ongelmaksi tämän kaltaisen
järjestelmän kanssa, mutta yleisesti ottaen verkkoliikenteen määrä on hyvä ottaa suunnittelussa huomioon.

Ennalta annetusta määrittelystä poiketen lisäsin mahdollisuuden myös poistaa anturin tietokannasta. Uskon, että tästä on
hyötyä mikäli yksittäinen anturi esimerkiksi hajoaa korjauskelvottomaksi. Lisäksi tätä ajatellen voisi lisätä myös
mahdollisuuden poistaa tietyn anturin kaikki mittaustulokset tai mittaustulokset annetulla ajanjaksolla. Tämä auttaisi
tilanteissa, missä huomataan jonkin anturin antaneen selkeästi virheellisiä mittaustuloksia.

---

## Yhteenveto ja opit

Koen, että tämä toteutus mukailee hyvin läheisesti kurssilla esitettyjen esimerkkien ja tehtyjen harjoitusten mallia.
Käytännön koodaamisen kannalta suurinta päänvaivaa aiheutti pythonin moduulien tuominen eri osiin koodia. Päädyin
lopulta jättämään relatiiviset `from .routers.router_sensor import router` tyyliset importit pois ja käyttämään koko
polkuja tyyliin `from app.routers.router_sensor import router`. Muuten koodaamisen kannalta sain keskittyä vain
seuraamaan alussa luomaani suunnitelmaa. Suunnitteluvaihe oli erittäin hyödyllinen jäsentämään tehtävän
kokonaisuutta.

Mikäli nyt tekisin vastaavan projektin uudelleen lisäisin datan syöttämiseen syötteiden validointia, jotta
nimeämiskäytännöt pysyisivät määritellyn mukaisina. Lisäksi toteuttaisin moduulien tuonnit vielä tiukemmin. Tällä
hetkellä toteutuksessa on ylimääräisiä importteja, jotka näyttävät päällisin puolin tarpeellisilta, mutta oikeasti samat
moduulit saattaa tulla käyttöön muiden importtien kautta. Esimerkiksi `./app/routers/router_measurements.py`
tiedostossa `from sqlalchemy.orm import Session` on teknisesti ottaen tarpeeton sillä sama `Session` tulee myös
myöhemmin kohdassa `from app.db.crud_measurements import *`.

---

## Infoa tarkistusta varten

`database.db`:ssä on valmiiksi anturit `t000 - t004` ja lohkot `A00 - A03`. Lisäksi kaikilla antureilla on vähintäänkin
muutamia mittaustuloksia. Virhelokissa on myös muutamia virherivejä jo valmiiksi.