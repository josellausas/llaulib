from uuid import uuid4


class Lead:
    pass

class Customer:
    pass

class Website:
    pass

class Domain:
    pass

class Feature:
    pass

class Epic:
    pass

class Goal:
    def __init__(self, title) -> None:
        self.id = uuid4()
        self.title = title

class Initiative:
    def __init__(self, title, parent: Goal) -> None:
        self.id = uuid4()
        self.title = title
        self.parent = parent

class BusinessManager:
    def __init__(self) -> None:
        pass
