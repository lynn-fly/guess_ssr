"""init_gift

Revision ID: a09c3ae41471
Revises: 9e2902d33df8
Create Date: 2022-09-04 12:04:23.027728

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'a09c3ae41471'
down_revision = '9e2902d33df8'
branch_labels = None
depends_on = None


def upgrade():
    user_table = table(
        'gift',
        column('id', sa.Integer),
        column('name', sa.String),
        column('allowance', sa.Integer),
        column('level', sa.Integer),
    )
    op.bulk_insert(
        user_table,
        [
            {
                "id": 1,
                "name": "户外座椅-灰",
                "allowance": 5,
                "level": 1,
            },
            {
                "id": 2,
                "name": "阿维塔定制保温杯",
                "allowance": 15,
                "level": 2,
            },
            {
                "id": 3,
                "name": "城市画展系列T恤衫-XL",
                "allowance": 15,
                "level": 3,
            },
            {
                "id": 4,
                "name": "户外超声波防潮野餐地垫-灰",
                "allowance": 15,
                "level": 3,
            },
            {
                "id": 5,
                "name": "户外折叠整理箱-灰",
                "allowance": 15,
                "level": 3,
            },
            {
                "id": 6,
                "name": "AVATR环保束口包",
                "allowance": 50,
                "level": 4,
            },
            {
                "id": 7,
                "name": "AVATR精品帆布包（含定制徽章）",
                "allowance": 100,
                "level": 4,
            },
            {
                "id": 8,
                "name": "杜邦电脑包",
                "allowance": 50,
                "level": 4,
            },
            {
                "id": 9,
                "name": "E值-66",
                "allowance": 1800,
                "level": 5,
            },
            {
                "id": 10,
                "name": "谢谢参与",
                "allowance": 9999,
                "level": 6,
            },
        ]
    )


def downgrade():
    pass
