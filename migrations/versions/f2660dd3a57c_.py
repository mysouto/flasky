"""empty message

Revision ID: f2660dd3a57c
Revises: 31ec3e73c359
Create Date: 2022-11-07 11:02:32.019511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2660dd3a57c'
down_revision = '31ec3e73c359'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cyclist',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cyclist')
    # ### end Alembic commands ###
