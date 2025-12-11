from selenium import webdriver

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)

def before_scenario(context, scenario):
    context.driver.delete_all_cookies()

def after_all(context):
    context.driver.quit()
