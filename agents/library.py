from events import ReservationConfirmationEvent, OverdueBookAlertEvent
from handlers import communication_queue

class Library:
    def __init__(self):
        self.books = {"Python 101": 3, "Data Science Handbook": 2, "AI for Beginners": 1}
        self.reserved_books = {}

    def handle_reservation_request(self, event):
        book_title = event.payload['book_title']
        user_id = event.payload['user_id']

        if self.books.get(book_title, 0) > 0:
            self.books[book_title] -= 1
            self.reserved_books[user_id] = book_title
            is_confirmed = True
            print(f"Library reserved '{book_title}' for User {user_id}.")
        else:
            is_confirmed = False
            print(f"Library: '{book_title}' is out of stock for User {user_id}.")

        confirmation_event = ReservationConfirmationEvent({'user_id': user_id, 'book_title': book_title, 'is_confirmed': is_confirmed})
        communication_queue.append(confirmation_event)

    def check_overdue_books(self):
        for user_id, book_title in self.reserved_books.items():
            alert_event = OverdueBookAlertEvent({'user_id': user_id, 'book_title': book_title})
            communication_queue.append(alert_event)
            print(f"Overdue alert generated for User {user_id} for book '{book_title}'.")
