import ConfigParser
import datetime
import humanize
import pynder

pynder_config = {}
session = None


class Tinder(object):
    def __init__(self):
        parse_config()
        self.session = get_session()
        self.matches = self.session.matches()
        self.messages = {}

    def get_messages(self):
        for m in self.matches:
            self.messages[m.user.name] = m.messages

    def refresh(self):
        self.matches = self.session.matches()
        self.get_messages()

def get_session():
    session = pynder.Session(pynder_config['id'],
                             pynder_config['access_token'])
    return session


def parse_config():
    config_path = 'tinder.ini'
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    global pynder_config
    pynder_config['id'] = config.get('auth', 'id')
    pynder_config['access_token'] = config.get('auth', 'access_token')


def print_matches(match_list):
    for match in match_list:
        print(match.user.name)

def print_messages_for_match(match):
    print_messages(match.messages)

def print_messages(message_list):
    for message in message_list:
        print(repr_message(message))


def repr_message(message):
    sent = humanize.naturaltime(datetime.datetime.utcnow() -
                                message.__dict__['created_date'])
    repr_ = "{sender}\t - \t{sent}\t - \t{body}\n".format(
        sender=message.sender,
        sent=sent,
        body=message.body)
    print(repr_)


def setup():
    parse_config()
    global session
    session = get_session()
