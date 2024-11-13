document.getElementById('reviews-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const category = document.getElementById('category').value;
    const subcategory = document.getElementById('subcategory').value;
    const product_name = document.getElementById('product-name').value;
    const brand = document.getElementById('brand').value;
    const rating = document.getElementById('rating').value;
    const text = document.getElementById('text').value;

    fetch('/reviews/reviews', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            category: category,
            subcategory: subcategory,
            product_name: product_name,
            brand: brand,
            rating: rating,
            text: text
        })
    })
    .then(response => response.json())
    .then(data => {
        alert('Review criado com sucesso');
        window.location.href = '/reviews';
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao criar review');
    });
});
