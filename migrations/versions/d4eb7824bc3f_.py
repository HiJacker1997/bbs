"""empty message

Revision ID: d4eb7824bc3f
Revises: 3cfd1d80367e
Create Date: 2018-04-07 16:18:09.293743

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd4eb7824bc3f'
down_revision = '3cfd1d80367e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('front_user', sa.Column('telephone', sa.String(length=11), nullable=False))
    op.drop_index('telephonr', table_name='front_user')
    op.create_unique_constraint(None, 'front_user', ['telephone'])
    op.drop_column('front_user', 'telephonr')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('front_user', sa.Column('telephonr', mysql.VARCHAR(length=11), nullable=False))
    op.drop_constraint(None, 'front_user', type_='unique')
    op.create_index('telephonr', 'front_user', ['telephonr'], unique=True)
    op.drop_column('front_user', 'telephone')
    # ### end Alembic commands ###
