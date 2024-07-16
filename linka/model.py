from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class Link(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    original_link: Mapped[str] = mapped_column(unique=True)
    short_link: Mapped[str] = mapped_column(unique=True)
