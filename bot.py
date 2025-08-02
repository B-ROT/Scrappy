from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cred import FEA, FEA_PASS, TEA, SS, SP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

opt = webdriver.FirefoxOptions()

head_status = input("\nExecute the bot...\n\n1. Headed\t2. Headless\nSelect[1/2]: ")
if head_status == "1":
    opt.add_argument("--headed")
else:
    opt.add_argument("--headless")

driver = webdriver.Firefox(options=opt)


def scraper():
    url = "https://news.ycombinator.com/"
    driver.get(url)
    
    try:
        titles = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"titleline")))
        news_list = []
        for no, title in enumerate(titles,start=1):
            link = title.find_element(By.TAG_NAME, "a")
            news_list.append(f"{no}. {title.text}\nMore: {link.get_attribute('href')}\n")

        return news_list

    finally:
        driver.quit()

def mailer(list):
    msg = MIMEMultipart()
    msg["Subject"] = "News List"
    msg["From"] = FEA
    msg["To"] = TEA
    body = "\n".join(list)
    msg.attach(MIMEText(body))
    
    with smtplib.SMTP(SS, SP) as server:
        server.starttls()
        server.login(FEA, FEA_PASS)
        server.sendmail(FEA, TEA, msg.as_string())       

if __name__ == "__main__":
    mailer(scraper())


