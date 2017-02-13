from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Firefox()

def after_all(context):
    context.browser.quit()

def before_feature(context, feature):
    pass

