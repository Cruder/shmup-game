import yaml


def yaml2dic(yaml_path):
    return yaml.load(yaml_gen(yaml_path))


def all_yaml2dic(yaml_path):
    return yaml.load_all(yaml_gen(yaml_path))


def yaml_gen(path):
    try:
        with open(path, 'r') as stream:
            return stream
    except FileNotFoundError:
        print("Couldn't parse yaml file ", path)
