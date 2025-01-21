from agents.user import User
from agents.library import Library
from agents.notification import NotificationSystem
from handlers import EventHandler, communication_queue
from events import ReservationConfirmationEvent, OverdueBookAlertEvent

# Event Handler Başlatılıyor
event_handler = EventHandler()

# Ajanlar
library = Library()
notification_system = NotificationSystem()

# Kullanıcılar
user1 = User(1, "Alice")
user2 = User(2, "Bob")

# Event Handlers Kayıt
event_handler.register_handler('book_reservation_request', library.handle_reservation_request)
event_handler.register_handler('reservation_confirmation', lambda event: print(f"Reservation {'confirmed' if event.payload['is_confirmed'] else 'denied'} for book '{event.payload['book_title']}'."))
event_handler.register_handler('overdue_book_alert', lambda event: print(f"Overdue alert for User {event.payload['user_id']} on book '{event.payload['book_title']}'."))

# Kullanıcı Talepleri
user1.request_book_reservation("Python 101")
user2.request_book_reservation("AI for Beginners")

# Kuyruktaki Taleplerin İşlenmesi
while communication_queue:
    current_event = communication_queue.pop(0)
    event_handler.emit(current_event.name, current_event)

# Gecikmiş Kitaplar İçin Uyarılar
library.check_overdue_books()
