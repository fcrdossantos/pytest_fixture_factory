from example.user import User
from fixture_factory.factory import Factory, factory_fixture

# If you don't set the fixture_name, the name will be the 'snake_cased' name of the class.
# In this case, the fixture name would be named 'user_factory'
@factory_fixture(fixture_name="user")
class UserFactory(Factory):

  def setup(self):
    print("Setup")
    self.count = 1
    self.users = [] # Think about this as a database

  def create(self, first_name=None, last_name=None, email=None):
    print("Create")

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
    print("Teardown")
    self.count = 1
    self.users = [] # Cleaning the "database"
