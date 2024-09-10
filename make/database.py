from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    category = Column(String)
    subcategory = Column(String)
    rating = Column(Float)
    review = Column(String)

engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def inserir_produto(dados_produto):
    produto = Produto(
        name=dados_produto["nome"],
        price=dados_produto["preco"],
        category=dados_produto["categoria"],
        subcategory=dados_produto["subcategoria"],
        rating=dados_produto["avaliacao"],
        review=dados_produto["review"]
    )
    session.add(produto)
    session.commit()

