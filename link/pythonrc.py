# Needs to stay here so sys.ps1 doesn't get modified.
import sys

def _init():
    import atexit
    import os
    import readline
    import types
    import time
    import uuid
    import pprint
    import hashlib
    import datetime
    try:
        import __builtin__
    except ImportError:
        import builtins as __builtin__

    histdir = os.path.expanduser('~/.pyhist')
    try:
        os.makedirs(histdir)
    except OSError:
        pass

    def _b(x):
        if not isinstance(x, bytes):
            x = x.encode('utf-8')
        return x

    histfile = os.path.join(histdir, hashlib.sha1(
        os.path.normpath(_b(os.path.abspath(sys.prefix)))).hexdigest())

    try:
        readline.read_history_file(histfile)
    except IOError:
        pass

    atexit.register(readline.write_history_file, histfile)


    def _magic_uuid(val=None):
        if val is None:
            return uuid.uuid4()
        elif isinstance(val, uuid.UUID):
            return val
        elif len(val) == 16:
            return uuid.UUID(bytes=val)
        return uuid.UUID(val)


    helpers = types.ModuleType('helpers')
    helpers.histfile = histfile
    helpers.pp = pprint.pprint
    helpers.uuid = _magic_uuid
    helpers.UUID = uuid.UUID
    helpers.uuid3 = uuid.uuid3
    helpers.uuid4 = uuid.uuid4
    helpers.uuid5 = uuid.uuid5
    helpers.dt = datetime.datetime
    helpers.datetime = datetime.datetime
    helpers.td = datetime.timedelta
    helpers.timedelta = datetime.timedelta
    helpers.time = time.time
    __builtin__.h = helpers

    COLORS = dict([
        ("Black"       , "0;30"),
        ("Red"         , "0;31"),
        ("Green"       , "0;32"),
        ("Brown"       , "0;33"),
        ("Blue"        , "0;34"),
        ("Purple"      , "0;35"),
        ("Cyan"        , "0;36"),
        ("LightGray"   , "0;37"),
        ("DarkGray"    , "1;30"),
        ("LightRed"    , "1;31"),
        ("LightGreen"  , "1;32"),
        ("Yellow"      , "1;33"),
        ("LightBlue"   , "1;34"),
        ("LightPurple" , "1;35"),
        ("LightCyan"   , "1;36"),
        ("White"       , "1;37"),
        ("Normal"      , "0"),
    ])

    NoColor = ''
    BaseTemplate  = '\001\033[%sm\002'

    for k in COLORS.keys():
        COLORS[k] = BaseTemplate % (COLORS[k],)

    sys.ps1 = '%s>>> %s' % (COLORS['Green'], COLORS['Normal'])
    #sys.ps2 = '%s... %s' % (COLORS['Red'], COLORS['Normal'])

_init()
del _init
