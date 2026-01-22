const form = document.getElementById('threadForm');
const container = document.getElementById('threads-container');

// 1. Charger les threads existants au démarrage
async function loadThreads() {
    const response = await fetch('http://localhost:3000/api/threads');
    const threads = await response.json();
    
    container.innerHTML = '';
    threads.forEach(t => {
        const div = document.createElement('div');
        div.className = 'thread';
        div.innerHTML = `
            <img src="http://localhost:3000${t.image_path}" alt="post image">
            <span class="author">${t.author}</span> 
            <span class="date">${new Date(t.last_bump).toLocaleString()}</span>
            <p>${t.content}</p>
        `;
        container.appendChild(div);
    });
}

// 2. Envoyer un nouveau thread
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData();
    formData.append('author', document.getElementById('author').value);
    formData.append('content', document.getElementById('content').value);
    formData.append('image', document.getElementById('image').files[0]);

    await fetch('/api/threads', {
        method: 'POST',
        body: formData
    });

    form.reset();
    loadThreads(); // Rafraîchir la liste
});

loadThreads();