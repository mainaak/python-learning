class Student:
    # It is optional to mention the type
    def __init__(self, id: int, fname: str, lname: str, major: str, gpa: float, is_on_probation: bool):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def to_string(self):
        string_value = ('{\n\t"id": ' + str(self.id) +
                        '\n\t"fname": ' + self.fname +
                        '\n\t"lname": ' + self.lname +
                        '\n\t"major": ' + self.major +
                        '\n\t"gpa": ' + str(self.gpa) +
                        '\n\t"is_on_probation": ' + str(self.is_on_probation)
                        + "\n}"
                        )
        return string_value
