"""empty message

Revision ID: 9e86adba0f09
Revises: 963c20aafe31
Create Date: 2020-03-16 16:02:30.426765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e86adba0f09'
down_revision = '963c20aafe31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_token',
    sa.Column('api_token_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('api_token_appid', sa.String(length=32), nullable=True),
    sa.Column('api_token_secretkey', sa.String(length=32), nullable=True),
    sa.Column('user_profile_id', sa.Integer(), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_profile_id'], ['user_profile.user_profile_id'], name=op.f('fk_api_token_user_profile_id_user_profile')),
    sa.PrimaryKeyConstraint('api_token_id', name=op.f('pk_api_token'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('api_token')
    # ### end Alembic commands ###