import requests
from bs4 import BeautifulSoup
from models import Product, SessionLocal

def crawl_and_store_data():
    url = "URL_DO_SEU_SITE"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    db = SessionLocal()
    for product_html in soup.find_all('seletor_produto'):
        name = product_html.find('seletor_nome').text
        category = product_html.find('seletor_categoria').text
        subcategory = product_html.find('seletor_subcategoria').text
        price = float(product_html.find('seletor_preco').text.replace('R$', '').strip())
        description = product_html.find('seletor_descricao').text
        rating = float(product_html.find('seletor_avaliacao').text)
        review = product_html.find('seletor_comentario').text

        db_product = Product(
            name=name,
            category=category,
            subcategory=subcategory,
            price=price,
            description=description,
            rating=rating,
            review=review
        )
        db.add(db_product)
    db.commit()
