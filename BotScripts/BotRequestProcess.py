from BotScripts.Senses import *
from BotScripts.BotConfiguration import *
from selenium import webdriver

# General Questions
def processRequest(input):
    try:
        if 'search' in input or 'play' in input:
            # a basic web crawler using selenium
            search_web(input)

        elif 'take' in input and ('screenshot' in input or 'snapshot' in input):
            #ScreenshotSaveOption()
            print("Screenshot")

        elif 'open' in input and 'app' in input:
            # another function to open
            open_application(input.lower())

    except:
        talk("I don't understand, I can search the web for you, Do you want to continue?")
        ans = Listen()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)


# function used to open application
def open_application(input):
    try:
        for app in (config['app']['applist']).split('+'):
            if app.lower() in input:
                talk("Opening "+app+" app")
                os.startfile(config['app'][app])
    except:
        talk("Application not available")

# Browser Search
def search_web(input):

    driver = webdriver.Chrome(os.getcwd() + config['path']['driverpath'])
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower():

        talk("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))

    elif 'wikipedia' in input.lower():

        talk("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))


    else:

        if 'google' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        else:
            driver.get("https://www.google.com/search?q=" + '+'.join(input.split()))