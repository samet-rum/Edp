class Event:
    def __init__(self, payload):
        self.payload = payload


class BookReservationRequestEvent(Event):
    name = 'book_reservation_request'


class ReservationConfirmationEvent(Event):
    name = 'reservation_confirmation'


class OverdueBookAlertEvent(Event):
    name = 'overdue_book_alert'


class UserNotificationEvent(Event):
    name = 'user_notification'
