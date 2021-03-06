"""empty message

Revision ID: 4f2f41dbeee1
Revises: 9a0a49dc0bed
Create Date: 2019-02-25 03:51:17.847456

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4f2f41dbeee1'
down_revision = '9a0a49dc0bed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('inventorys', 'deviceID',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('inventorys', 'deviceID',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###
