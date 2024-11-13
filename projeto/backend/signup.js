document.getElementById('signup-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const email = document.getElementById('email').value;

    fetch('/users/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password,
            email: email
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Conta criada com sucesso!');
            window.location.href = '/login';  // Redireciona para a página de login
        } else {
            alert('Erro ao criar conta. Tente novamente.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ocorreu um erro. Tente novamente mais tarde.');
    });
});

// Redirecionar para a página de login ao clicar no link "Faça seu login"
document.getElementById('login.html').addEventListener('click', function(event) {
    event.preventDefault(); // Impede a navegação padrão
    window.location.href = "/login"; // Redireciona para a página de login
});