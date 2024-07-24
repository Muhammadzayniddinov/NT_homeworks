### 1 ###

# import datetime
# from abc import abstractmethod,ABC

# class RoomAbc(ABC):
#     @abstractmethod
#     def is_available(self, check_in, check_out):
#         pass

#     @abstractmethod
#     def add_booking(self, booking):
#         pass

#     @abstractmethod
#     def remove_booking(self, booking):
#         pass

# class BookingAbc(ABC):
#     @abstractmethod
#     def send_confirmation(self):
#         pass

# class GuestAbc(ABC):
#     @abstractmethod
#     def make_booking(self, room, check_in, check_out):
#         pass

#     @abstractmethod
#     def cancel_booking(self, booking):
#         pass

# class HotelAbc(ABC):
#     @abstractmethod
#     def add_room(self, room):
#         pass

#     @abstractmethod
#     def add_guest(self, guest):
#         pass

#     @abstractmethod
#     def find_room_by_number(self, room_number):
#         pass

#     @abstractmethod
#     def find_guest_by_name(self, name):
#         pass



# class Room(RoomAbc):
#     def __init__(self, room_number, room_type, price_per_night):
#         self.room_number = room_number
#         self.room_type = room_type
#         self.price_per_night = price_per_night
#         self.bookings = []

#     def is_available(self, check_in, check_out):
#         for booking in self.bookings:
#             if booking.check_in <= check_out and booking.check_out >= check_in:
#                 return False
#         return True

#     def add_booking(self, booking):
#         self.bookings.append(booking)

#     def remove_booking(self, booking):
#         if booking in self.bookings:
#             self.bookings.remove(booking)

# class Booking(BookingAbc):
#     def __init__(self, guest, room: Room, check_in, check_out):
#         self.guest = guest
#         self.room = room
#         self.check_in = check_in
#         self.check_out = check_out

#     @property
#     def account_total_cost(self):
#         nights = (self.check_out - self.check_in).days
#         return nights * self.room.price_per_night

#     def send_confirmation(self):
#         total_cost = self.account_total_cost
#         print(f"Buyurtmani tasdiqlash: {self.guest.name} uchun {self.room.room_number} - {self.check_in} dan {self.check_out} gacha. Umumiy xarajat: ${total_cost}")

# class Guest(GuestAbc):
#     def __init__(self, name, email, bookings=None):
#         if bookings is None:
#             bookings = []
#         self.name = name
#         self.email = email
#         self.bookings = bookings

#     def make_booking(self, room, check_in, check_out):
#         if room.is_available(check_in, check_out):
#             booking = Booking(guest=self, room=room, check_in=check_in, check_out=check_out)
#             room.add_booking(booking)
#             self.bookings.append(booking)
#             booking.send_confirmation()
#         else:
#             print(f"Uzr, {room.room_number} raqamidagi xona {check_in} dan {check_out} gacha mavjud emas.")

#     def cancel_booking(self, booking):
#         if booking in self.bookings:
#             self.bookings.remove(booking)
#             booking.room.remove_booking(booking)
#             print(f"{booking.room.room_number} raqamodagi xona {booking.check_in} dan {booking.check_out} gacha bron qilingani bekor qilindi.")
#         else:
#             print(f"Bunday bron mavjud emas.")

# class Hotel(HotelAbc):
#     def __init__(self):
#         self.rooms = []
#         self.guests = []

#     def add_room(self, room):
#         self.rooms.append(room)

#     def add_guest(self, guest):
#         self.guests.append(guest)

#     def find_room_by_number(self, room_number):
#         for room in self.rooms:
#             if room.room_number == room_number:
#                 return room
#         return None

#     def find_guest_by_name(self, name):
#         for guest in self.guests:
#             if guest.name == name:
#                 return guest
#         return None


# hotel = Hotel()

# room1 = Room("101", "Single", 100)
# room2 = Room("102", "Double", 150)
# hotel.add_room(room1)
# hotel.add_room(room2)

# guest1 = Guest("Z M", "S@email.com")
# guest2 = Guest("S Z", "m@gmail.com")
# hotel.add_guest(guest1)
# hotel.add_guest(guest2)

# guest1.make_booking(room1, datetime.date(2024, 7, 15), datetime.date(2024, 7, 18))
# guest2.make_booking(room2, datetime.date(2024, 7, 20), datetime.date(2024, 7, 25))

# print("Room availability:")
# print(f"Room 101 available? {room1.is_available(datetime.date(2024, 7, 19), datetime.date(2024, 7, 22))}")
# example_booking = guest1.bookings[0]
# print(f"Total cost for booking: ${example_booking.account_total_cost}")
# print(f"Room 102 available? {room2.is_available(datetime.date(2024, 7, 19), datetime.date(2024, 7, 22))}")


# guest1.cancel_booking(example_booking)




####################


#### 2 ###
class BankAccount:
  def __init__(self, owner: str, balance: int):
    self.owner = owner
    self.__balance = balance
  
  @property
  def get_balance(self):
    return self.__balance
  


  def deposit(self, account, amount: float):
    if amount > 0:
      account.withdraw(amount)
      self.__balance += amount
    else:
      print('Deposit musbat bolishi kerak')
    
  
  def withdraw(self, amount: float):
    if 0 < amount <= self.__balance:
      self.__balance -= amount
    else:
      raise ValueError('Withdraw lik uchun yetarlicha mablag yoq')

account1 = BankAccount('M', 2000)
account2 = BankAccount('S', 2000)
print(f'{account1.owner}: {account1.get_balance}$')
print(f'{account2.owner}: {account1.get_balance}$')
account2.deposit(account1,200)
print(account2.get_balance)
account1.withdraw(500)
print(account1.get_balance)

print(f'{account1.owner}: {account1.get_balance}$')
print(f'{account2.owner}: {account1.get_balance}$')

###########################3


### 3 ###

# class User:
#   def __init__(self, name: str, age: int, email: str):
#     self.name = name
#     self.age = age
#     self.email = email
  

    

#   @property
#   def age(self):
#     return self._phone
  
#   @age.setter
#   def age(self, value):
#     if not value.isdigit():
#       raise TypeError('Yoshingizni togri formatda kiriting')
#     if len(value) > 3:
#       raise ValueError('Yoshingizni togri kiriting:') 
#     else:
#       self._phone = value




    
#   @property
#   def email(self):
#       return self._email

#   @email.setter
#   def email(self, value):
#       if '@mail' in value or '@gmail' in value:
#           self._email = value
#           return self._email
#       else:
#           raise ValueError('Emailni togri formatda kiriting.')
  

#   def __str__(self):
#       return f'{self.name}, {self.age}, {self.email}'

# try:
#   user = User('M', '18', 's@gmail.com')
#   print(user)
# except (ValueError, TypeError) as error:
#   print(error)

##############