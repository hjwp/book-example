import subprocess

from selenium import webdriver

options = webdriver.FirefoxOptions()
options.log.level = "trace"

service = webdriver.FirefoxService(
    log_output=subprocess.STDOUT, service_args=["--log", "trace"]
)

# just try to open a selenium session
webdriver.Firefox(options=options, service=service).quit()
