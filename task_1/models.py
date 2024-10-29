from datetime import datetime

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from task_1.database import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    price: Mapped[float]
    amount: Mapped[int]

    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="books")

    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"))
    genre: Mapped["Genre"] = relationship(back_populates="books")

    buy_books: Mapped[list["BuyBook"]] = relationship(back_populates="book")


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    books: Mapped[list["Book"]] = relationship(back_populates="author")


class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    books: Mapped[list["Book"]] = relationship(back_populates="genre")


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(String(254))

    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    city: Mapped["City"] = relationship(back_populates="clients")

    buys: Mapped[list["Buy"]] = relationship(back_populates="client")


class City(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    days_delivery: Mapped[int]

    clients: Mapped[list["Client"]] = relationship(back_populates="city")


class Buy(Base):
    __tablename__ = "buys"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text)

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    client: Mapped["Client"] = relationship(back_populates="buys")

    buy_books: Mapped[list["BuyBook"]] = relationship(back_populates="buy")

    buy_steps: Mapped[list["BuyStep"]] = relationship(back_populates="buy")


class Step(Base):
    __tablename__ = "steps"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    buy_steps: Mapped[list["BuyStep"]] = relationship(back_populates="step")


class BuyBook(Base):
    __tablename__ = "buy_books"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[int]

    buy_id: Mapped[int] = mapped_column(ForeignKey("buys.id"))
    buy: Mapped["Buy"] = relationship(back_populates="buy_books")

    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    book: Mapped["Book"] = relationship(back_populates="buy_books")


class BuyStep(Base):
    __tablename__ = "buy_steps"

    id: Mapped[int] = mapped_column(primary_key=True)
    date_step_beg: Mapped[datetime]
    date_step_end: Mapped[datetime]

    buy_id: Mapped[int] = mapped_column(ForeignKey("buys.id"))
    buy: Mapped["Buy"] = relationship(back_populates="buy_steps")

    step_id: Mapped[int] = mapped_column(ForeignKey("steps.id"))
    step: Mapped["Book"] = relationship(back_populates="buy_steps")
