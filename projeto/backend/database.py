from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

<<<<<<< HEAD
DATABASE_URL = "sqlite:///./test.db"  # Altere para sua URL de banco de dados, caso necessário
=======
DATABASE_URL = "sqlite:///./test.db"  
>>>>>>> 85ac6157ab1e23eba03221561352181474c3f6f1

# Criação do engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Necessário para SQLite

# Sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()
metadata = Base.metadata

# Função para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
