class parent:

    def __init(self, name, serial, **kwargs):
        self.name = name
        self.serial = serial

class ChildA(parent):

    def __init__(self, a_name, a_serial, **kwargs):
        self.a_name = a_name
        self.a_serial = a_serial
        super().__init__(**kwargs)

class ChildB(Parent):

    def __init__(self, b_name, b_serial, **kwargs):
        self.b_name = b_name
        self.b_serial = b_serial
        super().__init__(**kwargs)


class GrandChild(ChildA, ChildB):
    def __init__(self):
        super().__init__(name = "blah", a_name = "a blah", b_name = "b blah", a_serial = 99, b_serial = 99, serial = 30)
