import pytest
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure
from allure_commons.types import Severity


@allure.label("owner", "v_serov")
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.story('Test steps with "with"')


@pytest.fixture()
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()



def test_github(browser_setup):
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Открытие поля поиска'):
        s('.header-search-button').click()

    with allure.step('Ищем репозиторий'):
        s('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб "Issues"'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие "Issues" с номером "76"'):
        s(by.partial_text('#76')).should(be.visible)
