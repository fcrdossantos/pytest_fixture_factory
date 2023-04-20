# Pytest Fixture Factory

Code to make it possible to create powerful and reusable fixture's factory to use in Pytest

# Motivation

Some cases we must have to create some custom model/object to be used on a lot of tests and re-use then in a safe way.

In those cases, just a Fixture isn't enough.

We do have some factories to pytest, but all (publicly available) of then needs Django and most of then use's Factoryboy in backend (with the need to connect to a model, not object)

This code can be used as a "vanilla" pytest implementation of a fixture-factory.

# How to use

Let's say you have and "User" object like this:

```python
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

```

You should import the factory decorator (`factory_fixture`) and the factory base class (`Factory`) both from `fixture_factory/factory.py`:

```python
from fixture_factory.factory import Factory, factory_fixture
```

Then, you need to create a sub-class of Factory, as it's an abstract class.

This class should implement `Setup`, `Create` and `Teardown` methods.

Finally, we must include the decorator on this class, with the optional parameter `fixture_name`.

The full could would be:

```python
from example.user import User
from fixture_factory.factory import Factory, factory_fixture

@factory_fixture(fixture_name="user")
class UserFactory(Factory):
  def setup(self):
    """ Your Setup Method"""
    self.count = 1
    self.users = [] # Think about this as a database

  def create(self, first_name=None, last_name=None, email=None):
    """Your Create Method"""

    # Default values
    if first_name is None:
        first_name = f"Felipe_{self.count}"
    if last_name is None:
        last_name = f"Cabrera_{self.count}"
    if email is None:
        email = f"felipe_{self.count}@bylearn.com.br"

    user = User(first_name, last_name, email)

    self.users.append(user) # Appending to the "database"
    self.count += 1

    return user

  def teardown(self):
    """Your Teardown (Cleanup) Method"""
    self.count = 1
    self.users = [] # Cleaning the "database"
```

# Methods

## Setup
Method where we can setup things to be used by the factory controller.

For example:
- Initiate the database connection
- Read some CSV file...

It's executed only once, before the first 'create' method call.

## Create
Method where we can create the object that we want to test.

Here we can set how the object will be created.

For example:
- This class should have "name" and "email" properties...

## Teardown
This is the 'cleanup' method.

Here we can set routines to be executed after we finish to use the factory.

For example:
- Remove inserted data from the database
- Close the database connection
- Remove the CSV file...

This method is executed only once, after the last 'create' method call.

# Running Tests

I left an working example on this repo, you can run it using:

```pytest tests```
