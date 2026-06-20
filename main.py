from typing import List
from smart_devices import SmartDevice, SmartLight, SmartThermostat


def execute_system_override(hardware_stack: List[SmartDevice]) -> None:
    print("\n--- FIRMWARE INJECTION OVERRIDE SEQUENCING ---")
    for device_item in hardware_stack:
        action_log = device_item.turn_on()
        print(action_log)
    print("=============================================\n")


if __name__ == "__main__":
    print("=============================================")
    print("  DYNAMIC ENTERPRISE SMART HOME CONTROLLER   ")
    print("=============================================")

    kitchen_light = SmartLight(device_id="LT-4092", friendly_name="Kitchen Dimmer")
    bedroom_hvac = SmartThermostat(device_id="TH-1102", friendly_name="Master Bedroom Zone")

    home_network: List[SmartDevice] = [kitchen_light, bedroom_hvac]

    while True:
        print("Central Automation Menu:")
        print("1) Re-configure Kitchen Light Brightness")
        print("2) Re-configure Bedroom HVAC Temperature")
        print("3) Broadcast 'TURN ON' to All Registered Devices")
        print("4) Exit System")

        user_selection = input("\nSelect an option (1-4): ").strip()

        if user_selection == "1":
            try:
                brightness_level = int(input("Enter new brightness level (0-100): "))
                kitchen_light.adjust_dimmer(brightness_level)
                print("Success: Light configuration updated in memory.\n")
            except ValueError as error_message:
                print(f"Configuration Rejected: {error_message}\n")

        elif user_selection == "2":
            try:
                target_temp = float(input("Enter new target temperature Celsius (15.0-30.0): "))
                bedroom_hvac.modify_temperature(target_temp)
                print("Success: Thermostat configuration updated in memory.\n")
            except ValueError as error_message:
                print(f"Configuration Rejected: {error_message}\n")

        elif user_selection == "3":
            execute_system_override(home_network)

        elif user_selection == "4":
            print("Shutting down Central Automation Controller. Goodbye.")
            break

        else:
            print("Invalid menu selection. Try again.\n")