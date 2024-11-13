from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from projeto.backend.database import Base  
from projeto.backend.models import *
import sys
import os

# Essa configuração carrega as variáveis de configuração do arquivo alembic.ini
config = context.config
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:\\Users\\thali\\make\\projeto'))
sys.path.append(project_root)


# Configuração de logs
fileConfig(config.config_file_name)

# Defina a `target_metadata` para os modelos que precisam de migrações
target_metadata = Base.metadata

def run_migrations_offline():
    """Executa as migrações em modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Executa as migrações em modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
