const sqlite3 = require('sqlite3');
const { open } = require('sqlite');

async function initDatabase() {
    // Ouvre le fichier de base de données (il sera créé s'il n'existe pas)
    const db = await open({
        filename: './database.db',
        driver: sqlite3.Database
    });

    // Création des tables (le schéma complet qu'on a vu)
    await db.exec(`
        CREATE TABLE IF NOT EXISTS boards (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS threads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            board_id TEXT NOT NULL,
            last_bump TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (board_id) REFERENCES boards(id)
        );

        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            thread_id INTEGER NOT NULL,
            author TEXT DEFAULT 'Anonymous',
            content TEXT NOT NULL,
            image_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (thread_id) REFERENCES threads(id) ON DELETE CASCADE
        );
    `);

    // Insérer un board par défaut pour tester
    await db.run("INSERT OR IGNORE INTO boards (id, name) VALUES ('prog', 'Programmation')");

    console.log("Base de données initialisée et prête !");
    return db;
}

module.exports = { initDatabase };