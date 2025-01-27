"""empty message

Revision ID: e94cc1723102
Revises: 9d1ce39d9cb7
Create Date: 2021-05-11 20:22:04.278386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e94cc1723102'
down_revision = '9d1ce39d9cb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['goal_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###
