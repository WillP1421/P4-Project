"""updatd Order table for Quantity

Revision ID: 9b001f7a1e7d
Revises: 11e1d8ee3bb4
Create Date: 2023-12-21 19:55:15.175632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b001f7a1e7d'
down_revision = '11e1d8ee3bb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=True))
        batch_op.drop_column('total_price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_price', sa.INTEGER(), nullable=True))
        batch_op.drop_column('quantity')

    # ### end Alembic commands ###
