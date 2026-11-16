"""Generate fake data from a regular Python script (not Django shell).

Install Faker with ``python -m pip install Faker``. Rename this file to
something other than ``faker.py`` (for example, ``generate_names.py``),
because a local file named ``faker.py`` shadows the installed package.
Run it from a terminal with ``python generate_names.py``.
"""

from faker import Faker


def main():
    name =[]
    fake = Faker()
    for _ in range(100):
        name.append(fake.name())

    i =0
    for i in range(5):
        print(name[i])
    

        


if __name__ == "__main__":
    main()