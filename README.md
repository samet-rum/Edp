# Event-Driven Programming (EDP) System - Library Management

## Overview

This project is an **Event-Driven Programming (EDP)** based system designed for managing a **Library**. The system allows users to request book reservations, admins to add/remove books, and notifications to be sent to users for reservation updates and overdue alerts. The system implements the Event-Driven paradigm by having multiple agents (classes emitting events) to handle various tasks.

## Key Features

- **User Agent**: Handles book reservation requests.
- **Admin Agent**: Manages book inventory, approves/cancels reservations.
- **Library Agent**: Handles book availability and overdue alerts.
- **Notification Agent**: Sends notifications to users regarding the reservation status and overdue books.
- **User Interface** (Extra Credit): Provides an interactive UI to interact with the system.

## Project Structure

The project is organized into the following components:

- **events.py**: Contains event classes representing different system events.
- **handlers.py**: Contains the `EventHandler` class that registers and emits events.
- **admin.py**: Admin functionalities for adding/removing books and managing reservations.
- **library.py**: Library functionalities for reserving books and handling overdue books.
- **notification.py**: Notification functionalities for sending messages to users.
- **user.py**: User functionalities for requesting book reservations.
- **app.py**: Main application that integrates all agents and manages event flow.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/edp-library-management.git
    ```

2. Navigate into the project directory:

    ```bash
    cd edp-library-management
    ```

3. (Optional) Set up a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate     # On Windows
    ```

4. Install any dependencies (if applicable):

    ```bash
    pip install -r requirements.txt  # If there are any external dependencies
    ```

## Usage

### Running the Application

1. Open the `app.py` file to run the system.

2. The system simulates the following actions:
   - Users request book reservations.
   - Admins add/remove books and approve/cancel reservations.
   - Notifications are sent to users about their reservation status.
   - Overdue alerts are generated for users who have not returned books on time.

3. The flow works as follows:
   - A user sends a reservation request event.
   - The library agent checks availability and sends a confirmation or rejection event.
   - Admin actions can approve or cancel the reservations.
   - Notifications are sent to the user based on these events.

### User Interface (Extra Credit)

For extra credit, a simple user interface can be added to allow users to:
- Request book reservations
- View available books
- See reservation status and overdue alerts.

You can integrate this with a web framework like Flask or Django, or use a simple console-based UI.

## Event-Driven Architecture

This system is built around **Event-Driven Architecture** (EDA), where the following key concepts are used:

- **Event**: An object that represents an action or change in state within the system. For example, a user requesting a book reservation triggers a `BookReservationRequestEvent`.
- **Event Handler**: A function or method that processes events and triggers actions based on the event. For instance, when a reservation request is received, the `Library` class processes it to check if the book is available.
- **Event Queue**: Events are placed in a queue (`communication_queue`), allowing them to be processed asynchronously.

## Contributing

Feel free to fork this repository, create a branch, make improvements, and submit a pull request. All contributions are welcome!

## License

This project is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or comments, feel free to reach out or open an issue in the repository. You can also follow me on [Medium](https://medium.com/@sametdemirtug312) for more tutorials and guides.

---

### Blog Post

I have written a detailed blog post on **Event-Driven Programming (EDP)**, explaining the core concepts and how this project applies those principles in a practical system. You can read the blog post [here](https://medium.com/@sametdemirtug312/olay-odakl%C4%B1-programlama-edp-ile-k%C3%BCt%C3%BCphane-y%C3%B6netim-sistemi-olu%C5%9Fturma-8b25c777de43).

This post also includes a link to this GitHub repository, where you can find the code and further instructions.

Happy coding!
