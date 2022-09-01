"""add upload file

Revision ID: 5560aa15faee
Revises: ad7473fecb48
Create Date: 2022-09-01 15:55:13.037762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5560aa15faee'
down_revision = 'ad7473fecb48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('upload_time', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'upload_time')
    # ### end Alembic commands ###
