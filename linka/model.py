from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class Link(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    original_link: Mapped[str] = mapped_column(String(255), unique=True)
    short_link: Mapped[str] = mapped_column(String(255), unique=True)
