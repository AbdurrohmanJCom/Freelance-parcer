from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Опции для скрытия окна браузера
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Запуск браузера в фоновом режиме

# Инициализация драйвера браузера
driver = webdriver.Chrome(options=options)

def process_links(links):
    for link in links:
        driver.get(link)
        try:
            # Нажатие на кнопку "показать"
            show_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="show-phone"]'))
            )
            show_button.click()
            time.sleep(1)  # Ждем 1 секунду после нажатия кнопки

            phone_link = driver.find_element_by_css_selector('a[data-testid="contact-phone"]')
            phone_number = phone_link.get_attribute("href")
            print("Номер телефона:", phone_number)
        except Exception as e:
            print("Ошибка при обработке ссылки:", e)

links = [
    'https://www.olx.uz/d/obyavlenie/0-dan-uy-quramiz-ustachilik-ishlarini-qilamiz-ID3x4GN.html',
    'https://www.olx.uz/d/obyavlenie/1-marta-ishlaylgan-havo-kompressori-24ta-lik-ID3DNMb.html',
    'https://www.olx.uz/d/obyavlenie/1-remont-gazovyh-kotlov-tashkent-vyezd-30-minut-lyuboy-slozhnosti-ID3BhU7.html',
    'https://www.olx.uz/d/obyavlenie/100-gelievye-vozdushnye-shary-ID3DcaB.html',
    'https://www.olx.uz/d/obyavlenie/100-gotovyh-proektov-arhitektor-dizayner-proektov-ID25wVa.html',
    'https://www.olx.uz/d/obyavlenie/1000-tn-holodilnik-ID3z1C4.html',
    'https://www.olx.uz/d/obyavlenie/150-000-sum-be-pul-dostavka-plita-16-sm-lik-ID3DIAm.html',
    "https://www.olx.uz/d/obyavlenie/150-tonalik-biton-qoradigan-bochka-sotiladi-ID3Du4k.html",
    "https://www.olx.uz/d/obyavlenie/160-tonna-shtampofka-press-ID3DhRX.html",
    "https://www.olx.uz/d/obyavlenie/2-5-tonalik-tentlik-mshinam-bor-zakaga-ID3DNCf.html",
    "https://www.olx.uz/d/obyavlenie/24-7-arenda-mashal-posuda-stol-stulya-arenda-prakat-ID3xtzQ.html",
    "https://www.olx.uz/d/obyavlenie/24-7-prakat-arenda-opalubka-prokat-lesa-betonamishalka-lesa-malinki-a-ID1YjYz.html",
    "https://www.olx.uz/d/obyavlenie/24-7-prakat-arenda-prokat-stol-stul-naves-zontik-zont-opalfka-samav-ID29puX.html",
    "https://www.olx.uz/d/obyavlenie/24-7-prakat-qozon-ochoq-zontik-ID3xA6M.html",
    "https://www.olx.uz/d/obyavlenie/24-7-prakat-stol-stul-chinni-arenda-samovar-zontik-ID3C1H7.html",
    "https://www.olx.uz/d/obyavlenie/24-7-prakat-stol-stul-naves-zontik-arenda-stol-stul-prakat-zontik-zont-ID3yp8z.html",
    "https://www.olx.uz/d/obyavlenie/24-7-prakat-toy-va-boshqa-marosimlar-uchun-stol-stul-pasuda-naves-ID3lB95.html",
    "https://www.olx.uz/d/obyavlenie/24-7-prokat-prakat-arenda-stol-stul-naves-zont-samavar-opalubka-stoya-ID1W2A4.html",
    "https://www.olx.uz/d/obyavlenie/24-7-prokat-stol-stul-pasuda-zontik-naves-shatyor-ID3xfm9.html",
    "https://www.olx.uz/d/obyavlenie/24-soat-avtoelektrik-ID3pIWO.html",
    "https://www.olx.uz/d/obyavlenie/28m-45m-52m-usluga-avtovishka-arenda-xizmat-avtokran-usluga-avtovishka-ID3AXaI.html"

]

# Обработка ссылок
process_links(links)

# Закрытие драйвера браузера
driver.quit()
