from splinter.driver.webdriver.firefox import WebDriver as FirefoxWebDriver
from splinter.driver.webdriver.chrome import WebDriver as ChromeWebDriver
from splinter.exceptions import DriverNotFoundError

_DRIVERS = {
    'firefox': FirefoxWebDriver,
    'chrome': ChromeWebDriver
}

try:
    from splinter.driver.zopetestbrowser import ZopeTestBrowser
    _DRIVERS['zope.testbrowser'] = ZopeTestBrowser
except ImportError:
    pass


def Browser(driver_name='firefox', *args, **kwargs):
    """
    Returns a driver instance for the given name.

    When working with ``firefox``, it's possible to provide a profile name and a
    list of extensions.

    If you don't provide any driver_name, then ``firefox`` will be used.

    If there is no driver registered with the provided ``driver_name``, this function
    will raise a :class:`splinter.exceptions.DriverNotFoundError` exception.
    """

    try:
        driver = _DRIVERS[driver_name]
        return driver(*args, **kwargs)
    except KeyError:
        raise DriverNotFoundError("No driver for %s" % driver_name)
