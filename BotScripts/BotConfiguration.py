import configparser
import logging
import os

rawconfig = configparser.RawConfigParser()
config = configparser.ConfigParser()

def rawconfigsetting(File):
    global rawconfig
    rawconfig.read(File)
def configsetting(File):
    global config
    config.read(File)


logger = logging.getLogger("Kiddo")
def log2ConsoleConfig():
    #%(asctime)s :: %(levelname)s :: Module %(module)s :: Line No %(lineno)s :: %(message)s
    logging.basicConfig(level=logging.INFO, format='%(message)s')

# WRITING LOG TO FILE #
def log2FileConfig():
        global logger

        # Gets or creates a logger
        #logger = logging.getLogger(config.get('logsetup','loggername'))

        # set log level
        logger.setLevel(int(config['logsetup']['loglevel']))

        # define file handler and set formatter
        file_handler = logging.FileHandler(os.getcwd() + config['logsetup']['filename'])

        #logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        formatter    = logging.Formatter(rawconfig['logsetup']['logformat'])
        file_handler.setFormatter(formatter)

        # add file handler to logger
        logger.addHandler(file_handler)




#An application which requires initial values to be loaded from a
#   file should load the required file or files using readfp() before calling read()
#   for any optional files:
#import configparser, os
#config = configparser.ConfigParser()
#config.readfp(open('defaults.cfg'))
#config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')])