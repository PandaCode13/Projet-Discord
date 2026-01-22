const net = require('net');
const readline = require('readline');
const { HBMessage, TextMessage } = require('./messages.js');

const client = net.createConnection({ port: 1234 }, () => {
    console.log("Connecté.");
    const rl = readline.createInterface({ input: process.stdin });
    rl.on('line', (line) => {
        client.write(JSON.stringify(new TextMessage(line)));
    });
    setInterval(() => { if(!client.destroyed) client.write(JSON.stringify(new HBMessage())); }, 5000);
});

client.on('data', (data) => {
    try {
        const m = JSON.parse(data.toString());
        if (m.type === "TEXT") console.log(m.msg);
    } catch (e) {}
});