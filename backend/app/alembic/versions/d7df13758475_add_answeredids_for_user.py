"""add answeredids for user

Revision ID: d7df13758475
Revises: 8e4d70e763e6
Create Date: 2022-09-06 16:14:13.742030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7df13758475'
down_revision = '8e4d70e763e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('answeredids', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'answeredids')
    # ### end Alembic commands ###
