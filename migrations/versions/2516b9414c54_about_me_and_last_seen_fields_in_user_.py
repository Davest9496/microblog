"""about me and last seen fields in user model

Revision ID: 2516b9414c54
Revises: 0da20be815f8
Create Date: 2024-08-02 17:40:10.848465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2516b9414c54'
down_revision = '0da20be815f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
