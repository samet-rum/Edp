from events import BookReservationRequestEvent
from handlers import communication_queue

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def request_book_reservation(self, book_title):
        event = BookReservationRequestEvent({'user_id': self.user_id, 'book_title': book_title})
        communication_queue.append(event)
        print(f"User {self.name} requested reservation for '{book_title}'.")
