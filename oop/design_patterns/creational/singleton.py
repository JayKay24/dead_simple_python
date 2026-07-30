import threading
from ..behavioral import Notification_Context, Notification_Strategy, Email_Strategy, SMS_Strategy

class Notification_Service:
  """
  A service that provides a singleton instance of Notification_Context.
  Ensures that only one context is created and shared across the application.
  """
  _notification_context: Notification_Context | None = None

  @classmethod
  def obtain_context(cls) -> Notification_Context:
    """
    Returns the singleton instance of Notification_Context.
    Creates it if it doesn't already exist.
    """
    if cls._notification_context is None:
      cls._notification_context = Notification_Context()
    
    return cls._notification_context

def main():
  """
  Demonstrates using the Notification_Service singleton in a thread-safe manner.
  """
  # Lock to ensure thread-safe access when changing the shared context's strategy
  lock = threading.Lock()
  notification_service = Notification_Service()

  def notify(strategy: Notification_Strategy, recipient: str) -> None:
    """
    Helper function to send a notification using a specific strategy.
    Uses a lock to prevent race conditions when updating the singleton's strategy.
    """
    nonlocal notification_service

    with lock:
      # Obtain the singleton context, update its strategy, and send the notification
      context = notification_service.obtain_context()
      context.set_strategy(strategy)
      context.notify(recipient)

  notify(Email_Strategy(), "jim@example.com")
  notify(SMS_Strategy(), "+555333222111")

if __name__ == "__main__":
  main()