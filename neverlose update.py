from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp_server = 'smtp.qq.com'
smtp_port = 587
sender_email = '@qq.com'
password = ''

driver = webdriver.Chrome()
driver.get("https://en.neverlose.cc/sub?type=cs2")

time.sleep(60)

element = driver.find_element(By.CLASS_NAME, "cheat_changelog__wrapper")
WebDriverWait(driver, 5).until(EC.visibility_of(element))
initial_content = element.text

while True:
    time.sleep(3)
    current_content = element.text

    if initial_content!= current_content:
        updated_content = current_content.replace(initial_content, "")
        msg = MIMEText("更新内容: \n" + updated_content, 'plain', 'utf-8')
        msg['Subject'] = Header('Neverlose更新了！！！', 'utf-8')
        msg['From'] = '421881218@qq.com'
        msg['To'] = '421881218@qq.com'
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, [msg['To']], msg.as_string())
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('邮件发送失败:', str(e))
        initial_content = current_content

    driver.refresh()
    time.sleep(2)
    element = driver.find_element(By.CLASS_NAME, "cheat_changelog__wrapper")
