

from Base.base import Base
from Page.PageElements import PageElements
from selenium.common.exceptions import TimeoutException

class HomePage(Base):

    def __init__(self, driver ):
        Base.__init__(self, driver)

    def click_after_btn(self):
        """点击稍后跟新按钮"""
        try:
            self.click_ele(PageElements.home_after_btn_id)
        except TimeoutException:
            """什么也不弹"""
            print("更新弹窗没有弹出")

    def click_my_btn(self):
        """点击首页"""
        self.click_ele(PageElements.home_my_btn_id)

