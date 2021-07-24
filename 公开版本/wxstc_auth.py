hello_world = \
"""
Hello World
    Name：WXSC_Air校园网基于IP一键认证
    Maintainer：HangYu
    InitalTime：2021-03-12
    LasetTime：2021-07-24
    Version： 根据IP地址直接认证版本 v1.0
    
选择操作
    1. 根据IP地址直接校园网认证
    2. 检验认证结果
    3. 账号密码管理（首次使用，需要先进行该操作）
"""

import os, sys
import requests, configparser


# 定义认证体
class Auth():
    # 初始化数据
    def __init__(self):
        self.get_password_pwd = os.path.expanduser('~') + "\\wxstc_auth.txt"
        self.init_file()


    def create_auth(self):
        self.auth_ip = input('请输入需要认证的IP地址：')
        # 获取认证账号和密码
        cf = configparser.ConfigParser()
        cf.read(self.get_password_pwd, encoding='utf-8')

        self.user_name = cf.get('wxstc_auth', 'user_name')
        self.user_password = cf.get('wxstc_auth', 'user_password')
        self.auth_method = cf.get('wxstc_auth', 'auth_method')

        if self.user_name == 'user1':
            print('请先在配置文件中编辑认证账号、密码和认证方式')
            self.open_auth_txt()
        else:
            # 开始认证
            try:
                operator_dist = {'校园网': '', '中国移动': 'cmcc', '中国电信': '%40telecom', '中国联通': '%40unicom'}

                create_url = "http://10.255.254.1:801/eportal/?c=Portal&a=login&callback=dr1005&login_method=1&user_account=%2C0%2C{}{}&user_password={}&wlan_user_ip={}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.2&v=730".format(
                        self.user_name, operator_dist[self.auth_method], self.user_password, self.auth_ip)

                create_rsp = requests.get(create_url)
                create_rseult = create_rsp.content.decode('unicode_escape')
                print(create_rseult)
            except Exception as e:
                print('错误：', e)


    def test_baidu(self):
        os.system('ping baidu.com')

    def open_auth_txt(self):
        os.startfile(self.get_password_pwd)

    def init_file(self):
        if os.path.exists(self.get_password_pwd) == False:
            with open(self.get_password_pwd, 'wb') as f:
                f.write(b'[wxstc_auth]\r\n# \xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe8\xae\xa4\xe8\xaf\x81\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\r\nuser_name = user1\r\n# \xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe8\xae\xa4\xe8\xaf\x81\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81\r\nuser_password = 000000\r\n# \xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe8\xae\xa4\xe8\xaf\x81\xe6\x96\xb9\xe5\xbc\x8f\xef\xbc\x9a\xe6\xa0\xa1\xe5\x9b\xad\xe7\xbd\x91\xe3\x80\x81\xe4\xb8\xad\xe5\x9b\xbd\xe7\xa7\xbb\xe5\x8a\xa8\xe3\x80\x81\xe4\xb8\xad\xe5\x9b\xbd\xe7\x94\xb5\xe4\xbf\xa1\xe3\x80\x81\xe4\xb8\xad\xe5\x9b\xbd\xe8\x81\x94\xe9\x80\x9a\r\nauth_method = \xe6\xa0\xa1\xe5\x9b\xad\xe7\xbd\x91')
        else:
            pass


# 程序入口
if __name__ == '__main__':
    # 定义认证体
    print(hello_world)
    auth = Auth()

    # 选择程序
    while True:
        choose = input("请输入你需要的操作：")
        if choose == '1':
            auth.create_auth()
        elif choose == '2':
            auth.test_baidu()
        elif choose == '3':
            auth.open_auth_txt()
        else:
            pass



