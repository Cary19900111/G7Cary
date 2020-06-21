from datetime import datetime
import configparser
from optparse import OptionParser

class Pipe(object):
    def __init__(self,arg):
        self.Handle = []
        self.mid = arg
    def add(self,Handler):
        self.Handle.append(Handler)
    def runAndPrint(self):
        for Handler in self.Handle:
            self.mid = Handler(self.mid)
        print(self.mid)

def VisualConfig(): 
    components = {}
    steps = []
    config = configparser.ConfigParser()
    config.read("config.ini")
    for section in config.sections():
        for step in config.items(section):
           steps.append(step[1]) 
        components[section]=steps
        steps=[]
    print(components)
    # print(config.options("GetHour"))
    # print(config.items("GetHour"))
    # print(type(config.get("GetHour","step1")))
    # template = "{}|{}\n".format(component,steps)

def GetTimeFromStamp(time_stamp=1578640826):
    times = datetime.fromtimestamp(time_stamp)
    return times

def GetYears(time):
    year = time.year
    return year

def GetMinute(time):
    m = time.minutes
    return m 

def parse_options():
    #initialize
    parser = OptionParser(usage="python main.py [components] [i_parameter]")
    parser.add_option(
        '-r','--run',
        dest = 'run',
        default=None,
        help = 'run the component'
    )
    parser.add_option(
        '-l','--componentList',
        dest = 'component',
        default = None,
        help= 'show component list'

    )
    opts, args = parser.parse_args()
    return parser, opts, args

if __name__=="__main__":
    parser, options, arguments = parse_options()
    print(options.run)
    print(arguments)