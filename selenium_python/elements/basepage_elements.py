from selenium.webdriver.support.select import Select


class BasePageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, value):
        driver = obj.driver
        return driver.find_element(*self.locator).get_attribute("value")


class BasePageDropDown(object):
    def __set__(self, obj, value):
        driver = obj.driver
        select = driver.find_element(*self.locator)
        Select(select).select_by_visible_text(value)

    def __get__(self, obj, value):
        driver = obj.driver
        select = driver.find_element(*self.locator)
        return Select(select).first_selected_option.text


class TagElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, value):
        driver = obj.driver
        return driver.find_element(*self.locator).get_attribute("data-value")


class DOMElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, value):
        driver = obj.driver
        return driver.find_element(*self.locator)


class DOMElements(object):
    def __set__(self, obj, value):
        driver = obj.driver
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, value):
        driver = obj.driver
        return driver.find_elements(*self.locator)
