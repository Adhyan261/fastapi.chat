"""add posts table

Revision ID: 6c5c8413bdd7
Revises: 3a883ffdf91c
Create Date: 2022-04-01 14:30:13.492224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c5c8413bdd7'
down_revision = '3a883ffdf91c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content', sa.String(), nullable=False),
                    sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    )


def downgrade():
    op.drop_table('posts')
    pass
