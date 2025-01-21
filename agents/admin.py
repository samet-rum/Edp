from events import UserNotificationEvent
from handlers import communication_queue

class Admin:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name

    def add_book(self, library, book_title, quantity):
        if book_title in library.books:
            library.books[book_title] += quantity
        else:
            library.books[book_title] = quantity
        print(f"Admin {self.name} added {quantity} copies of '{book_title}' to the library.")

    def remove_book(self, library, book_title):
        if book_title in library.books:
            del library.books[book_title]
            print(f"Admin {self.name} removed '{book_title}' from the library.")
        else:
            print(f"Book '{book_title}' not found in the library.")

    def approve_reservation(self, user_id, book_title):
        event = UserNotificationEvent({
            'user_id': user_id,
            'message': f"Your reservation for '{book_title}' has been approved by Admin {self.name}."
        })
        communication_queue.append(event)
        print(f"Admin {self.name} approved the reservation for User {user_id}.")

    def cancel_reservation(self, library, user_id, book_title):
        if user_id in library.reserved_books and library.reserved_books[user_id] == book_title:
            del library.reserved_books[user_id]
            library.books[book_title] += 1
            event = UserNotificationEvent({
                'user_id': user_id,
                'message': f"Your reservation for '{book_title}' has been canceled by Admin {self.name}."
            })
            communication_queue.append(event)
            print(f"Admin {self.name} canceled the reservation for User {user_id}.")
        else:
            print(f"No reservation found for User {user_id} on book '{book_title}'.")
