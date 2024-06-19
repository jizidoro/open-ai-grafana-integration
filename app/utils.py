import os
import yaml

def load_config():
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path to the config file
    config_path = os.path.join(current_dir, '../config/config.yaml')

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Add debug print statement
    print("Loaded config:", config)

    return config