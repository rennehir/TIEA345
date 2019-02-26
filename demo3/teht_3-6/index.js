const fs = require('fs')
const express = require('express')

const imagePath = '/home/pi/code/TIEA345/demo3/cronimages'

const app = express()

const getNewestFile = (files, path) => {
    const out = [];
    files.forEach(file => {
        const stats = fs.statSync(path + '/' + file);
        if(stats.isFile()) {
            out.push({'file':file, 'mtime': stats.mtime.getTime()});
        }
    });
    out.sort((a,b) => {
        return b.mtime - a.mtime;
    })
    return (out.length>0) ? out[0].file : '';
}

app.get('/latestImage', (req, res) => {
    fs.readdir(imagePath, function(err, files) {
        if (err) { throw err; }
        var audioFile = getNewestFile(files, imagePath).replace('.wav', '.mp3');
        //process audioFile here or pass it to a function...
        console.log(audioFile);
    });
})

app.listen(3000, () => {
    console.log('Listening on port 3000')
})
