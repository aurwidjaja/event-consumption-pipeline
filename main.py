from event_simulator.services import generate_random_event
from queue.define import EventQueue
import asyncio
from attrs import define
from enum import Enum
from datetime import datetime


def normalize_time():
    pass


class EventType(Enum):
    ORDER_CREATED = "order_created"
    ORDER_CANCELLED = "order_cancelled"
    PAYMENT = "payment"
    AUTH = "auth"


class EventStatus(Enum):
    SUCCESS = "success"
    FAIL = "fail"
    PENDING = "pending"


@define(kw_only=True)
class Event:
    event_type: EventType
    status: EventStatus
    user_id: int
    amount: float
    timestamp: datetime


def consume(event: dict):
    """
    This fn should contain all sorts of logic around normalizing the events, currency associated that we're generating
    """
    breakpoint()
    status = normalize_status(event[status_key])
    time = normalize_time(event[time_key])
    price = normalize_price(event[price_key])
    user_id = normalize_user_id(event[user_id_key])
    price_status = get_price_status(price)
    return


async def main():
    while True:
        event_queue = EventQueue()
        rand_event = await generate_random_event()
        event_queue.push(rand_event)
        curr_event = event_queue.pop()
        consume(curr_event)


if __name__ == "__main__":
    asyncio.run(main())
