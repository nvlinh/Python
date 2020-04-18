class Dog:
    """Model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.age = age
        self.name = name

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is sit.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name} is roll over.")


your_dog = Dog('Mundo', 1)
print(f"\nMy dog is {your_dog.name}")
print(f"{your_dog.name}'s {your_dog.age} year old")
your_dog.sit()

your_dog = Dog('Bun', 3)
print(f"\nYour dog is {your_dog.name}")
print(f"{your_dog.name}'s {your_dog.age} year old")
your_dog.roll_over()