"""empty message

Revision ID: 72eb5aa0b7bb
Revises: dcccd0449d08
Create Date: 2021-02-25 05:45:34.728057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72eb5aa0b7bb'
down_revision = 'dcccd0449d08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('book_name', sa.String(length=100), nullable=True),
    sa.Column('publisher', sa.String(length=30), nullable=True),
    sa.Column('author', sa.String(length=30), nullable=True),
    sa.Column('publication_date', sa.DATE(), nullable=True),
    sa.Column('pages', sa.Integer(), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('link', sa.String(length=200), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('isbn', sa.BIGINT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###