from typing import Protocol

class Notification_Strategy(Protocol):
  def notify(self, recipient: str) -> None:
    ...
        
class Email_Strategy:
  def notify(self, recipient: str) -> None:
    print(f"Notifying {recipient} with Email...")
        
class SMS_Strategy:
  def notify(self, recipient: str) -> None:
    print(f"Notifying {recipient} with SMS...")
        
class Notification_Context:
  def __init__(self, strategy: Notification_Strategy) -> None:
    self._strategy = strategy
  
  def set_strategy(self, strategy: Notification_Strategy) -> None:
    self._strategy = strategy
      
  def notify(self, recipient: str) -> None:
    self._strategy.notify(recipient)
        
if __name__ == "__main__":
  notification_context = Notification_Context(Email_Strategy())
  notification_context.notify("jim@example.com")
  
  notification_context.set_strategy(SMS_Strategy())
  notification_context.notify("+555333222111")
