import os
import math

# def handler(event, context):
#     response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
#     res = {
#         "event": event,
#         "output": response.json(),
#         "context": context
#     }
#     print(res)

#     return None


def func1(a, b) -> int:
    return math.floor(a + b)


def func2(a, b) -> str:
    return os.getcwd()
