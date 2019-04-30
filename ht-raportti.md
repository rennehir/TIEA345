# Automaattisesti päivittyvä infotelevisio

## Harjoitustyöraportti, TIEA345

## Tavoite

Harjoitustyön tavoitteena on rakentaa Raspberry PI:stä infotelevision ohjausyksikkö. Ajatuksena on, että televisiossa näytettävää sisältöä muokataan ulkopuolisessa sisällönhallintajärjestelmässä. Kyseinen sisällönhallintajärjestelmä ottaa yhteyden Raspberry PI:hin, kun uutta sisältöä on tarjolla, minkä jälkeen raspi päivittää selainnäkymän. Käynnistettäessä raspi hakee televisioon uusimman sisällön ja avaa selaimen näkyviin.

## Toteutus

### 1. Raspberry PI avaa valitun verkkosivun kioski-moodissa

`sudo nano ~/.config/lxsession/LXDE-pi/autostart`

```bash
@xset s off
@xset -dpms
@xset s noblank
@sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' ~/.config/chromium-browser Default/Prefere$
@chromium-browser --noerrdialogs --kiosk https://dumppitv.netlify.com/ --incognito --disable-translate
```

### 2. Käynnistyksen yhteydessä käynnistetään rajapinta

`crontab -e`

```bash
@reboot /usr/bin/sudo -u pi -H /usr/local/bin/forever start /home/pi/code/dumppitv-raspi/index.js
```

### 3. Rajapinnan koodi

`index.js`

```js
const shell = require("shelljs");
const express = require("express");
const internetAvailable = require("internet-available");
const forever = require("forever-monitor");

const PORT = process.env.PORT || 3000;

const app = express();

setTimeout(() => {
  internetAvailable()
    .then(() => {
      console.log("Internet available");
      try {
        forever.start(["/bin/bash", "-le", "serveo.sh"], {
          max: 10,
          silent: false
        });
      } catch (e) {
        console.log(e);
      }
    })
    .catch(e => {
      console.log("No internet");
      console.log(e);
    });
}, 60000);

app.get("/ping", (req, res) => {
  res.send("pong");
});

app.post("/refresh", (req, res) => {
  if (shell.exec("DISPLAY=:0 xdotool getactivewindow key F5").code !== 0) {
    shell.echo("Refresh command failed");
    shell.exit(1);
    res.status(500).send("Refresh command failed");
  } else {
    res.status(200).send("OK");
  }
});

app.listen(PORT, () => {
  console.log(`Server started on port: ${PORT}`);
});
```

`serveo.sh`

```bash
#!/bin/bash
ssh -R dumppitv:80:localhost:3000 serveo.net
```

Ylläoleva scripti välittää localhostista portin 3000 urliin https://dumppitv.serveo.net, jonka kautta APIa pystytään kutsumaan.

### 4. Webhook sisällönhallintajärjestelmästä

![Webhook DatoCMS:ssä](https://github.com/rennehir/TIEA345/raw/master/images/webhook.png)
