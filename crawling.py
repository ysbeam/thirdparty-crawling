import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class CLatestVersion:
    def collectHnc2024(self):
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)

        url = "https://help.hancom.com/updates/hoffice130/ko-KR/HOffice2024_update.htm"
        driver.get(url)

        try:
            link = driver.find_elements(By.CLASS_NAME, "DropDown")

            # 리스트의 첫 번째 요소(가장 위에 있는 요소)를 클릭
            if link:
                link[0].click()
            else:
                print("content_title 요소를 찾을 수 없습니다.")
        
            version_text = driver.find_element(By.XPATH, '//*[@id="expcol"]/ul/table/tbody/tr[2]/td[2]').text.strip()
            print("한컴 2024 최신 버전: ", version_text)
        except Exception as e:
            print("오류가 발생했습니다:", e)
    
        driver.quit()
        
    def collectHnc2022(self):
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)

        url = "http://help.hancom.com/updates/hoffice120/ko-KR/HOffice2022_update.htm"
        driver.get(url)

        try:
            link = driver.find_elements(By.CLASS_NAME, "DropDown")

            # 리스트의 첫 번째 요소(가장 위에 있는 요소)를 클릭
            if link:
                link[0].click()
            else:
                print("content_title 요소를 찾을 수 없습니다.")
        
            version_text = driver.find_element(By.XPATH, '//*[@id="expcol"]/ul/table/tbody/tr[2]/td[2]').text.strip()
            print("한컴 2022 최신 버전: ", version_text)
        except Exception as e:
            print("오류가 발생했습니다:", e)
    
        driver.quit()
        
    def collectHnc2020(self):
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)

        url = "https://help.hancom.com/updates/hoffice110/ko-KR/HOffice2020_update.htm"
        driver.get(url)

        try:
            link = driver.find_elements(By.CLASS_NAME, "DropDown")

            # 리스트의 첫 번째 요소(가장 위에 있는 요소)를 클릭
            if link:
                link[0].click()
            else:
                print("content_title 요소를 찾을 수 없습니다.")
        
            version_text = driver.find_element(By.XPATH, '//*[@id="expcol"]/ul/table/tbody/tr[2]/td[2]').text.strip()
            print("한컴 2020 최신 버전: ", version_text)
        except Exception as e:
            print("오류가 발생했습니다:", e)
    
        driver.quit()
        
    def collectHnc2018(self):
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)

        url = "https://help.hancom.com/updates/hoffice100/ko-KR/HOffice2018_update.htm"
        driver.get(url)

        try:
            link = driver.find_elements(By.CLASS_NAME, "DropDown")

            # 리스트의 첫 번째 요소(가장 위에 있는 요소)를 클릭
            if link:
                link[0].click()
            else:
                print("content_title 요소를 찾을 수 없습니다.")
        
            version_text = driver.find_element(By.XPATH, '//*[@id="expcol"]/ul/table/tbody/tr[2]/td[2]').text.strip()
            print("한컴 2018 최신 버전: ", version_text)
        except Exception as e:
            print("오류가 발생했습니다:", e)
    
        driver.quit()
        
    def collectHncNeo(self):
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)

        url = "http://help.hancom.com/update_multilang/details/HOfficeNEO_update.htm"
        driver.get(url)

        try:
            link = driver.find_elements(By.CLASS_NAME, "DropDown")

            # 리스트의 첫 번째 요소(가장 위에 있는 요소)를 클릭
            if link:
                link[0].click()
            else:
                print("content_title 요소를 찾을 수 없습니다.")
        
            version_text = driver.find_element(By.XPATH, '//*[@id="expcol"]/ul/table/tbody/tr[2]/td[2]').text.strip()
            print("한컴 NEO 최신 버전: ", version_text)
        except Exception as e:
            print("오류가 발생했습니다:", e)
    
        driver.quit()
        
    def collectJava(self):
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)

        url = "https://www.oracle.com/java/technologies/javase/8all-relnotes.html"
        driver.get(url)
        
        version_element = driver.find_element(By.XPATH, '/html/body/div[2]/section[4]/div/div/div/div[1]/div/ul/li[1]')
        version_text = version_element.text.split()[1]
        print("Java 최신 버전: ", version_text)
        driver.quit()
        
    def collectAdobeReaderDC(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)
        
        url = "https://helpx.adobe.com/acrobat/release-note/release-notes-acrobat-reader.html#AcrobatDCandAcrobatReaderDCContinuousTrackreleasenotes"
        driver.get(url)
        
        modal = driver.find_element(By.CSS_SELECTOR, '#localeModalv2 > div > div > div.locale-link-wrapper.dexter-Cta > div > a')
        modal.click()
        
        link = driver.find_element(By.XPATH, '//*[@id="root_content_flex_items_position"]/div/div[16]/div/table/tbody/tr[2]/td[2]/a')
        link.click()
        version_text = driver.find_element(By.XPATH, '//*[@id="id1"]/tbody/tr[1]/td[3]/p/a').text.strip()
        # 정규 표현식을 사용해 숫자만 추출
        version_num = re.findall(r'\d+', version_text)
        version = '.'.join(map(str, version_num))  # 숫자를 '.'로 연결
        print("Adobe Reader DC 최신 버전: ", version)
        
        driver.quit()
        
    def collectAdobeAcrobat2020(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)
        
        url = "https://helpx.adobe.com/acrobat/release-note/release-notes-acrobat-reader.html#Acrobat2020andAcrobatReader2020ClassicTrackreleasenotes"
        driver.get(url)
        
        modal = driver.find_element(By.CSS_SELECTOR, '#localeModalv2 > div > div > div.locale-link-wrapper.dexter-Cta > div > a')
        modal.click()
        
        link = driver.find_element(By.XPATH, '//*[@id="root_content_flex_items_position"]/div/div[21]/div/table/tbody/tr[2]/td[2]/a')
        link.click()
        version_text = driver.find_element(By.CSS_SELECTOR, '#id1 > tbody > tr.row-even > td:nth-child(3) > p > a').text.strip()
        # 정규 표현식을 사용해 숫자만 추출
        version_num = re.findall(r'\d+', version_text)
        version = '.'.join(map(str, version_num))  # 숫자를 '.'로 연결
        print("Adobe Acrobat 2020 최신 버전: ", version)
        
        driver.quit()    
        
    def collectChrome(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=options)
        
        url = "https://chromereleases.googleblog.com/search/label/Desktop%20Update"
        driver.get(url)
        
        stable_channel_btn = driver.find_element(By.CSS_SELECTOR, '#Blog1 > div:nth-child(4) > h2 > a')
        stable_channel_btn[0].click()  # 첫 번째 요소 클릭
        
        version_text = driver.find_element(By.XPATH, '//*[@id="Blog1"]/div[1]/div[2]/div/p[1]/span/span/text()[1]').text.strip()
        # 정규 표현식을 사용해 숫자만 추출
        version_num = re.findall(r'\d+', version_text)
        version = '.'.join(map(str, version_num))  # 숫자를 '.'로 연결
        print("Chrome 최신 버전: ", version)
        
        driver.quit()

    def collectAll(self):
        self.collectHnc2024()
        self.collectHnc2022()
        self.collectHnc2020()
        self.collectHnc2018()
        self.collectHncNeo()
        self.collectJava()
        self.collectAdobeReaderDC()
        self.collectAdobeAcrobat2020()
        self.collectChrome()
        
collector = CLatestVersion()
collector.collectAll()