"""empty message

Revision ID: 10ec2e769d32
Revises: ce2cf8e219db
Create Date: 2018-04-06 21:03:41.036601

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '10ec2e769d32'
down_revision = 'ce2cf8e219db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_role', sa.Column('name', sa.String(length=50), nullable=False))
    op.drop_column('cms_role', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cms_role', sa.Column('username', mysql.VARCHAR(length=50), nullable=False))
    op.drop_column('cms_role', 'name')
    # ### end Alembic commands ###
