from datetime import datetime
from collections import UserDict
import pickle

class Field:
    def __init__(self, value) -> None:
        self.value = value
   
    def __eq__(self, other):
        return self.value == other.value
    
    def __repr__(self) -> str:
        return self.value


class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: str):
        if value.isdigit():
            self._value = value

class Birthday(Field):
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value: str):
        if value:
            try:
                datetime.strptime(value, "%d.%m.%Y")
            except ValueError:
                print(f"You entered: {value}. Correct date format: DD.MM.YYYY")


class Record():
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        if phone:
            self.phones = [phone]
        else:
            self.phones = []
        if birthday:
            self.birthday = birthday
        else:
            self.birthday = ''
   
    def add_phone(self, phone):
        self.phones.append(phone)

    def dell_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
    
    def edit_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
            self.phones.append(input("Enter neu phone: "))

    def add_birthday(self, birthday):
        self.birthday = birthday

    def days_to_birthday(self):
        birthday_ = self.birthday.value.split('.')
        year_date = datetime.datetime.today().year if datetime.datetime.today().month < int(birthday_[1]) else datetime.datetime.today().year + 1
        birthday_date = datetime.date(year=int(year_date), month=int(birthday_[1]), day=int(birthday_[0]))
        now = datetime.datetime.today().date()
        day = birthday_date - now
        return abs(day.days)

    def __repr__(self) -> str:
        return f"User {self.name} Phones: {self.phones} Birthday: {self.birthday}"
    


class AddressBook(UserDict):
    current_value = 0

    def file_open(self):
        with open('book.bin', 'rb') as file_open:
            self.data = pickle.load(file_open)
        return self.data

    def file_write(self):
        with open('book.bin', 'wb') as file_write:
            pickle.dump(self.data, file_write)

    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def iterator(self, n=2):
        self.n = n  
        index = 0
        print_block = '-' * 50 + '\n'
        for record in self.data.values():
            index += 1
            if index < n:
                index += 1
                yield record.___repr___()
            else:
                index = 0
                yield '-' * 50 + '\n'
        yield '-' * 50 + '\n'
           
    def next(self, n=2):
        result = "List of all users:\n"
        print_list = self.iterator(n)
        for item in print_list:
            result += f"{item}"
        return result





    def search(self, data):
        result = ""
        for record in self.data.values():
            if str(data).lower() in str(record.name).lower() or str(data).lower() in str(phone):
                result += f"User {self.name} Phones: {self.phones} Birthday: {self.birthday}\n"
        return result


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    birthday = Birthday('27.05.1985')
    rec = Record(name, phone, birthday)
    ab = AddressBook()
    ab.add_record(rec)

   
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
        
    print('All Ok)')