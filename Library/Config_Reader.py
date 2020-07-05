import configparser


def Readconfigdata(section, key):
    config = configparser.ConfigParser()
    config.read("C:/Pycharm/Configuration/Path_details.cfg")
    return config.get(section, key)

def Readelements(section, key):
    config = configparser.ConfigParser()
    config.read("C:/Pycharm/Configuration/Elements.cfg")
    return config.get(section, key)
