from data.data import PersonData, fake


def generate_person_data() -> PersonData:
    """
    Generate a PersonData object with random values.

    Returns:
        PersonData: The generated person data.
    """
    # Create an instance of the PersonData class
    person = PersonData()

    # Generate random values for each attribute of the person object
    person.name = fake.name()
    person.description = fake.email()

    # Return the generated person data
    return person
