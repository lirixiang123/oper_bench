"""empty message

Revision ID: d75ab610bf8d
Revises: 
Create Date: 2020-03-11 15:09:14.748839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd75ab610bf8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asset',
    sa.Column('asset_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('asset_type', sa.Enum('SERVER', 'NETWORK', 'MONITOR', name='assettype'), nullable=True),
    sa.PrimaryKeyConstraint('asset_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('asset')
    # ### end Alembic commands ###