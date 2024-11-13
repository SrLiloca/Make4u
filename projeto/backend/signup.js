document.addEventListener("DOMContentLoaded", function () {
    const signupForm = document.getElementById('signup-form');
    
    // Verifica se o formulário foi encontrado
    if (!signupForm) {
        console.error("Formulário não encontrado!");
        return;
    }

    signupForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        if (!name || !email || !password) {
            alert("Todos os campos são obrigatórios.");
            return;
        }

        // Envia a requisição para o backend
        fetch('http://localhost:8000/signup', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: name,
                email: email,
                password: password,
            }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro ao cadastrar usuário");
            }
            return response.json();  // Tenta obter o JSON
        })
        .then(data => {
            if (data.success) {
                alert("Cadastro realizado com sucesso!");
                window.location.href = "/login";  // Redireciona para a página de login
            } else {
                alert("Erro ao cadastrar. Tente novamente.");
            }
        })
        .catch(error => {
            console.error("Erro:", error);
            alert("Ocorreu um erro ao realizar o cadastro. Tente novamente mais tarde.");
        });
    });
});
