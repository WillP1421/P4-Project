"""Added Relationships

Revision ID: a58f97f960bd
Revises: d96d51b5519a
Create Date: 2023-12-17 18:07:47.866685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a58f97f960bd'
down_revision = 'd96d51b5519a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_food', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_food', schema=None) as batch_op:
        batch_op.drop_column('price')

    # ### end Alembic commands ###