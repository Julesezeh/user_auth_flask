"""empty message

Revision ID: 266ce735e310
Revises: 
Create Date: 2023-09-24 10:40:16.897259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '266ce735e310'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
