from datetime import datetime

class DHCPLogProcessor:
    def __init__(self, log_path):
        self.log_path = log_path

    def process_logs(self):
        leases = []
        try:
            with open(self.log_path, 'r') as f:
                for line in f:
                    if 'DHCPACK' in line:
                        leases.append(self.extract_info_from_log(line))
        except IOError as e:
            print(f"Failed to open log file: {e}")
        return leases

    @staticmethod
    def extract_info_from_log(line):
        parts = line.split()
        timestamp_str = " ".join(parts[0:3])
        timestamp = datetime.strptime(timestamp_str, "%b %d %H:%M:%S")
        ip = parts[7]
        mac = parts[9]
        return ip, mac, timestamp, timestamp
