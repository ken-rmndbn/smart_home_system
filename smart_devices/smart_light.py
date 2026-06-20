from .base_device import SmartDevice

class SmartLight(SmartDevice):
    def __init__(self, device_id: str, friendly_name: str) -> None:
        super().__init__(device_id, friendly_name)
        self.__brightness_percentage: int = 0
        self.__is_powered: bool = False

    def adjust_dimmer(self, target_level: int) -> None:
        if 0 <= target_level <= 100:
            self.__brightness_percentage = target_level
            print(f"[Hardware Alert] Configured {self.friendly_name} dimmer register to {self.__brightness_percentage}%.")
        else:
            raise ValueError("Dimmer register setting out of physical bounds (0-100).")

    @property
    def current_brightness(self) -> int:
        return self.__brightness_percentage

    def turn_on(self) -> str:
        self.__is_powered = True
        self.__brightness_percentage = 100
        return f"Success: Light '{self.friendly_name}' illuminated to {self.__brightness_percentage}%."

    def turn_off(self) -> str:
        self.__is_powered = False
        self.__brightness_percentage = 0
        return f"Success: Light '{self.friendly_name}' relay broken (OFF)."