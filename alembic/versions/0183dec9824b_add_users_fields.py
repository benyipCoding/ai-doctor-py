"""add mobile_phone and total_token_count to users

Revision ID: 0183dec9824b
Revises: 0182dec9823a
Create Date: 2026-02-01 00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0183dec9824b"
down_revision = "0182dec9823a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("mobile_phone", sa.String(length=20), nullable=True),
    )
    op.add_column(
        "users",
        sa.Column(
            "total_token_count",
            sa.Integer(),
            nullable=False,
            server_default="0",
        ),
    )
    op.create_index(
        op.f("ix_users_mobile_phone"), "users", ["mobile_phone"], unique=True
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_users_mobile_phone"), table_name="users")
    op.drop_column("users", "total_token_count")
    op.drop_column("users", "mobile_phone")
