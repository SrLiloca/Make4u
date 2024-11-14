// Função para exibir/esconder o menu em dispositivos móveis
document.addEventListener('DOMContentLoaded', () => {
    const menuIcon = document.querySelector('.menu-icon');
    const navMenu = document.querySelector('nav ul');

    // Adiciona um evento de clique ao ícone do menu
    menuIcon.addEventListener('click', () => {
        navMenu.classList.toggle('show-menu');
    });

    // Evento de clique nos cartões de serviço
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach(card => {
        card.addEventListener('click', () => {
            const category = card.querySelector('h3').innerText.toLowerCase();
            window.location.href = `/categorias/${category}`; // Redireciona para a página da categoria correspondente
        });
    });
});

// Estiliza a exibição do menu em dispositivos móveis
document.addEventListener('DOMContentLoaded', () => {
    const style = document.createElement('style');
    style.innerHTML = `
        @media (max-width: 768px) {
            .menu-icon {
                display: block;
                cursor: pointer;
                font-size: 24px;
                margin-left: auto;
            }
            nav ul {
                display: none;
                flex-direction: column;
                background-color: #db9c9c;
                position: absolute;
                top: 50px;
                right: 20px;
                border-radius: 5px;
                width: 150px;
            }
            nav ul.show-menu {
                display: flex;
            }
            nav ul li {
                margin: 0;
                padding: 10px;
                text-align: right;
            }
        }
    `;
    document.head.appendChild(style);
});
