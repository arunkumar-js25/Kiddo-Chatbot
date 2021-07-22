'''
Author  @Arun Kumar
Date    @11-OCT-2020
Project @KIDDO
Desc    @Personal Assistant
'''

import aiml
import os
from BotScripts.Properties import BotProperties
from multiprocessing import Process,Value
from BotScripts.BotRequestProcess import *
from BotScripts.Senses import *
from BotScripts.BotConfiguration import *

#Configuration
rawconfigsetting('config.ini')
configsetting('config.ini')

#LoggerSetup
log2ConsoleConfig()
log2FileConfig()

#Main
procs = []
BotInactive = True
BotMode = config['Basic']['mode']

#Kernel Setup
kernel = aiml.Kernel()
sessionId = 12345

if __name__ == "__main__":

    if os.path.isfile(os.getcwd() + config['Basic']['botBrain']):
       kernel.bootstrap(brainFile=os.getcwd() + config['Basic']['botBrain'])
    else:
        kernel.bootstrap(learnFiles=os.getcwd() + config['Basic']['botaimlstartup'],
                         commands=config['Basic']['botaimlstartupcommand'])
        kernel.saveBrain(os.getcwd() + config['Basic']['botBrain'])

    # Load Bot Predicates
    BotProperties(kernel)

    if (BotInactive):
        print(config['Basic']['welcomemsg'])
        talk(config['Basic']['welcomemsg'])
        BotInactive = False

    while True:
        listen = str(input()).lower() #str(Listen()).lower()

        if (listen != None and listen != 'sorry could not recognize your voice'):

            if (listen != 'sorry could not recognize your voice'):
                logger.info("ME    >> " + listen)
            elif(listen=="save brain"):
                kernel.saveBrain(os.getcwd() + config['Basic']['botBrain'])
            elif listen == "quit":
                #print("Bye-Bye...")
                logger.info("KIDDO >> " + listen)
                exit()

            #if(listen):
             #   ChatBotCommands()

            bot_response = kernel.respond(listen.upper())

            if(listen[:16] == "ak change focus"):
                BotMode = kernel.getPredicate("mode").upper()
                print(BotMode)

            if(BotMode == "ACTION"):
                proc = Process(target=processRequest, args=(listen,))
                procs.append(proc)
                proc.start()
            elif(BotMode == "NORMAL"):
                logger.info("KIDDO >> " + str(bot_response))
                talk(bot_response)
