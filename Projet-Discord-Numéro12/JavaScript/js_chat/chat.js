const net = require('net');
const readline = require('readline');

// --- CLASSES DE MESSAGES ---
class HBMessage {
    constructor() { this.type = "HB"; this.timestamp = new Date(); }
}
class TextMessage {
    constructor(msg = "") { this.type = "TEXT"; this.msg = msg; }
}

const PORT = 1234;

// --- LOGIQUE DU SERVEUR ---
function runServer() {
    const clients = new Map();
    const server = net.createServer((socket) => {
        let pseudo = "";
        let lastHB = Date.now();

        // Heartbeat Listener
        const check = setInterval(() => {
            if (Date.now() - lastHB > 15000) {
                console.log(`[PANNE] ${pseudo || 'Inconnu'} déconnecté.`);
                socket.destroy();
                clearInterval(check);
            }
        }, 10000);

        socket.on('data', (data) => {
            try {
                const msg = JSON.parse(data.toString());
                if (msg.type === "HB") lastHB = Date.now();
                else if (msg.type === "TEXT") {
                    if (!pseudo) {
                        pseudo = msg.msg;
                        clients.set(socket, pseudo);
                        console.log(`[LOGIN] ${pseudo} est là.`);
                    } else {
                        const out = JSON.stringify(new TextMessage(`${pseudo}: ${msg.msg}`));
                        clients.forEach((name, s) => { if (s !== socket) s.write(out); });
                    }
                }
            } catch (e) {}
        });

        socket.on('close', () => { clients.delete(socket); clearInterval(check); });
    });

    server.listen(PORT, () => console.log(`>>> SERVEUR DÉMARRÉ SUR LE PORT ${PORT} <<<`));
}

// --- LOGIQUE DU CLIENT ---
function runClient() {
    const client = net.createConnection({ port: PORT }, () => {
        console.log("Connecté au serveur.");
        const rl = readline.createInterface({ input: process.stdin });
        console.log("Entrez votre pseudo :");
        rl.on('line', (line) => {
            client.write(JSON.stringify(new TextMessage(line)));
        });
        setInterval(() => { if(!client.destroyed) client.write(JSON.stringify(new HBMessage())); }, 5000);
    });

    client.on('data', (data) => {
        const m = JSON.parse(data.toString());
        if (m.type === "TEXT") console.log(`\n${m.msg}`);
    });
}

// --- SÉLECTEUR ---
if (process.argv.includes('--server')) {
    runServer();
} else {
    runClient();
}