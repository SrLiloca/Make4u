document.addEventListener('DOMContentLoaded', function () {
    const menuIcon = document.querySelector('.menu-icon');
    
    menuIcon.addEventListener('click', function () {
        alert('Menu clicado! Aqui você pode abrir uma navegação lateral ou redirecionar.');
    });

    const categoryBoxes = document.querySelectorAll('.category-box');

    categoryBoxes.forEach(box => {
        box.addEventListener('click', function () {
            alert(`Você clicou na categoria: ${this.querySelector('h2').textContent}`);
        });
    });
});

