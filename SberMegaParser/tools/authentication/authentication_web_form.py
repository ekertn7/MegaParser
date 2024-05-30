__all__ = ['authentication_web_form']


def authentication_web_form(
    username_input_xpath: str,
    password_input_xpath: str,
    login_button_xpath: str,
    *args
):
    """Авторизация с помощью веб-формы только для selenium."""
