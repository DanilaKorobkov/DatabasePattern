class Person:

    def __init__(self):

        self.id: int = None
        self.company: str = None


class PersonGateway:

    def insert(self, person: Person):
        pass

    def update(self, person: Person):
        pass

    def delete(self, person: Person):
        pass

    def findById(self, id) -> Person:
        pass

    def findByCompany(self, company) -> iter:
        pass


