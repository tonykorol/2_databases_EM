from datetime import datetime

from task_2.database.database import AsyncSession
from task_2.database.models import SpimexTradingResults
from task_2.parser.data_classes import Product


async def save_to_database(data: list[Product]) -> None:
    async with AsyncSession() as session:
        for item in data:
            new_product = SpimexTradingResults(
                exchange_product_id=item.exchange_product_id,
                exchange_product_name=item.exchange_product_name,
                oil_id=item.oil_id,
                delivery_basis_id=item.delivery_basis_id,
                delivery_basis_name=item.delivery_basis_name,
                delivery_type_id=item.delivery_type_id,
                volume=item.volume,
                total=item.total,
                count=item.count,
                date=item.date
            )
            session.add(new_product)
        await session.commit()
