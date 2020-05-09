import HTMLTestRunner
import unittest
from Common.send_email import *
'''
暂时用不掉，省略了一些功能
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
'''
case_dirs = r"D:\project_shumai\TestCase"  # 测试用例路径
discover = unittest.defaultTestLoader.discover(case_dirs, "test_*.py")




if __name__ =="__main__":
    # 运行测试用例同时保存测试报告
    test_report_path = "D:\project_shumai\Report\\report" + '.html'  # 保存测试报告路径
    with open(test_report_path, "wb") as report_file:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, title="自动化测试报告", description="接口功能测试")
        runner.run(discover)
    main()