network_settings = {
    1: {'name': 'Network_1', 'ip_range': '192.168.1.0/24', 'status': 'active'},
    2: {'name': 'Network_2', 'ip_range': '192.168.2.0/24', 'status': 'inactive'}
}


def create_network():
    try:
        network_id = int(input("Enter network ID: "))
        name = input("Enter network name: ")
        ip_range = input("Enter IP range (e.g., 192.168.1.0/24): ")
        status = input("Enter status (active/inactive): ")

        if network_id in network_settings:
            print(f"❌ Network with ID {network_id} already exists.")
        else:
            network_settings[network_id] = {
                'name': name,
                'ip_range': ip_range,
                'status': status
            }
            print(f"✅ Network '{name}' created with ID {network_id}.")
    except ValueError:
        print("Invalid input. Network ID must be an integer.")


def read_network():
    try:
        network_id = int(input("Enter network ID to view: "))
        network = network_settings.get(network_id)
        if network:
            print(f"📡 Network {network_id}: {network}")
        else:
            print(f"❌ Network with ID {network_id} does not exist.")
    except ValueError:
        print("Invalid input. Please enter a valid network ID.")


def update_network():
    try:
        network_id = int(input("Enter network ID to update: "))
        if network_id in network_settings:
            name = input("Enter new name (press Enter to skip): ")
            ip_range = input("Enter new IP range (press Enter to skip): ")
            status = input("Enter new status (press Enter to skip): ")

            if name:
                network_settings[network_id]['name'] = name
            if ip_range:
                network_settings[network_id]['ip_range'] = ip_range
            if status:
                network_settings[network_id]['status'] = status

            print(f"✅ Network {network_id} updated.")
        else:
            print(f"❌ Network with ID {network_id} does not exist.")
    except ValueError:
        print("Invalid input. Please enter a valid network ID.")


def delete_network():
    try:
        network_id = int(input("Enter network ID to delete: "))
        if network_id in network_settings:
            del network_settings[network_id]
            print(f"🗑️ Network {network_id} deleted.")
        else:
            print(f"❌ Network with ID {network_id} does not exist.")
    except ValueError:
        print("Invalid input. Please enter a valid network ID.")


def setup_virtual_network():
    try:
        network_id = int(input("Enter new virtual network ID: "))
        name = input("Enter network name: ")
        ip_range = input("Enter IP range: ")
        status = input("Enter status: ")

        if network_id not in network_settings:
            network_settings[network_id] = {
                'name': name,
                'ip_range': ip_range,
                'status': status
            }
            print(f"✅ Virtual network '{name}' set up successfully.")
        else:
            print(f"⚠️ Network with ID {network_id} already exists.")
    except ValueError:
        print("Invalid input. Please enter a valid network ID.")


def update_network_settings():
    try:
        settings_id = int(input("Enter network ID to update configuration: "))
        if settings_id in network_settings:
            ip_range = input("Enter new IP range (press Enter to skip): ")
            status = input("Enter new status (press Enter to skip): ")

            if ip_range:
                network_settings[settings_id]['ip_range'] = ip_range
            if status:
                network_settings[settings_id]['status'] = status

            print(f"✅ Network {settings_id} updated with new configuration.")
        else:
            print(f"❌ Network with ID {settings_id} does not exist.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")


def display_menu():
    print("\n🌐 Virtual Network Configuration")
    print("----------------------------------")
    print("1. Create Network")
    print("2. Read Network")
    print("3. Update Network")
    print("4. Delete Network")
    print("5. Setup Virtual Network")
    print("6. Update Network Settings")
    print("7. Exit")


def main():
    while True:
        display_menu()
        choice = input("Select an option (1–7): ")

        if choice == '1':
            create_network()
        elif choice == '2':
            read_network()
        elif choice == '3':
            update_network()
        elif choice == '4':
            delete_network()
        elif choice == '5':
            setup_virtual_network()
        elif choice == '6':
            update_network_settings()
        elif choice == '7':
            print("🔚 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select from 1 to 7.")


if __name__ == "__main__":
    main()
