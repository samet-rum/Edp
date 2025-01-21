class NotificationSystem:
    @staticmethod
    def send_notification(event):
        user_id = event.payload['user_id']
        message = event.payload.get('message', 'No message specified.')
        print(f"Notification sent to User {user_id}: {message}")
