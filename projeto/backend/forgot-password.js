document.getElementById('forgot-password-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const email = document.getElementById('email').value;

    fetch('/users/forgot-password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Instruções de recuperação de senha enviadas para seu e-mail.');
            window.location.href = '/login';
        } else {
            alert('Erro ao enviar instruções. Tente novamente.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ocorreu um erro. Tente novamente mais tarde.');
    });
});
