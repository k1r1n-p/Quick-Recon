import os 
import getpass
import socket
import platform 
import psutil

def username():
    return getpass.getuser()

def system_information():
    return platform.system(), platform.version(), platform.release(), platform.machine(), platform.processor()

def ram():
    ram_information = psutil.virtual_memory()
    return ram_information.total, ram_information.available, ram_information.used, ram_information.percent

def private_ip_address():
    hostname = socket.gethostname()
    private_ip_add = socket.gethostbyname(hostname)
    return private_ip_add

def cpu():
    cpu_usage = psutil.cpu_percent(interval=2)
    cpu_physical_cores = psutil.cpu_count(logical=False)
    cpu_logical_cores = psutil.cpu_count(logical=True)
    return cpu_usage, cpu_physical_cores, cpu_logical_cores

def ssd():
    ssd_usage = psutil.disk_usage('/')
    return ssd_usage.total, ssd_usage.used, ssd_usage.free, ssd_usage.percent 

while True:
    print("\nMain Menu")
    print("0. Exit")
    print("1. User Information")
    print("2. System Information")
    print("3. RAM Information")
    print("4. IP Address")
    print("5. CPU Information ")
    print("6. SSD Information")
    print("7. All of above ")

    try:
        choice = int(input("Choose something from the menu (0-6):  "))
        if 0 <= choice <= 6:
            if choice == 0:
                print("Exiting")
                break
            if choice == 1:
                print(username())
            elif choice == 2:
                print("1. System Type \n2. System Version \n3. System Release  \n4. Machine Type \n5. Process Type \n6. All of them ")
                system_choice = int(input("Choose an option from system information menu (1-6): "))

                if system_choice == 1:
                    print(f"System Type: {system_information()[0]}")
                elif system_choice == 2:
                    print(f"System Version: {system_information()[1]}")
                elif system_choice == 3:
                    print(f"System Release: {system_information()[2]}")
                elif system_choice == 4:
                    print(f"Machine Type: {system_information()[3]}")
                elif system_choice == 5:
                    print(f"Process Type: {system_information()[4]}")
                elif system_choice == 6:
                    print(system_information())
                else:
                    print("Please enter a valid option")

            elif choice == 3:
                print("1. Total RAM  \n2. Available RAM \n3. Used RAM  \n4. Percent used  \n5. All of them ")
                ram_choice = int(input("Choose an option from RAM Information menu (1-5): "))

                if ram_choice == 1:
                    print(f"Total RAM: {ram()[0]/(1024 ** 3): .1f} GB")
                elif ram_choice == 2:
                    print(f"Available RAM: {ram()[1]/(1024 ** 3): .1f} GB")
                elif ram_choice == 3:
                    print(f"Used RAM: {ram()[2]/(1024 ** 3): .1f} GB")
                elif ram_choice == 4:
                    print(f"Percentage RAM: {ram()[3]: .1f} %")
                elif ram_choice == 5:
                    print(f"Total RAM: {ram()[0]/(1024 ** 3): .1f} GB, Available RAM: {ram()[1]/(1024 ** 3): .1f} GB, Used RAM: {ram()[2]/(1024 ** 3): .1f} GB, Percentage RAM: {ram()[3]: .1f} %")
                else:
                    print("Please enter a valid number")
            elif choice == 4:
                print(private_ip_address())
            elif choice == 5:
                print("1. CPU usage \n2. Physical Cores \n3. Logical Cores \n4. All of them ")
                cpu_choice = int(input("Choose an option from the CPU Information menu (1-4): "))
                if cpu_choice == 1:
                    print(f"Usage: {cpu()[0]}")
                elif cpu_choice == 2:
                    print(f"Physical Cores: {cpu()[1]}")
                elif cpu_choice == 3:
                    print(f"Logical Cores: {cpu()[2]}")
                elif cpu_choice == 4:
                    print(f"Usage:{cpu()[0]}, Physical Cores: {cpu()[1]}, Logical Cores: {cpu()[2]}")
                else:
                    print("Please enter a valid number")
            elif choice == 6:
                print("1. Total SSD Space \n2. Used SSD Space \n3. Free SSD Space \n4. SSD Usage Percentage \n5. All of them ")
                ssd_choice = int(input("Choose an option from SSD usage menu (1-5): "))
                if ssd_choice == 1:
                    print(f"Total SSD Space: {ssd()[0]/(1024 ** 3): .1f} GB")
                elif ssd_choice == 2:
                    print(f"Used SSD Space: {ssd()[1]/(1024 ** 3): .1f} GB")
                elif ssd_choice == 3:
                    print(f"Free SSD Space: {ssd()[2]/(1024 ** 3): .1f} GB")
                elif ssd_choice == 4:
                    print(f"SSD Usage: {ssd()[3]: .1f} %")
                elif ssd_choice == 5:
                    print(f"Total SSD Space: {ssd()[0]/(1024 ** 3): .1f} GB")
                    print(f"Used SSD Space: {ssd()[1]/(1024 ** 3): .1f} GB")
                    print(f"Free SSD Space: {ssd()[2]/(1024 ** 3): .1f} GB")
                    print(f"SSD Usage: {ssd()[3]: .1f} %")
                else:
                    print("Please enter a valid option")

            elif choice == 7:
                print(f"Username: {username()}")
                print(f"System: {system_information()}")
                print(f"Total RAM: {ram()[0]/(1024 ** 3): .1f} GB, Available RAM: {ram()[1]/(1024 ** 3): .1f} GB, Used RAM: {ram()[2]/(1024 ** 3): .1f} GB, Percentage RAM: {ram()[3]: .1f} %")
                print(f"Private IP Address {private_ip_address()}")
                print(f"Usage:{cpu()[0]}, Physical Cores: {cpu()[1]}, Logical Cores: {cpu()[2]},")
        else:
            print("\nPlease input a valid option")

    except ValueError:
        print("\nInvalid Input. Please enter a valid number.")


