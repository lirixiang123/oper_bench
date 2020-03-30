"""empty message

Revision ID: 64705b0e4c8b
Revises: 9e86adba0f09
Create Date: 2020-03-16 16:09:07.265291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64705b0e4c8b'
down_revision = '9e86adba0f09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_permission',
    sa.Column('api_permission_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('api_permission_url', sa.String(length=128), nullable=True),
    sa.Column('api_permission_method_type', sa.Enum('GET', 'POST', 'PUT', 'PATCH', 'DELETE', name='methodtype'), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('api_permission_id', name=op.f('pk_api_permission'))
    )
    op.create_table('api_token_permissions',
    sa.Column('api_token_id', sa.Integer(), nullable=True),
    sa.Column('api_permission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['api_permission_id'], ['api_permission.api_permission_id'], name=op.f('fk_api_token_permissions_api_permission_id_api_permission')),
    sa.ForeignKeyConstraint(['api_token_id'], ['api_token.api_token_id'], name=op.f('fk_api_token_permissions_api_token_id_api_token'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('api_token_permissions')
    op.drop_table('api_permission')
    # ### end Alembic commands ###