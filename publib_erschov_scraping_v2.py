from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from tqdm import tqdm
import os
import zipfile

url = 'http://www.publ.lib.ru/ARCHIVES/_CLASSES/OBS_HUD/_Obs_hud.html'
# получение ответа сервера при обращении к веб-странице
response = requests.get(url)
# с помощью библиотеки bs4 парсим HTML-страницу, предварительно перекодировав ответ сервера в текст (unicode)
soup = BeautifulSoup(response.text, 'html.parser')
# создаем список, куда будут добавлены ссылки на скачивание файлов
zip_links = []
# ищем все объекты с тегом "а" и атрибутом "href" (гипертекстовые ссылки)
links = soup.find_all('a', href=True)
# проверяем распознанные объекты: если ссылка заканчивается на .zip, она нам подходит => добавляем в список
for link in links:
    href = link.get('href')
    if href.endswith('.zip'):
        zip_links.append(urljoin(url, href))
print(zip_links)

# создание архива, куда будут загружаться все необходимые файлы
merged_zip_name = 'merged.zip'
# задаем для него ту же директорию, в которой находится файл с кодом
merged_zip_path = os.path.join(os.getcwd(), merged_zip_name)

# список ссылок на случай ошибок
errors = []

# открываем общий архив в режиме записи
with zipfile.ZipFile(merged_zip_path, 'w') as merged_zip:
    # запуск цикла по списку ссылок на скачивание (прогресс продвижения по циклу (= загрузки файлов) отображается в
    # специальном индикаторе)
    for url in tqdm(zip_links):
        # получение ответа сервера при обращении к ссылкам
        response = requests.get(url)
        # если статус запроса 200 (OK), файл скачивается по ссылке в общий архив
        if response.status_code == 200:
            file_name = url.split('/')[-1]
            merged_zip.writestr(file_name, response.content, zipfile.ZIP_DEFLATED)
        # при возникновении ошибки ссылка добавляется в список ошибок, который выводится при наличии хотя бы 1 ссылки
        else:
            errors.append(url)
if len(errors) > 0:
    print(f'Number of errors occurred: {len(errors)}. Broken links: {errors}.')
