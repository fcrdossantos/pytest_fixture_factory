from typing import Union
from abc import ABC, abstractmethod

import pytest

from utils import class_to_snake_case

class Factory(ABC):
    @abstractmethod
    def setup(self, *args, **kwargs):
      """
      Method where we can setup things to be used by the factory controller.

      For example:
      - Initiate the database connection
      - Read some CSV file...

      It's executed only once, before the first 'create' method call.
      """

    @abstractmethod
    def create(self, *args, **kwargs):
      """
      Method where we can create the object that we want to test.

      Here we can set how the object will be created.

      For example:
      - This class should have "name" and "email" properties...
      """

    @abstractmethod
    def teardown(self, *args, **kwargs):
      """
      This is the 'cleanup' method.

      Here we can set routines to be executed after we finish to use the factory.

      For example:
      - Remove inserted data from the database
      - Close the database connection
      - Remove the CSV file...

      This method is executed only once, after the last 'create' method call.
      """

def factory_fixture(fixture_name: Union[str,None] = None):
  """
  Decorator that creates a fixture for a Factory class.

  Args:
      fixture_name (Union[str,None], optional): The name of our fixture.
      If you don't set anything (None), the value of the name will be the 'snake_cased' name of the class. Defaults to None.

      For example:
      - The class UserFactory will have the fixture name 'user_factory'
  """

  def _factory_fixture(factory_class):
    """
    Inner decorator function that creates the fixture.

    Should be used that way to allows us to use the 'fixture_name' variable.
    """

    # Check for fixture_name value. If none, then we use the 'snake_cased' name of the class.
    # Example: UserFactory -> user_factory
    nonlocal fixture_name
    if fixture_name is None:
        fixture_name = class_to_snake_case(factory_class.__name__)

    # Create the fixture
    @pytest.fixture(scope="session", name=fixture_name)
    def factory():

        # Check if the class is a subclass of Factory
        # So we can ensure the Setup/Create/Teardown methods are implemented
        assert issubclass(factory_class, Factory)

        factory_instance = factory_class()

        factory_instance.setup()

        # Returns (yields) the instance of the factory
        # So we should call it like this:
        # def test_something(user_factory):
        #     user = user_factory.create(params)
        yield factory_instance

        factory_instance.teardown()

    return factory

  return _factory_fixture
