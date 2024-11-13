import sys
import os
from alembic.config import main as alembic_main

# Adicione o caminho do diretório do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'projeto')))

if __name__ == "__main__":
    alembic_main()
