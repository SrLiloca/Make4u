document.addEventListener("DOMContentLoaded", function () {
    const signupForm = document.getElementById("signup-form");
    
    // Verifica se o formulário foi encontrado
    if (!signupForm) {
        console.error("Formulário não encontrado!");
        return;
    }

    signupForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        if (!name || !email || !password) {
            alert("Todos os campos são obrigatórios.");
            return;
        }

        // Envia a requisição para o backend
        fetch('http://localhost:8000/users/signup', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: "Maria",
                email: "maria@example.com",
                password: "senha_segura"
            }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error("Erro:", error));
        
    });
});
