"""empty message

Revision ID: d9ea698464e3
Revises: a791ec1ae587
Create Date: 2020-03-25 09:35:45.390678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9ea698464e3'
down_revision = 'a791ec1ae587'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasklog',
    sa.Column('tasklog_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('tasklog_tid', sa.String(length=64), nullable=True),
    sa.Column('tasklog_result', sa.Text(), nullable=True),
    sa.Column('tasklog_create_time', sa.DateTime(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.task_id'], name=op.f('fk_tasklog_task_id_tasks')),
    sa.ForeignKeyConstraint(['user'], ['user_profile.user_profile_id'], name=op.f('fk_tasklog_user_user_profile')),
    sa.PrimaryKeyConstraint('tasklog_id', name=op.f('pk_tasklog'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasklog')
    # ### end Alembic commands ###
