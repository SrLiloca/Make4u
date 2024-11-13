document.addEventListener("DOMContentLoaded", function () {
<<<<<<< HEAD
    const signupForm = document.getElementById("signup-form");
=======
    const signupForm = document.getElementById('signup-form');
>>>>>>> 85ac6157ab1e23eba03221561352181474c3f6f1
    
    // Verifica se o formulário foi encontrado
    if (!signupForm) {
        console.error("Formulário não encontrado!");
        return;
    }

    signupForm.addEventListener("submit", function (event) {
        event.preventDefault();

<<<<<<< HEAD
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
=======
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
>>>>>>> 85ac6157ab1e23eba03221561352181474c3f6f1

        if (!name || !email || !password) {
            alert("Todos os campos são obrigatórios.");
            return;
        }

        // Envia a requisição para o backend
<<<<<<< HEAD
        fetch('http://localhost:8000/users/signup', {
=======
        fetch('http://localhost:8000/signup', {
>>>>>>> 85ac6157ab1e23eba03221561352181474c3f6f1
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
<<<<<<< HEAD
                name: "Maria",
                email: "maria@example.com",
                password: "senha_segura"
            }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error("Erro:", error));
        
=======
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
>>>>>>> 85ac6157ab1e23eba03221561352181474c3f6f1
    });
});
