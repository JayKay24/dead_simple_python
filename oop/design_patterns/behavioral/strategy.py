from typing import Protocol

class Notification_Strategy(Protocol):
  """
  Defines the common interface for all notification strategies.
  """
  def notify(self, recipient: str) -> None:
    """Send a notification to the specified recipient."""
    ...
        
class Email_Strategy:
  """
  A concrete strategy that sends notifications via Email.
  """
  def notify(self, recipient: str) -> None:
    """Send an email notification."""
    print(f"Notifying {recipient} with Email...")
        
class SMS_Strategy:
  """
  A concrete strategy that sends notifications via SMS.
  """
  def notify(self, recipient: str) -> None:
    """Send an SMS notification."""
    print(f"Notifying {recipient} with SMS...")
        
class Notification_Context:
  """
  Context class that uses a Notification_Strategy to send notifications.
  This allows changing the notification mechanism at runtime.
  A strategy can be provided at initialization or set later.
  """
  def __init__(self, strategy: Notification_Strategy | None = None) -> None:
    """Initialize the context with an optional strategy."""
    self._strategy = strategy
  
  def set_strategy(self, strategy: Notification_Strategy) -> None:
    """Update the current notification strategy."""
    self._strategy = strategy
      
  def notify(self, recipient: str) -> None:
    """Delegate the notification task to the current strategy, if one is set."""
    if self._strategy:
      self._strategy.notify(recipient)
        
if __name__ == "__main__":
  # Initialize the context with the Email strategy and send a notification
  notification_context = Notification_Context(Email_Strategy())
  notification_context.notify("jim@example.com")
  
  # Switch to the SMS strategy dynamically and send another notification
  notification_context.set_strategy(SMS_Strategy())
  notification_context.notify("+555333222111")
