"""empty message

Revision ID: e7ff087ac36c
Revises: 01f9d42a98c2
Create Date: 2018-04-06 22:00:42.886589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7ff087ac36c'
down_revision = '01f9d42a98c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'cms_user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cms_user', type_='unique')
    # ### end Alembic commands ###