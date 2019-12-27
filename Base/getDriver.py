from appium import webdriver

def get_android_driver(pac, act):
    """
    返回android手机驱动对象
    :param pac:
    :param act:
    :return:
    """

    #由字典类实例化一个对象
    capabilities = dict()
    capabilities["platformName"] = "Android"
    capabilities["platformVersion"] = "5.1"
    capabilities["deviceName"] = "模拟器"
    capabilities["appPackage"] = pac
    capabilities["appActivity"] = act
    capabilities['automationName'] = 'Uiautomator2'

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=capabilities)