import os
import ConfigParser

__ROOT = os.path.abspath(os.path.dirname(__file__))
__CONFIG_FILE = os.path.join(__ROOT,'..','config.ini')
__config = ConfigParser.ConfigParser()

def get_config():
    __config.read(__CONFIG_FILE)
    zkConfig = __get_config_section_map('zookeeper')
    result = {}
    zkHosts = zkConfig['hosts'].split(",")
    newZkHosts = []
    for z in zkHosts:
        newZkHosts.append(z + ':' + zkConfig['port'])
    newZkHostsString = ','.join(map(str, newZkHosts))
    result['zkHosts'] = newZkHostsString
    result['zkroot'] = zkConfig['root']
    topicConfig = __get_config_section_map('topic')
    result['topicName'] = topicConfig['name']
    brokerConfig = __get_config_section_map('broker')
    brokerHosts = brokerConfig['hosts'].split(",")
    newBrokerHosts = []
    for b in brokerHosts:
        newBrokerHosts.append(b + ':' + brokerConfig['port'])
    newBrokerHostsString = ','.join(map(str, newBrokerHosts))
    result['brokerHosts'] = newBrokerHostsString
    return result


def __get_config_section_map(section):
    result = {}
    options = __config.options(section)
    for option in options:
        try:
            result[option] = __config.get(section, option)
        except:
            print("exception on %s!" % option)
            result[option] = None
    return result
