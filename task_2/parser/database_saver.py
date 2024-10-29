from datetime import datetime

from sqlalchemy.orm import Session

from task_2.database.database import get_session
from task_2.database.models import SpimexTradingResults
from task_2.parser.data_classes import Product


def save_to_database(data: list[Product]) -> None:
    with get_session() as session:
        for item in data:
            add_new_product(item, session)
            session.commit()

def add_new_product(item: Product, session: Session) -> None:
    new_product = SpimexTradingResults(
        exchange_product_id=item.product_id,
        exchange_product_name=item.name,
        oil_id=item.product_id[:4],
        delivery_basis_id=item.product_id[4:7],
        delivery_basis_name=item.basis_name,
        delivery_type_id=item.product_id[-1],
        volume=item.volume,
        total=item.total,
        count=item.count,
        date=datetime.strptime(item.date, "%d.%m.%Y")
    )
    session.add(new_product)
