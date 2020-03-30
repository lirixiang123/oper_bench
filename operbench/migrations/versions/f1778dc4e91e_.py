"""empty message

Revision ID: f1778dc4e91e
Revises: d75ab610bf8d
Create Date: 2020-03-11 15:14:25.123351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1778dc4e91e'
down_revision = 'd75ab610bf8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asset', schema=None) as batch_op:
        batch_op.add_column(sa.Column('asset_hostname', sa.String(length=64), nullable=False))
        batch_op.add_column(sa.Column('asset_sn', sa.String(length=128), nullable=False))
        batch_op.create_unique_constraint(None, ['asset_sn'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asset', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('asset_sn')
        batch_op.drop_column('asset_hostname')

    # ### end Alembic commands ###