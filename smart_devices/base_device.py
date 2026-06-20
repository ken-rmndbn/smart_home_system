from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, device_id: str, friendly_name: str) -> None:
        self.device_id: str = device_id
        self.friendly_name: str = friendly_name

    @abstractmethod
    def turn_on(self) -> str:
        pass

    @abstractmethod
    def turn_off(self) -> str:
        pass