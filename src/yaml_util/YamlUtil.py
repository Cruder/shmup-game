import yaml


def yaml2dic(yaml_path):
    try:
        with open(yaml_path, 'r') as stream:
            config = yaml.load(stream)
            return config
    except FileNotFoundError:
        print("Couldn't parse yaml file ", yaml_path)


def all_yaml2dic(yaml_path):
    try:
        with open(yaml_path, 'r') as stream:
            config = yaml.load_all(stream)
            return config
    except FileNotFoundError:
        print("Couldn't parse yaml file ", yaml_path)
