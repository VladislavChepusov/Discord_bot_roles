# Инструкция
Для работы бота нужно сделать несколько шагов.

Для начала интегрировать в проект следующие python пакеты:

1.1)asyncio

1.2)re

1.3)httplib2

1.4)apiclient.discovery

1.5)oauth2client.service_account

1.5)discord.py


В visual studio 2019 для данных действий нужно перейти Средства->Python->Окружение Python->Пакеты (PyPI) и в поиске написать необходимый пакет.
Для примера возьмем основную(для нашего проекта) библиотеку discord.py.

![alt tag](https://user-images.githubusercontent.com/61112124/87040699-c71ff800-c1f9-11ea-9925-fe2ae5726cb0.png)​
Дальше нажимаем на pip instal

![alt tag](https://user-images.githubusercontent.com/61112124/87041063-562d1000-c1fa-11ea-98aa-2f2ab71d8542.png)

 Результат должен быть таким:
 
![alt tag](https://user-images.githubusercontent.com/61112124/87041107-68a74980-c1fa-11ea-8b58-7faa97c3fe92.png)


Следующий шаг,необходимо получить токен для вашего личного бота!Необходимо пройти на сайт https://discord.com/developers/applications, авторизоваться и создать свое приложение

![alt tag](https://user-images.githubusercontent.com/61112124/87041576-19154d80-c1fb-11ea-8664-5eea71dcb3b6.png)

Придумаем название для своего бота

![alt tag](https://user-images.githubusercontent.com/61112124/87041600-216d8880-c1fb-11ea-8102-b96f80ce3a86.png)

Переходим в раздел Bot и добавляем свеого бота,нажимая на кнопку "Add bot"
![alt tag](https://user-images.githubusercontent.com/61112124/87041644-32b69500-c1fb-11ea-9b39-b327080de0e6.png)

На появившейся странице нуобходимо получить уникальный токен вашего бота
![alt tag](https://user-images.githubusercontent.com/61112124/87041706-4cf07300-c1fb-11ea-98aa-9bca48b9f76f.png)

Чуть ниже в разделе Bot,нужно указать разрешения для бота

![alt tag](https://user-images.githubusercontent.com/61112124/87042138-e9b31080-c1fb-11ea-9f77-ed7981656639.png)

Никому не доверяйте эти данные и не держите их открытыми при загрузке на хостинг 

![alt tag](https://user-images.githubusercontent.com/61112124/87041887-8f19b480-c1fb-11ea-89c9-5ecbfa766324.png)


Копируйте полученную строчку и переходите в самый низ нашего с вами кода

![alt tag](https://user-images.githubusercontent.com/61112124/87041981-b4a6be00-c1fb-11ea-8358-d733efbae283.png)

Вставьте токен в данный участок кода

![alt tag](https://user-images.githubusercontent.com/61112124/87041935-a35db180-c1fb-11ea-9b85-12d7d1c5c825.png)


Большая часть пути позади!
 
Переходим https://console.developers.google.com/cloud-resource-manager и создаем свой проект 

![alt tag](https://user-images.githubusercontent.com/61112124/87043858-6515c180-c1fe-11ea-8064-c8742d702c32.png)

Дальше нам необходимо в нашем проекте включить два api: google drive и google sheets.

![alt tag](https://user-images.githubusercontent.com/61112124/87043946-870f4400-c1fe-11ea-9b2c-ca2ff688516a.png)

Начнем с первого.

![alt tag](https://user-images.githubusercontent.com/61112124/87044013-9db59b00-c1fe-11ea-9ff3-593937ecbd50.png)
![alt tag](https://user-images.githubusercontent.com/61112124/87044041-a9a15d00-c1fe-11ea-9086-6a5f1b3cb904.png)

После включения нам нужно создать рабочий аккаунт 

![alt tag](https://user-images.githubusercontent.com/61112124/87044120-c89fef00-c1fe-11ea-8f6e-db61e3dd3e41.png)

Заполняем поля в соответсвии со скришотом 

![alt tag](https://user-images.githubusercontent.com/61112124/87044249-f422d980-c1fe-11ea-87d1-ad58c2365fb9.png)

Продолжаем.тут придумываем имя своей почты и ставим  роль "редактор"

![alt tag](https://user-images.githubusercontent.com/61112124/87044389-1caad380-c1ff-11ea-8c5c-00a43e0e412f.png)

После успешного заполнения всех данных,на ваш компьютер должен скачаться файл типа json

![alt tag](https://user-images.githubusercontent.com/61112124/87044443-2fbda380-c1ff-11ea-867a-2dc4c5fbf9ba.png)

Данный файл нужно будет перенести в папку с проектом.Для удобства переименуйте его в creds.json

![alt tag](https://user-images.githubusercontent.com/61112124/87046356-c4c19c00-c201-11ea-8559-b14dc75930f3.png)

Включим еще google sheets api 

![alt tag](https://user-images.githubusercontent.com/61112124/87044628-7b704d00-c1ff-11ea-9fba-2ae197e59bbb.png)

Дальше мы переходим на сайт https://www.google.ru/intl/ru/sheets/about/
Создаем там таблицу и в правом верхнем углу нажимаем на "Настройки доступа"
![alt tag](https://user-images.githubusercontent.com/61112124/87046724-31d53180-c202-11ea-9bdf-6037be285087.png)

![alt tag](https://user-images.githubusercontent.com/61112124/87044816-becabb80-c1ff-11ea-9f4f-05f384f00884.png)

Добавляем наш созданный ранее аккаунт
![alt tag](https://user-images.githubusercontent.com/61112124/87044794-b70b1700-c1ff-11ea-99cf-3f6920c2ffc6.png)

Теперь,нам нужно получить ID документа Google Sheets(Это можно сделать скопировав часть адресной строки)
![alt tag](https://user-images.githubusercontent.com/61112124/87045141-34368c00-c200-11ea-866d-52b2828a79e2.png)

Снова переходим в наш с вами код и вставляем в этот участок полученный ID
![alt tag](https://user-images.githubusercontent.com/61112124/87045337-7233b000-c200-11ea-9653-cef3a11708f0.png)
 
