"""empty message

Revision ID: ed6882205b65
Revises: 4c5913c3c7b1
Create Date: 2019-02-25 02:40:29.719708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed6882205b65'
down_revision = '4c5913c3c7b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventorys', sa.Column('name', sa.String(length=250), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inventorys', 'name')
    # ### end Alembic commands ###
