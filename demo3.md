# Demo 3, yht. 10p

## Lämpötila- ja kosteussensorin tehtävät

### Tehtävä 3.1: Sensori toimintakuntoon ja dataa ruutuun,2p

- [x] Koodit `demo3 –> teht_3-1.py`
- [x] Rivi näyttöön kirjoitettua dataa

```bash
Temperature: 22.0 C    Humidity: 17.0 %
Temperature: 22.0 C    Humidity: 17.0 %
Temperature: 22.0 C    Humidity: 42.0 %
Temperature: 22.0 C    Humidity: 70.0 %
```

### Tehtävä 3.2: Sensorin dataa Google Sheetsiin, 2p

- [x] `client_email` -kenttä, `raspberry-pi@tiea345-demo3-232813.iam.gserviceaccount.com`
- [x] Koodit `demo3 –> teht_3-2.py`
- [x] Driven taulukko jaettu opettajaryhmälle tiea345kevat2019@googlegroups.com
- [x] Selitys, kuinka JSON päätyi raspille

1. Kirjaudu Google Developers -konsoliin
2. Luo projekti
3. Lue Service Account
4. Lataa Service Account Key JSON-muodossa
5. Siirrä json-tiedosto raspille käyttämällä `scp`-komentoa

## Kameran tehtävät

### Tehtävä 3.3: Raspin kameralla kuva ja videota, 1p

- [x] Kuva
- [x] [Linkki videoon](https://streamable.com/93u2n)
- [x] Raportti, miten resoluutiota pienennettiin

```python
camera.resolution = (720, 540)
```

### Tehtävä 3.4: Liikkeentunnistava kamera, 2p

- [x] Koodit `demo3 –> teht_3-4.py`

### Tehtävä 3.5: Aseta kamera ottamaan kuva aina tasatunnein, 2p

- [x] Koodit
- [x] Komennot ja config-tiedostojen muutokset

```bash
sudo apt-get install gnome-schedule
crontab -e
0 * * * * python3 /home/pi/code/TIEA345/demo3/teht_3-5.py
```

### Tehtävä 3.6: Toteuta web-palvelin, josta voi hakea uusimman tallennetun kuvan, 1p

- [ ] Selostus
- [ ] Komennot
- [ ] Koodit
