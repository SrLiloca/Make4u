"""Initial migration

Revision ID: 0e734c115af7
Revises: 
Create Date: 2024-11-13 15:19:17.425435

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sys
sys.path.append('C:\\Users\\thali\\make')
from projeto.backend.database import Base


# revision identifiers, used by Alembic.
revision: str = '0e734c115af7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
