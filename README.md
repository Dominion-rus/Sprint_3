_Необходимо наличие ChromeWebDriver соответствующий версии установленного браузера_
### Подробнее по ссылке ###
>https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

### Установка зависимостей ###
>pip install -r requirements.txt

### Запуск из корня проекта ###
>pytest -v ./tests/
### Тестируемое приложение(сайт) ###
> https://stellarburgers.nomoreparties.site
### Содержимое директории tests ###
-  test_login.py - тесты авторизации
-  test_logout.py - тесты на выход из аккаунта
-  test_navigate_in_constructor.py - тесты раздела Конструктор
-  test_personal_account.py - тесты личного кабинета
-  test_registration.py - тесты регистрации
-  test_from_pers_acc_to_constructor.py - тесты перехода из личного кабинета в конструктор 
