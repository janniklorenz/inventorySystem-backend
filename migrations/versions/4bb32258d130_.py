"""empty message

Revision ID: 4bb32258d130
Revises: 2afb1c764236
Create Date: 2019-01-06 15:52:07.292664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bb32258d130'
down_revision = '2afb1c764236'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('has_owner_ibfk_2', 'has_owner', type_='foreignkey')
    op.drop_constraint('has_owner_ibfk_1', 'has_owner', type_='foreignkey')
    op.create_foreign_key(None, 'has_owner', 'users', ['ownerID'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'has_owner', 'inventorys', ['inventoryID'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'has_owner', type_='foreignkey')
    op.drop_constraint(None, 'has_owner', type_='foreignkey')
    op.create_foreign_key('has_owner_ibfk_1', 'has_owner', 'inventorys', ['inventoryID'], ['id'])
    op.create_foreign_key('has_owner_ibfk_2', 'has_owner', 'users', ['ownerID'], ['id'])
    # ### end Alembic commands ###
