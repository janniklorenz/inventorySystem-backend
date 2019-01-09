"""empty message

Revision ID: 2afb1c764236
Revises: 
Create Date: 2019-01-06 15:47:44.097535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2afb1c764236'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('vendor', sa.String(length=250), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('street', sa.String(length=250), nullable=True),
    sa.Column('streetNumber', sa.String(length=10), nullable=True),
    sa.Column('city', sa.String(length=250), nullable=True),
    sa.Column('postCode', sa.String(length=250), nullable=True),
    sa.Column('latitude', sa.String(length=20), nullable=True),
    sa.Column('longitude', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=2500), nullable=True),
    sa.Column('creation_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('color', sa.String(length=7), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=50), nullable=False),
    sa.Column('lastName', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('has_tags',
    sa.Column('tagID', sa.Integer(), nullable=False),
    sa.Column('deviceID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['deviceID'], ['devices.id'], ),
    sa.ForeignKeyConstraint(['tagID'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('tagID', 'deviceID')
    )
    op.create_table('inventorys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deviceID', sa.Integer(), nullable=False),
    sa.Column('parent', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('description', sa.String(length=2500), nullable=True),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['deviceID'], ['devices.id'], ),
    sa.ForeignKeyConstraint(['parent'], ['inventorys.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('has_owner',
    sa.Column('inventoryID', sa.Integer(), nullable=False),
    sa.Column('ownerID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['inventoryID'], ['inventorys.id'], ),
    sa.ForeignKeyConstraint(['ownerID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('inventoryID', 'ownerID')
    )
    op.create_table('instances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inventoryID', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=2500), nullable=True),
    sa.ForeignKeyConstraint(['inventoryID'], ['inventorys.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instances')
    op.drop_table('has_owner')
    op.drop_table('inventorys')
    op.drop_table('has_tags')
    op.drop_table('users')
    op.drop_table('tags')
    op.drop_table('locations')
    op.drop_table('devices')
    # ### end Alembic commands ###
