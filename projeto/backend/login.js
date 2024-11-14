document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById('login-form');

    if (!loginForm) {
        console.error("Formulário não encontrado!");
        return;
    }

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const emailElement = document.getElementById('email');
        const passwordElement = document.getElementById('password');

        if (!emailElement || !passwordElement) {
            console.error("Elemento de e-mail ou senha não encontrado!");
            return;
        }

        const email = emailElement.value;
        const password = passwordElement.value;

        console.log("E-mail:", email);
        console.log("Senha:", password);

        if (!email || !password) {
            alert("Todos os campos são obrigatórios.");
            return;
        }

        fetch('http://127.0.0.1:8000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        })
        .then(response => {
            console.log("Status da resposta:", response.status);
            return response.json();
        })
        .then(data => {
            console.log("Resposta do backend:", data);
            if (data.access_token) {
                console.log("Token de acesso recebido:", data.access_token);
                localStorage.setItem('access_token', data.access_token);
                window.location.href = '/home';
            } else {
                console.error("Token de acesso não recebido.");
                alert("Erro ao fazer login. Verifique suas credenciais.");
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert("Erro na requisição. Tente novamente mais tarde.");
        });
    });
});
