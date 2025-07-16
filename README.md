# 🌐 Virtual Network Configuration – Python Project

A menu-based Python project for simulating and managing basic virtual network settings like creating, reading, updating, and deleting networks. Built using core Python with dictionary data structures.

---

## 🧠 Features

- Create a new network
- View a network’s current configuration
- Update network name, IP range, and status
- Delete an existing network
- Set up a virtual network if not already created
- Update configuration settings (status, IP)
- Menu-based system with validation and user prompts

---

## 🔧 Technologies Used

- Language: Python 3
- Concepts: Dictionaries, Functions, Menus, Validation
- IDE: VS Code / PyCharm / Terminal-based Python

---

## 📂 File Structure

| File Name       | Description                                     |
|------------------|-------------------------------------------------|
| `vnet_config.py` | Main Python script for virtual network management |

---

## ▶️ How to Run

```bash
python vnet_config.py


🌐 Virtual Network Configuration
----------------------------------
1. Create Network
2. Read Network
3. Update Network
4. Delete Network
5. Setup Virtual Network
6. Update Network Settings
7. Exit
Select an option (1–7): 1
Enter network ID: 3
Enter network name: OfficeNet
Enter IP range (e.g., 192.168.3.0/24): 192.168.3.0/24
Enter status (active/inactive): active
✅ Network 'OfficeNet' created with ID 3.

🌐 Virtual Network Configuration
----------------------------------
1. Create Network
2. Read Network
3. Update Network
4. Delete Network
5. Setup Virtual Network
6. Update Network Settings
7. Exit
Select an option (1–7): 2
Enter network ID to view: 3
📡 Network 3: {'name': 'OfficeNet', 'ip_range': '192.168.3.0/24', 'status': 'active'}

🌐 Virtual Network Configuration
----------------------------------
Select an option (1–7): 3
Enter network ID to update: 3
Enter new name (press Enter to skip): OfficeNet_V2
Enter new IP range (press Enter to skip): 
Enter new status (press Enter to skip): inactive
✅ Network 3 updated.

🌐 Virtual Network Configuration
----------------------------------
Select an option (1–7): 4
Enter network ID to delete: 3
🗑️ Network 3 deleted.

🌐 Virtual Network Configuration
----------------------------------
Select an option (1–7): 5
Enter new virtual network ID: 4
Enter network name: BackupNet
Enter IP range: 192.168.4.0/24
Enter status: active
✅ Virtual network 'BackupNet' set up successfully.

🌐 Virtual Network Configuration
----------------------------------
Select an option (1–7): 6
Enter network ID to update configuration: 4
Enter new IP range (press Enter to skip): 192.168.4.0/25
Enter new status (press Enter to skip): inactive
✅ Network 4 updated with new configuration.

🌐 Virtual Network Configuration
----------------------------------
Select an option (1–7): 7
🔚 Exiting... Goodbye!

