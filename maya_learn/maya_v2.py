

# ___  __  ___  _  _  ___
# || \/ | ||=|| \\// ||=||
# ||    | || ||  //  || ||

# Ignore warnings for yaml usage.
import warnings
import ruamel.yaml
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)

import email.utils
import time
from datetime import datetime as Datetime

import pytz
import humanize
import dateparser
import iso8601

EPOCH_START = (1970, 1, 1)

class MayaDT(object):
    """The Maya Datetime object."""

    def __init__(self, epoch):
        super(MayaDT, self).__init__()
        self._epoch = epoch

    def __repr__(self):
        return '<MayaDT epoch={}>'.format(self._epoch)

    @staticmethod
    def __dt_to_epoch(dt):
        epoch_start = Datetime(*EPOCH_START, tzinfo=pytz.timezone('UTC'))
        return (dt - epoch_start).total_seconds()

    @classmethod
    def from_datetime(klass, dt):
        return klass(klass.__dt_to_epoch(dt))

    def datetime(self, to_timezone=None, naive=False):
        """Returns a timezone-aware datetime...
        Defaulting to UTC (as it should).
        Keyword Arguments:
            to_timezone {string} -- timezone to convert to (default: {None/UTC})
        """
        if to_timezone:
            return self.datetime().astimezone(pytz.timezone(to_timezone))

        dt = Datetime.utcfromtimestamp(self._epoch)

        # Strip the timezone info if requested to do so.
        if naive:
            return dt.replace(tzinfo=None)

        return dt.replace(tzinfo=self.timezone)


    # 调用了方程然后再进行封装
    @property
    def year(self):
        return self.datetime().year

    @property
    def month(self):
        return self.datetime().month

    @property
    def day(self):
        return self.datetime().day

    @property
    def hour(self):
        return self.datetime().hour

    @property
    def minute(self):
        return self.datetime().minute

    @property
    def second(self):
        return self.datetime().second

    @property
    def microsecond(self):
        return self.datetime().microsecond

    @property
    def timezone(self):
        return pytz.timezone('UTC')

    def iso8601(self):
        # Get a timezone-naive datetime.
        dt = self.datetime(naive=True)
        return '{}Z'.format(dt.isoformat())

    def epoch(self):
        return self._epoch

    def slang_date(self):
        return humanize.naturaldate(self.datetime())

    def slang_time(self):
        return humanize.naturaldate(self.datetime())

    def rfc2822(self):
        tt = self.datetime().timetuple()
        ts = email.utils.mktime_tz(tt, pytz.utc)
        return email.utils.formatdate(ts)


def now():
    """Returns MayaDT for right now."""
    epoch = time.time()
    return MayaDT(epoch=epoch)

def when(string, timezone='UTC'):
    dt = dateparser.parse(string, settings={'TIMEZONE': timezone, 'RETURN_AS_TIMEZONE_AWARE': True, 'TO_TIMEZONE': 'UTC'})

    if dt is None:
        raise ValueError('invalid datetime input specified.')

    return MayaDT.from_datetime(dt)

def from_iso8601(string):
    # import from dateutil.parser import parse
    dt = iso8601.parse_date(string)
    return MayaDT.from_datetime(dt)

def from_rfc2822(string):
    # dt = Datetime.fromtimestamp(email.utils.mktime_tz(email.utils.parsedate_tz(string)), pytz.utc)
    print string
    from dateutil.parser import parse
    dt = parse(string)
    dt = pytz.utc.localize(dt)
    return MayaDT.from_datetime(dt)
