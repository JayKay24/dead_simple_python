import threading
from ..behavioral import Notification_Context, Notification_Strategy, Email_Strategy, SMS_Strategy

class Notification_Service:
  _notification_context: Notification_Context | None = None

  @classmethod
  def obtain_context(cls) -> Notification_Context:
    if cls._notification_context is None:
      cls._notification_context = Notification_Context()
    
    return cls._notification_context

def main():
  lock = threading.Lock()
  notification_service = Notification_Service()

  def notify(strategy: Notification_Strategy, recipient: str) -> None:
    nonlocal notification_service

    with lock:
      context = notification_service.obtain_context()
      context.set_strategy(strategy)
      context.notify(recipient)

  notify(Email_Strategy(), "jim@example.com")
  notify(SMS_Strategy(), "+555333222111")

if __name__ == "__main__":
  main()