"""empty message

Revision ID: 3b4fa74ecad
Revises: 2afb44ff17b
Create Date: 2015-06-10 03:07:17.438247

"""

# revision identifiers, used by Alembic.
revision = '3b4fa74ecad'
down_revision = '2afb44ff17b'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_author_name'), 'author', ['name'], unique=False)
    op.create_table('publisher',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_publisher_name'), 'publisher', ['name'], unique=False)
    op.create_table('tag',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('value', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('podcast',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('language', sa.Enum('en', name='languages'), nullable=True),
    sa.Column('subtitle', sa.String(length=80), nullable=True),
    sa.Column('summary', sa.Text(), nullable=True),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('rights', sa.Text(), nullable=True),
    sa.Column('link', sa.String(length=2048), nullable=True),
    sa.Column('publisher_id', postgresql.UUID(), nullable=True),
    sa.Column('author_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['publisher_id'], ['publisher.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('display_name', sa.String(length=80), nullable=True),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.Column('author_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profile_display_name'), 'profile', ['display_name'], unique=True)
    op.create_index(op.f('ix_profile_email'), 'profile', ['email'], unique=True)
    op.create_index(op.f('ix_profile_first_name'), 'profile', ['first_name'], unique=False)
    op.create_index(op.f('ix_profile_last_name'), 'profile', ['last_name'], unique=False)
    op.create_index(op.f('ix_profile_username'), 'profile', ['username'], unique=True)
    op.create_table('image',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('href', sa.String(length=2048), nullable=True),
    sa.Column('podcast_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['podcast_id'], ['podcast.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('tag_id', postgresql.UUID(), nullable=True),
    sa.Column('podcast_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['podcast_id'], ['podcast.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    op.drop_table('base')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='base_pkey')
    )
    op.drop_table('tags')
    op.drop_table('image')
    op.drop_index(op.f('ix_profile_username'), table_name='profile')
    op.drop_index(op.f('ix_profile_last_name'), table_name='profile')
    op.drop_index(op.f('ix_profile_first_name'), table_name='profile')
    op.drop_index(op.f('ix_profile_email'), table_name='profile')
    op.drop_index(op.f('ix_profile_display_name'), table_name='profile')
    op.drop_table('profile')
    op.drop_table('podcast')
    op.drop_table('user')
    op.drop_table('tag')
    op.drop_index(op.f('ix_publisher_name'), table_name='publisher')
    op.drop_table('publisher')
    op.drop_index(op.f('ix_author_name'), table_name='author')
    op.drop_table('author')
    ### end Alembic commands ###
