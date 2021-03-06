"""empty message

Revision ID: 0227b5cdd5ff
Revises: 5c2bfdfcec1a
Create Date: 2018-06-28 10:18:51.371704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0227b5cdd5ff'
down_revision = '5c2bfdfcec1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('board')
    # ### end Alembic commands ###
