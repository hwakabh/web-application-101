from uuid import uuid4


def generate_uuid() -> str:
    return str(uuid4())


random_uuid = generate_uuid()
print(random_uuid)
