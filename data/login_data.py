# coding=utf-8


class LoginPageData:
    # 用户名输入框
    username_selectors = ['id', 'username']
    # 密码输入框
    password_selectors = ['id', 'password']
    # 登录按钮
    login_selectors = ['xpath', "//button[@class='ant-btn login-btn password-login ant-btn-primary']"]
    # 右上角单位名称
    quit_postion_selectors = ['css', '# user-toggle > div.header-right-user-avatar > i.icon-zcy.icon-touxiang1']

    logout_selectors = ['name', 'logout']
    # 订单页面 右上角单位名称
    order_quit_postion_selectors = ['class', 'header-right-user-avatar']
    # test_icon_selectors = ['css', 'div.ant-upload.ant-upload-select.ant-upload-select-picture-card > span > input[type=file]']
