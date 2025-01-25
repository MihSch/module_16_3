from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

#Create (POST): Создание новой записи.
# Метод POST отправляет данные на сервер для создания нового объекта.
#Read (GET): Получение данных.
# Метод GET используется для запроса информации,
# такой как получение списка всех задач или одной конкретной задачи.
#Update (PUT): Обновление данных.
# Метод PUT заменяет существующую запись на сервере на новую.
#Delete (DELETE): Удаление данных.
# Метод DELETE удаляет существующую запись.
users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/user')
async def get_user() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=3, max_length=15, description='Enter Username', example='Ivan')]
                 , age: Annotated[int, Path(ge=18, le=100, description='Enter age', example=30)]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered!'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int = Path(ge=1, le=5),
        username: str = Path(min_length=5, max_length=20, description='Enter Username'),
                    age: int = Path(ge=18, le=80, description='Enter Age')) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is updated"

@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=5)) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"
