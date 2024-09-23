from fastapi import FastAPI

app = FastAPI()

USERS = {1: {
    'Имя': 'Example',
    'Возраст': 18
    }
}


@app.get('/users')
async def users_list():
    return USERS


@app.post('/user/{username}/{age}')
async def create_user(username, age):
    user_id = max(USERS.keys())+1
    USERS[user_id] = {username: age}
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int):
    if username:
        USERS[user_id]['Имя'] = username
    if age:
        USERS[int(user_id)]['Возраст'] = age
    return f'The user {user_id} is registered'


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    del USERS[user_id]


print(USERS)