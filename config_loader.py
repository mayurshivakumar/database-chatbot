import toml


class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = {}

    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                self.config = toml.load(file)
        except IOError:
            print(f"Error: Failed to load config file '{self.config_file}'")
            raise

    def get_value(self, section, key):
        try:
            return self.config[section][key]
        except KeyError:
            print(f"Error: Failed to retrieve value from config file for section '{section}' and key '{key}'")
            raise
