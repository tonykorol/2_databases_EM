from datetime import datetime
from sqlalchemy import String, DateTime, Integer
from sqlalchemy.orm import mapped_column, Mapped

from task_2.database.database import Base


class SpimexTradingResults(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    exchange_product_id: Mapped[int] = mapped_column()
    exchange_product_name: Mapped[str]
    oil_id: Mapped[str] = mapped_column(String(4))
    delivery_basis_id: Mapped[str] = mapped_column(String(3))
    delivery_basis_name: Mapped[str]
    delivery_type_id: Mapped[str] = mapped_column(String(1))
    volume: Mapped[int]
    total: Mapped[int]
    count: Mapped[int]
    date: Mapped[datetime]
    created_on: Mapped[datetime] = mapped_column(DateTime(default=datetime.now()))
    updated_on: Mapped[datetime]