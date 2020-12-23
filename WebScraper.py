from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException

class WebScraper:

    # Setup settings
    def __init__(self, url):
        self.url = url
        self.setUpProfile() # for setup profiles
        self.setUpOptions() # options for running gecko
        self.setUpCapabilities() # enable some abilities like marionette
        self.setUpProxy() # setup proxy if you get ban
        self.driver = webdriver.Firefox(options=self.options, capabilities=self.capabilities, firefox_profile=self.profile) # initialize web driver

    def setUpOptions(self):
        self.options = webdriver.FirefoxOptions()
        self.options.headless = self.headless

    def setUpProfile(driver):
        driver.profile = webdriver.FirefoxProfile()
        driver.profile.add_extension("buster_captcha_solver_for_humans-0.6.0.xpi") # add buster extension path
        driver.profile.set_preference("security.fileuri.strict_origin_policy", False) # disable Strict Origin Policy
        self.profile.update_preferences() # Update profile with new configs

    # Enable Marionette, An automation driver for Mozilla's Gecko engine
    def setUpCapabilities(self):
        self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.capabilities['marionette'] = True

    # Setup proxy
    def setUpProxy(self):
        pass
        #self.capabilities['proxy'] = { "proxyType": "MANUAL", "httpProxy": PROXY, "ftpProxy": PROXY, "sslProxy": PROXY }
    
    def run(self):
        print(self.driver.get(self.url))