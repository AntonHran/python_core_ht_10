from collections import UserDict, UserList


class Record:
    def __init__(self, name=None, phone=None, email=None):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.email = Email(email)
        self.check(phone)

    def add_number(self, phone):
        self.phone.append(phone)

    def delete_number(self, phone_num):
        self.phone.remove(phone_num)

    def change_number(self, old_phone_num, changed_phone_num):
        ind = self.phone.index(old_phone_num)
        self.phone.remove(old_phone_num)
        self.phone.insert(ind, changed_phone_num)

    def add_change_email(self, email_val):
        self.email = Email(email_val)

    def check(self, arg):
        if not arg:
            self.phone.remove(None)


class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    pass


class Phone(Field, UserList):
    def __init__(self, value):
        Field.__init__(self)
        UserList.__init__(self)
        self.data.append(value)


class Email(Field):
    pass


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def __str__(self):
        return [f'Name: {name} -> Info: telephone number(-s): {rec.phone} | Email: {rec.email.value}.'
                for name, rec in self.data.items()]


contacts = AddressBook()
record1 = Record('name1')
contacts.add_record(record1)
print(*contacts.__str__(), '\n')

record1.add_number('111')

record2 = Record('name2')
record2.add_number('222')
# contacts.add_record(record1) !!!
contacts.add_record(record2)
print(*contacts.__str__(), '\n')

record1.add_number(1111)
record2.add_change_email('some_email')
print(*contacts.__str__(), '\n')

print(contacts['name1'].phone)
contacts['name2'].add_number(333)
print(*contacts.__str__(), '\n')

contacts.add_record(Record('name3', 3131, 'another_email'))
print(*contacts.__str__(), '\n')
print(contacts['name3'].email.value)
contacts['name2'].change_number('222', 2121)
print(*contacts.__str__())

contacts['name3'].add_change_email('@')
print(contacts['name3'].email.value)
print(*contacts.__str__())
