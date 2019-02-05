# Demo 3

## Lämpötila- ja kosteussensorin tehtävät

### Tehtävä 3.1: Sensori toimintakuntoon ja dataa ruutuun

- [ ] Sensori liitetty oikein raspiin ja sensorin lähettämää dataa saa kirjoitettua näyttöön *Palauta: Koodit ja yksi rivi näyttöön kirjoitettua dataa

### Tehtävä 3.2: Sensorin dataa Google Sheetsiin

- [ ] Datan saa lähetettyä Google Sheetsiin:
- [ ] OAuth:n tarvitsema Service Account Key -tiedosto (json) on raspilla.
- [ ] Palautuksessa vain selitys, kuinka JSON päätyi raspille ja sen client_email-kenttä, ei koko JSONia. Sen avulla kuka tahansa voi käyttää Drivessa jaettuja resursseja!
- [ ] Data päivittyy Sheetsiin
- [ ] Palauta koodit ja jaa Driven taulukko opettajaryhmälle tiea345kevat2019@googlegroups.com

## Kameran tehtävät

### Tehtävä 3.3: Raspin kameralla kuva ja videota

- [ ] Ota kuva ja 15 sekunnin video kameralla. Laita ainakin video muualle saataville ja linkki repoon
- [ ] Videon resoluution tulee olla pienempi kuin oletuksena oleva HD. Raportoi repoon, miten pienensit kokoa
- [ ] Palauta kuva, linkki videoon ja raportti, miten pienensit resoluutiota

### Tehtävä 3.4: Liikkeentunnistava kamera

- [ ] Tee liikkeentunnistava kamera, joka tallentaa kuvan, kun PIR havaitsee liikettä
- [ ] Palauta koodit.

### Tehtävä 3.5: Aseta kamera ottamaan kuva aina tasatunnein

- [ ] Aseta kamera ottamaan kuva aina tasatunnein

- [ ] Kuva otetaan kun kellonaika päättyy .00 (eikä tunnin kuluttua edellisen kuvan ottamisesta)
- [ ] Raspin uudelleen käynnistys ei saa haitata kuvien ottamista.
- [ ] -> Eli pelkkä Python-ohjelma ei riitä. Aseta Python käynnistymään uudelleen raspin käynnistyessä tai perehdy cron-ohjelmaan. Cronin käyttö erittäin suotavaa
- [ ] Palauta: Koodit, komennot ja config-tiedostojen muutokset

### Tehtävä 3.6: Toteuta web-palvelin, josta voi hakea uusimman tallennetun kuvan

- [ ] Toteuta web-palvelin, josta voi hakea uusimman tallennetun kuvan
- [ ] Palvelimen ei tarvitse olla saavutettavissa muualla kuin lähiverkossa
- [ ] Käyttää voi Apachea, Pythonia tai mitä työkalua haluaa.
- [ ] Palauta selostus, miten teit. Mukaanlukien komennot ja koodit.
