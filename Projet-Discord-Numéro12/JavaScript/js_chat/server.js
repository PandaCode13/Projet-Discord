const net = require('net');
const { TextMessage } = require(__dirname + '/messages.js');

const PORT = 1234;
const clients = new Map();

const server = net.createServer((socket) => {
    let pseudo = "";
    let lastHeartbeat = Date.now();

    const hbCheck = setInterval(() => {
        if (Date.now() - lastHeartbeat > 15000) {
            console.log("Panne détectée.");
            socket.destroy();
            clearInterval(hbCheck);
        }
    }, 10000);

    socket.on('data', (data) => {
        try {
            const message = JSON.parse(data.toString());
            if (message.type === "HB") lastHeartbeat = Date.now();
            else if (message.type === "TEXT") {
                if (!pseudo) {
                    pseudo = message.msg;
                    clients.set(socket, pseudo);
                    console.log(`${pseudo} connecté.`);
                } else {
                    broadcast(JSON.stringify(new TextMessage(`${pseudo}: ${message.msg}`)), socket);
                }
            }
        } catch (e) {}
    });

    socket.on('close', () => { clearInterval(hbCheck); clients.delete(socket); });
});

function broadcast(data, sender) {
    clients.forEach((name, s) => { if (s !== sender) s.write(data); });
}

server.listen(PORT, () => console.log("Serveur OK sur port 1234"));