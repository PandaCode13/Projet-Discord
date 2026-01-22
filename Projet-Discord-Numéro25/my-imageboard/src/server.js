const express = require('express');
const cors = require('cors');
const multer = require('multer');
const path = require('path');
const { initDatabase } = require('./database');

const app = express();
const PORT = 3000;

// Configuration du stockage des images
const storage = multer.diskStorage({
    destination: './uploads/',
    filename: (req, file, cb) => {
        cb(null, Date.now() + path.extname(file.originalname)); // Nom unique : timestamp + extension
    }
});
const upload = multer({ storage: storage });

// Middlewares
app.use(cors());
app.use(express.json());
app.use('/uploads', express.static('uploads')); // Rend le dossier uploads accessible via URL
app.use(express.static('public')); // Pour servir ton futur Frontend

// Variable pour stocker la connexion DB
let db;

// --- ROUTES API ---

// 1. Récupérer tous les messages d'un board
app.get('/api/threads', async (req, res) => {
    const threads = await db.all(`
        SELECT threads.*, posts.content, posts.image_path, posts.author 
        FROM threads 
        JOIN posts ON threads.id = posts.thread_id 
        WHERE posts.id = (SELECT MIN(id) FROM posts WHERE thread_id = threads.id)
        ORDER BY last_bump DESC
    `);
    res.json(threads);
});

// 2. Créer un nouveau thread (Sujet + Image + Message)
app.post('/api/threads', upload.single('image'), async (req, res) => {
    const { content, author } = req.body;
    const imagePath = req.file ? `/uploads/${req.file.filename}` : null;

    // Créer le thread
    const result = await db.run('INSERT INTO threads (board_id) VALUES (?)', ['prog']);
    const threadId = result.lastID;

    // Créer le premier post (OP)
    await db.run(
        'INSERT INTO posts (thread_id, author, content, image_path) VALUES (?, ?, ?, ?)',
        [threadId, author || 'Anonymous', content, imagePath]
    );

    res.status(201).json({ message: "Thread créé !", threadId });
});

// Lancement du serveur et de la DB
initDatabase().then(database => {
    db = database;
    app.listen(PORT, () => {
        console.log(`✅ Serveur lancé sur http://localhost:${PORT}`);
    });
});