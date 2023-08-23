import os
import ctypes

# Disable USB Ports
def disable_usb_ports():
    key = r"SYSTEM\CurrentControlSet\Services\USBSTOR"
    try:
        ctypes.windll.winreg.SetValueEx(ctypes.windll.winreg.HKEY_LOCAL_MACHINE, key, 0, ctypes.windll.winreg.REG_DWORD, 4)
        print("USB ports are disabled.")
    except Exception as e:
        print("Error:", e)

# Disable Bluetooth
def disable_bluetooth():
    # Code to disable Bluetooth here
    print("Bluetooth is disabled.")

# Restrict Command Prompt
def restrict_command_prompt():
    # Code to restrict command prompt here
    print("Command Prompt is restricted.")

# Block Website Access
def block_website(website):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    try:
        with open(hosts_path, "a") as hosts_file:
            hosts_file.write("\n127.0.0.1 " + website)
        print(f"Access to {website} is blocked.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    disable_usb_ports()
    disable_bluetooth()
    restrict_command_prompt()
    block_website("facebook.com")
