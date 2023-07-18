from dhcp_config_handler import DHCPConfigHandler
from dhcp_log_processor import DHCPLogProcessor
from db_handler import DBHandler
from email_notifier import EmailNotifier

def main():
    log_processor = DHCPLogProcessor('/path/to/dhcp/logs')
    db_handler = DBHandler()

    while True:
        print("\n1. Upload DHCP configurations")
        print("2. Run DHCP log analyzer")
        print("3. Display unused IPs")
        print("4. Quit")

        choice = input("Please enter your choice: ")
        if choice == "1":
            config_path = input("Please enter the path to the DHCP configurations: ")
            config_handler = DHCPConfigHandler(config_path.strip())
            configs = config_handler.parse_configs()
            db_handler.update_db(configs)
        elif choice == "2":
            leases = log_processor.process_logs()
            db_handler.update_db(leases)
        elif choice == "3":
            unused_ips = db_handler.get_unused_ips()
            print('\n'.join(ip[0] for ip in unused_ips))
            EmailNotifier.send_email(unused_ips)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
