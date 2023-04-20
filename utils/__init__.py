import re

def class_to_snake_case(class_name: str):
    """Convert the class name (CamelCase) to snake_case.

    Credits: Inflection (pip install inflection)
    https://inflection.readthedocs.io/en/latest/_modules/inflection.html#underscore

    Args:
        class_name (str): name of the class

    Returns:
        str: value in snake_case
    """
    class_name = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', class_name)
    class_name = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', class_name)
    class_name = class_name.replace("-", "_")
    return class_name.lower()
