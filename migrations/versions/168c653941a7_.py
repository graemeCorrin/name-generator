"""empty message

Revision ID: 168c653941a7
Revises: 0f2daa5d0ce3
Create Date: 2019-03-19 15:57:53.445938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '168c653941a7'
down_revision = '0f2daa5d0ce3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('surname', 'lan')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('surname', sa.Column('lan', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###