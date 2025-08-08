import requests
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.by import By


st_accept = "text/html" # говорим веб-серверу, 
                        # что хотим получить html
# имитируем подключение через браузер Mozilla на macOS
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
# формируем хеш заголовков
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}

# # отправляем запрос с заголовками по нужному адресу
# req = requests.get("https://stepik.org/catalog", headers)
# # считываем текст HTML-документа
# src = req.text
# # file = open("parsing/file.txt", "a", encoding="utf-8")
# # file.write(src)
# # file.close

# # инициализируем html-код страницы 
# soup = BeautifulSoup(src, 'lxml')
# # считываем заголовок страницы
# title = soup.title.string
# print(title)

# # cService = wd.ChromeService(executable_path=r"parsing/chromedriver.exe")
# # browser = wd.Chrome(service = cService)
# # open_search = browser.find_element_by_class_name("navbar__search-input")
# # open_search.click()
# # регистрируем текстовое поле и имитируем ввод строки "Git"
# # search = browser.find_element_by_class_name("search-modal_input")
# # open_search.send_keys("Git")

# driver = wd.Chrome()
# driver.get("https://stepik.org/catalog")
# element = driver.find_element("class name", "search-form__input")
# element.send_keys("python")
# but = driver.find_element('class name', "search-form__submit")
# but.click()

# print(driver)

# req = requests.get(driver.current_url, headers)
# src = req.text
# file = open("parsing/file.txt", "a", encoding="utf-8")
# file.write(src)
# file.close

driver = wd.Chrome()
driver.get()
