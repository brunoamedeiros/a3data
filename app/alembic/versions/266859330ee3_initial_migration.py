"""Initial migration

Revision ID: 266859330ee3
Revises: 
Create Date: 2024-06-03 07:16:40.409363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '266859330ee3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=False),
    sa.Column('deathdate', sa.Date(), nullable=True),
    sa.Column('ssn', sa.String(length=11), nullable=False),
    sa.Column('drivers', sa.String(length=15), nullable=True),
    sa.Column('passport', sa.String(length=20), nullable=True),
    sa.Column('prefix', sa.String(length=10), nullable=True),
    sa.Column('first', sa.String(length=50), nullable=False),
    sa.Column('middle', sa.String(length=50), nullable=True),
    sa.Column('last', sa.String(length=50), nullable=False),
    sa.Column('suffix', sa.String(length=10), nullable=True),
    sa.Column('maiden', sa.String(length=50), nullable=True),
    sa.Column('marital', sa.String(length=20), nullable=True),
    sa.Column('race', sa.String(length=20), nullable=False),
    sa.Column('ethnicity', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.String(length=1), nullable=False),
    sa.Column('birthplace', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('state', sa.String(length=255), nullable=False),
    sa.Column('county', sa.String(length=50), nullable=False),
    sa.Column('fips', sa.String(length=5), nullable=True),
    sa.Column('zip', sa.String(length=10), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lon', sa.Float(), nullable=False),
    sa.Column('healthcare_expenses', sa.Float(), nullable=False),
    sa.Column('healthcare_coverage', sa.Float(), nullable=False),
    sa.Column('income', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('passport'),
    sa.UniqueConstraint('ssn')
    )
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('patients')
    # ### end Alembic commands ###
