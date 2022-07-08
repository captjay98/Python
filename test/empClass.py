class Employee:

    raise_amount = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@nigga.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)