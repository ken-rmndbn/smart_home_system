from base_device import SmartDevice

class SmartThermostat(SmartDevice):
    def __init__(self, device_id: str, friendly_name: str) -> None:
        super().__init__(device_id, friendly_name)
        self.__target_temperature_celsius: float = 21.0
        self.__system_active: bool = False

    def modify_temperature(self, target_temperature: float) -> None:
        if 15.0 <= target_temperature <= 30.0:
            self.__target_temperature_celsius = target_temperature
            print(f"[Hardware Alert] Thermostat threshold shifted to {self.__target_temperature_celsius} degrees C.")
        else:
            raise ValueError("Target temperature parameter crosses safe physical hardware thresholds.")

    def turn_on(self) -> str:
        self.__system_active = True
        return f"Success: HVAC Controller '{self.friendly_name}' engaged. Core Targets: {self.__target_temperature_celsius} degrees C."

    def turn_off(self) -> str:
        self.__system_active = False
        return f"Success: HVAC Controller '{self.friendly_name}' disengaged."