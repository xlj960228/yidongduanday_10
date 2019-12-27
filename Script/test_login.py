import pytest, sys, os
sys.path.append(os.getcwd())

from Base.getData import GetData
from Base.getDriver import get_android_driver
from Base.page import Page

def login_value():
    #存储数据
    lis = []
    #读数据
    data = GetData().get_yaml_data("login.yml")
    #组装数据
    for i in data.values():
        lis.append(tuple(i.values()))

    return lis

class TestLogin:
    def setup_class(self):
        """初始化driver和统一入口类"""
        self.driver = get_android_driver("com.bjcsxq.chat.carfriend",".module_main.activity.MainActivity")
        #实例化统一入口类
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        """退出driver"""
        #退出
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def goto_person(self):
        """进入未登录个人中心 -class"""
        #点击稍后更新
        self.page_obj.get_home_page().click_after_btn()
        #点击我的
        self.page_obj.get_home_page().click_my_btn()

    @pytest.fixture(autouse=True)
    def goto_login(self):
        """进入登录页面 function"""
        #点击登录/注册
        self.page_obj.get_person_page().click_login_sigin_btn()

    @pytest.mark.parametrize("phone, password, mess, expData", login_value())
    def test_login(self, phone, password, mess, expData):
        """
        测试方法
        :param phone: 手机号
        :param password: 密码
        :param mess: 提示消息拼接内容
        :param expData: 预期结果
        :return:
        """
        #登录操作
        self.page_obj.get_login_page().login(phone, password)
        #判断用例的走向
        if mess:
            """失败用例"""
            #获取toast消息
            toast_message = self.page_obj.get_login_page().get_toast(mess)
            try:
                #断言assert
                assert toast_message == expData
            except AssertionError as e:  #断言失败异常
                #截图
                self.page_obj.get_setting_page().screen_png_adb("预期断言失败截图")
                #抛出异常
                raise e
            finally:
                #登录返回
                self.page_obj.get_login_page().click_return_btn()

        else:
            """成功用例"""
            #登录确认
            self.page_obj.get_login_page().click_login_acc_btn()

            #取用户名
            username = self.page_obj.get_person_page().get_username()
            print(username)

            try:
                #断言用户名
                assert username == expData
            except AssertionError as e:
                #截图
                self.page_obj.get_login_page().screen_png_adb("预期断言成功截图")
                #抛出异常
                raise e
            finally:
                #点击设置
                self.page_obj.get_person_page().click_setting_btn()
                #退出登录
                self.page_obj.get_setting_page().logout()
