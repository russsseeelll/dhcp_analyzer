class DHCPConfigHandler:
    def __init__(self, config_path):
        self.config_path = config_path

    def parse_configs(self):
        configs = []
        try:
            with open(self.config_path, 'r') as f:
                for line in f:
                    device_id, ip = line.strip().split()
                    configs.append((ip, device_id, None, None))
        except IOError as e:
            print(f"Failed to open config file: {e}")
        return configs
