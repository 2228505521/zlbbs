"""empty message

Revision ID: a84297b413b7
Revises: f8bac4577c6e
Create Date: 2018-06-12 21:15:53.087355

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a84297b413b7'
down_revision = 'f8bac4577c6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('front_user', 'gender')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('front_user', sa.Column('gender', mysql.ENUM('GenderEnum'), nullable=True))
    # ### end Alembic commands ###
