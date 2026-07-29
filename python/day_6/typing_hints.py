from typing import Any, Callable

def greet(name:str, age:int):
    print(f"My name is {name} and age {age}")
greet("bhupendra", 23)

def process_user_data(
        user_id: int,
        config: dict[str, Any],
        callback: Callable[[int], bool],
        nickname: str | None = None
        )->dict[str,str]:
    return {"status": "success"}

print(process_user_data(1, {"hello":"1"}, [2,3]))

