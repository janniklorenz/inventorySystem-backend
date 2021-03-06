"""empty message

Revision ID: 390af3535dcb
Revises: 53c9f816694b
Create Date: 2019-01-06 16:00:38.330426

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '390af3535dcb'
down_revision = '53c9f816694b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('inventorys_ibfk_2', 'inventorys', type_='foreignkey')
    op.drop_column('inventorys', 'parent')
    op.drop_column('inventorys', 'count')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventorys', sa.Column('count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('inventorys', sa.Column('parent', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('inventorys_ibfk_2', 'inventorys', 'inventorys', ['parent'], ['id'])
    # ### end Alembic commands ###
