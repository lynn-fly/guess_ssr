"""add blue

Revision ID: 310c9f81adb8
Revises: d7df13758475
Create Date: 2022-09-07 14:40:25.661862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '310c9f81adb8'
down_revision = 'd7df13758475'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('upload_file_url', sa.String(length=128), nullable=True),
    sa.Column('upload_comment', sa.String(length=255), nullable=True),
    sa.Column('upload_time', sa.Integer(), nullable=True),
    sa.Column('thumbed', sa.Text(), nullable=True),
    sa.Column('thumbe_times', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blue')
    # ### end Alembic commands ###
