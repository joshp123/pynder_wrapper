import ConfigParser
import datetime
import humanize
import pynder
import pytz
from prettytable import PrettyTable

from iterm_image import display_image

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
        original_matches = len(self.matches)
        original_messages = self.total_messages
        self.matches = self.session.matches()
        self.get_messages()
        new_matches = len(self.matches)
        if original_matches != new_matches:
            print("Before: {} matches, Now: {} matches.".format(
                original_matches, new_matches))

        if self.total_messages != original_messages:
            print("Before: {} messages, Now: {} matches.".format(
                original_messages, self.total_messages))


    @property
    def total_messages(self):
        return sum([len(self.messages[sender]) for sender in self.messages])

    def print_messages(self):
        self.refresh()
        recent = sorted([m for m in self.matches if m.messages], key=lambda match: match.messages[-1].sent)
        for match in recent:
            print_messages_for_match(match)


def get_session():
    session = pynder.Session(pynder_config['id'],
                             pynder_config['access_token'])
    return session


def repr_match(match):
    for photo in match.user.photos:
        display_image(photo)


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


def repr_matches(match_list):
    
    pass
    # table_of_images([m.photos])


def print_messages_for_match(match):
    print_messages(match.messages)


def split_every(n, s):
    return [s[i:i+n] for i in xrange(0, len(s), n)]


def print_messages(message_list):
    t = PrettyTable(["name", "time", "message"])
    for message in message_list:
        body = "\n".join(split_every(80, message.body))
        t.add_row([message.sender,
                   humanized_delta(message.sent),
                   body])
    print(t)


def humanized_delta(dt):
    return humanize.naturaltime(datetime_to_delta(dt))


def datetime_to_delta(dt):
    now = datetime.datetime.utcnow()
    now = now.replace(tzinfo=pytz.utc)
    return now - dt


def repr_message(message):
    sent = humanized_delta(message.sent)
    repr_ = "{sender}\t - \t{sent}\t - \t{body}\n".format(
        sender=message.sender,
        sent=sent,
        body=message.body)
    return repr_


def setup():
    parse_config()
    global session
    session = get_session()
