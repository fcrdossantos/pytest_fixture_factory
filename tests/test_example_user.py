
from example.user import User

# We must explicitly import the Factory Fixture
# We can use 'from example.user_factory import UserFactory" or:
from example.user_factory import * # This avoid pylint errors!


# Note: the 'user' param is the fixture created at: example/user_factory.py
def test_creating_user(user):
    created_user = user.create("Felipe", "Cabrera", "felipe@bylearn.com.br")

    assert isinstance(created_user, User)
    assert created_user.first_name == "Felipe"
    assert created_user.last_name == "Cabrera"
    assert created_user.email == "felipe@bylearn.com.br"
    assert created_user.full_name() == "Felipe Cabrera"

def test_creating_users(user):
    # "Resetting" the factory. (In this case, reset the counter and "database")
    user.teardown()


    user1 = user.create()
    user2 = user.create()

    assert user1.first_name != user2.first_name
    assert user1.last_name != user2.last_name
    assert user1.email != user2.email
    assert user1.full_name() != user2.full_name()

    assert user1.first_name == "Felipe_1"
    assert user1.last_name == "Cabrera_1"
    assert user1.email == "felipe_1@bylearn.com.br"
    assert user1.full_name() == "Felipe_1 Cabrera_1"

    assert user2.first_name == "Felipe_2"
    assert user2.last_name == "Cabrera_2"
    assert user2.email == "felipe_2@bylearn.com.br"
    assert user2.full_name() == "Felipe_2 Cabrera_2"
