import random
import asyncio
from datetime import datetime
import time

# event types - order made, payment made, fraud check (auth)
ORDER: str = "order"
CREATED: str = "created"
CANCELLED: str = "cancelled"

PAY: str = "pay"
SUCCESS: str = "success"
FAIL: str = "fail"
AUTH: str = "auth"


EVENTS = [ORDER, PAY, AUTH]


def select_random(lst: list[str]) -> str:
    return random.choice(lst)


def generate_order() -> dict:
    """
    order types are as follows: created or cancelled
    """
    rand_choice = random.randint(-4, 100)
    if rand_choice < 0:
        # a negative price indicates a partial failure
        cost = -1
    else:
        f"${str(random.randint(5, 75))}"

    event = {
        "status": select_random([CREATED, CANCELLED]),
        "user_id": 123,
        "cost": cost,
        "timestamp": datetime.now(),
    }
    if random.random() < 0.5:
        event["coupon_code"] = "SAVE10"

    if random.random() < 0.3:
        event.pop("cost", None)

    return event


def generate_payment() -> dict:
    return {
        "viability": select_random([SUCCESS, FAIL]),
        "uid": 123,
        "price": random.randint(5, 123),
        "time": int(time.time()),
    }


def generate_auth() -> dict:
    return {
        "status": select_random([SUCCESS, FAIL]),
        select_random(["uid", "user_id", "customerId"]): 123,
        "amount": str(float(random.randint(5, 75))),
        "curr_time": datetime.now(),
    }


EVENTS_MAPPING = {
    ORDER: generate_order,
    PAY: generate_payment,
    AUTH: generate_auth,
}


async def generate_random_event():
    await asyncio.sleep(random.uniform(0.1, 5))
    curr_event = random.choices(EVENTS, k=1)
    return EVENTS_MAPPING[curr_event[0]]()
