class Pet:
    # Define class variables
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate that pet_type is one of the allowed types
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Append this instance to the class variable `all` that stores all Pet instances
        Pet.all.append(self)

        if owner:
            owner.add_pet(self)

   

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Ensure this is initialized as an empty list

    def pets(self):
        """Returns a list of all pets associated with the owner."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner after checking that it is of type Pet."""
        if not isinstance(pet, Pet):
            raise Exception("Argument must be an instance of Pet")
        
        pet.owner = self  # Set the owner of the pet to self (current owner)
        self._pets.append(pet)  # Add pet to owner's pets list

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)    

