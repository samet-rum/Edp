from agents.user import User
from agents.library import Library
from agents.notification import NotificationSystem
from agents.admin import Admin
from handlers import EventHandler, communication_queue
from events import ReservationConfirmationEvent, OverdueBookAlertEvent, UserNotificationEvent

def main():
    # Event Handler oluştur
    event_handler = EventHandler()

    # Ajanlar oluştur
    library = Library()
    notification_system = NotificationSystem()
    admin = Admin(1, "Admin Jane")

    # Kullanıcılar
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")

    # Event Handlers kayıt
    event_handler.register_handler('book_reservation_request', library.handle_reservation_request)
    event_handler.register_handler('reservation_confirmation', lambda event: print(
        f"Reservation {'confirmed' if event.payload['is_confirmed'] else 'denied'} for book '{event.payload['book_title']}'."))
    event_handler.register_handler('overdue_book_alert', lambda event: print(
        f"Overdue alert for User {event.payload['user_id']} on book '{event.payload['book_title']}'."))

    event_handler.register_handler('user_notification', notification_system.send_notification)

    # Kullanıcıların kitap rezervasyon talepleri
    print("\n--- Kullanıcıların Kitap Rezervasyon Talepleri ---\n")
    user1.request_book_reservation("Python 101")
    user2.request_book_reservation("AI for Beginners")

    # Kuyruktaki eventlerin işlenmesi
    print("\n--- Kuyruktaki Eventlerin İşlenmesi ---\n")
    while communication_queue:
        current_event = communication_queue.pop(0)
        event_handler.emit(current_event.name, current_event)

    # Gecikmiş kitaplar için uyarılar
    print("\n--- Gecikmiş Kitaplar İçin Uyarılar ---\n")
    library.check_overdue_books()

    # Admin işlemleri
    print("\n--- Admin İşlemleri ---\n")
    admin.add_book(library, "Deep Learning", 5)
    admin.remove_book(library, "Python 101")
    admin.approve_reservation(1, "Python 101")
    admin.cancel_reservation(library, 2, "AI for Beginners")

    # Kuyruktaki eventlerin yeniden işlenmesi
    print("\n--- Kuyruktaki Eventlerin Yeniden İşlenmesi ---\n")
    while communication_queue:
        current_event = communication_queue.pop(0)
        event_handler.emit(current_event.name, current_event)

if __name__ == "__main__":
    main()
