import allure
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
@allure.story('Steps with decorator')



@pytest.fixture()
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


def test_with_decorator_steps(browser_setup):
    open_main_page()
    open_input()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab('#issues-tab')
    should_see_issue_with_number("#81")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('https://github.com')


@allure.step('Открываем инпут поиска')
def open_input():
    s('.header-search-button').click()

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s('#query-builder-test').click().type(repo).press_enter()


@allure.step("Переходим посслыке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()



@allure.step('Открываем таб "Issues" {repo}')
def open_issue_tab(repo):
    s(repo).click()



@allure.step('Проверяем наличие "Issues" с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()