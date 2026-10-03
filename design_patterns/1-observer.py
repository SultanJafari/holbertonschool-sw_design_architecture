#!/usr/bin/env python3
"""
Observer pattern implementation - Adding a new subscriber (SmsObserver).
"""

from typing import Dict, Optional, Set


class NewsSubject:
    """The subject (publisher) that manages observers and broadcasts events."""

    def __init__(self) -> None:
        # Maps observer to the set of topics they care about
        # (None means all topics)
        self._observers: Dict[object, Optional[Set[str]]] = {}

    def subscribe(self, observer: object, topics: Optional[Set[str]] = None) -> None:
        """Subscribe an observer to specific topics or all topics if None."""
        self._observers[observer] = topics

    def unsubscribe(self, observer: object) -> None:
        """Unsubscribe an observer."""
        if observer in self._observers:
            del self._observers[observer]

    def notify(self, topic: str, data: str) -> None:
        """Notify all relevant observers about an event on a topic."""
        # Snapshot iteration to safely handle modifications during notification
        for observer, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Observer that logs specific news topics."""

    def update(self, topic: str, data: str) -> None:
        print(f"log:{topic}={data}")


class EmailObserver:
    """Observer that sends email notifications for all news topics."""

    def update(self, topic: str, data: str) -> None:
        print(f"email:{topic}={data}")


class SmsObserver:
    """Observer that sends SMS alerts for specific news topics."""

    def update(self, topic: str, data: str) -> None:
        print(f"sms:{topic}={data}")


def main() -> None:
    # Initialize the news subject (publisher)
    news = NewsSubject()

    # Instantiate existing observers
    log_obs = LogObserver()
    email_obs = EmailObserver()

    # Instantiate the new SMS observer
    sms_obs = SmsObserver()

    # Subscribe observers with their respective topic filters
    news.subscribe(email_obs, topics=None)  # Subscribed to all topics
    news.subscribe(log_obs, topics={"sports", "breaking"})
    news.subscribe(sms_obs, topics={"breaking"})  # Only subscribes to breaking news

    # Trigger events
    news.notify("weather", "rain")
    news.notify("sports", "goal")
    news.notify("breaking", "alert")


if __name__ == "__main__":
    main()
