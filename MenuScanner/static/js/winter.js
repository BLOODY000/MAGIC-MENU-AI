// Функция для подбора еды
function showMood(mood) {
    const suggestions = {
        'happy': {title: 'Испанский чизкейк', desc: 'Для сладкого праздника!', link: '/desserts'},
        'sad': {title: 'Домашняя лапша', desc: 'Теплый уют в каждой ложке.', link: '/first_course'},
        'winter': {title: 'Шурпа с бараниной', desc: 'Лучший способ согреться зимой.', link: '/first_course'},
        'hungry': {title: 'Плов', desc: 'Сытно и мощно для большого аппетита!', link: '/second_course'}
    };

    const box = document.getElementById('mood-suggestion');
    document.getElementById('suggestion-title').innerText = "Рекомендуем: " + suggestions[mood].title;
    document.getElementById('suggestion-text').innerText = suggestions[mood].desc;
    document.getElementById('suggestion-link').href = suggestions[mood].link;

    box.style.display = 'block';
    box.style.animation = 'fadeIn 0.5s ease';
}

// Улучшенный снег
function createSnow() {
    const body = document.body;
    for (let i = 0; i < 40; i++) {
        let flake = document.createElement('div');
        flake.className = 'snowflake';
        flake.innerHTML = '❄';
        flake.style.cssText = `
            position: fixed;
            top: -10%;
            left: ${Math.random() * 100}vw;
            color: white;
            opacity: ${Math.random()};
            font-size: ${Math.random() * 20 + 10}px;
            z-index: 9999;
            pointer-events: none;
            animation: fall ${Math.random() * 5 + 5}s linear infinite;
        `;
        body.appendChild(flake);
    }
}

function openDish(name, imgUrl) {
    document.getElementById('modalImg').src = imgUrl;
    document.getElementById('modalCaption').innerText = name;
    document.getElementById('dishModal').style.display = 'flex';
}

window.onload = createSnow;