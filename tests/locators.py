

class RegistrationPage():
    reg_text = "//h2[text()='Регистрация']"  # заголовок Регистрация
    name_text = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/label" #Лейбл Имя
    email_text ="//*[@id='root']/div/main/div/form/fieldset[2]/div/div/label" #Лейбл Email
    passw_text = "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/label" #Лейбл пароль
    button_reg = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']" #Кнопка Зарегистрироваться
    input_name="//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input" # Инпут Имя
    input_email="//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input" # Инпут Email
    input_passw="//input[@name='Пароль']" #Инпут Пароль
    incorrect_passw_text="//p[text()='Некорректный пароль']" #Текст не корректный пароль
    login_button="//a[text()='Войти']" #Кнопка Войти на странице регистрации


class LoginPage():
    auth_text="//h2[text()='Вход']" #Текст Вход на странице логина
    email_text = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/label"  # Лейбл Email
    passw_text = "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/label"  # Лейбл пароль
    login_button="//button[text()='Войти']" #Кнопка Войти
    login_page_button="//button[text()='Войти в аккаунт']" #Кнопка Войти в аккаунт
    input_email = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"  # Инпут Email
    input_passw = "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"  # Инпут пароль
    recovery_passw_btn="//a[text()='Восстановить пароль']" #Кнопка Восстановить пароль


class MainPage():
    order_button="//button[text()='Оформить заказ']"#Кнопка Оформить заказ
    lk_button="// p[text()='Личный Кабинет']"#Кнопка перехода в ЛК
    logo_svg="//div[@class='AppHeader_header__logo__2D0X2']"# Лого
    bun_span = "//span[text()='Булки']"  # раздел с булками
    bun_header =  "//h2[text()='Булки']"  # хидер с булками
    sauce_span = "//span[text()='Соусы']"  # раздел с соусами
    sauce_header =  "//h2[text()='Соусы']"  # хидер с соусами
    topping_span = "//span[text()='Начинки']" # раздел с начинками
    topping_header =  "//h2[text()='Начинки']"  # хидер с начинками

class PersonalAccount():
    info_text="// p[text()='В этом разделе вы можете изменить свои персональные данные']"
    constructor_button = "// p[text()='Конструктор']"  # кнопка для перехода в конструктор
    logout_button = "// button[text()='Выход']"  # кнопка для выхода из аккаунта





