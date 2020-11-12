#!/usr/bin/python
from configparser import ConfigParser


def read_config(filename='config.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def default_config(filename='temp-config.ini,'):
    # create a parser
    parser = ConfigParser()

    # Setup Defaults
    postgresql_defaults = {"host":"localhost", "database":"bacula", "user":"bacula", "password":"password"}
    discord_defaults = {"token":"TOKEN", "bot":"True", "reconnect":"True"}
    bacula_defaults = {"job_map":"/etc/bacula/job-map.ini"}

    # Add sections and keys
    parser.add_section('postgresql')
    for key in postgresql_defaults.keys():
        parser.set('postgresql', key, postgresql_defaults[key])
    
    parser.add_section('discord')
    for key in discord_defaults.keys():
        parser.set('discord', key, discord_defaults[key])

    parser.add_section('bacula')
    for key in discord_defaults.keys():
        parser.set('bacula', key, bacula_defaults[key])

    # Write files
    with open(filename, 'w') as f:
        parser.write(f)
