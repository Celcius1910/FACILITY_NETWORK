import pytest
from pages import HomePage
import allure


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Find Your Service Navbar")
@allure.story("Navbar Item")
@pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
def test_open_findYourService_navbar(page, index):
    home_page = HomePage(page)
    home_page.load()
    home_page.findYourService.hover_findYourServices()
    home_page.findYourService.open_navbar_item(index)
    home_page.findYourService.validate_nav_item(index)


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'Success Stories' Navbar")
def test_open_successStories_navbar(page):
    home_page = HomePage(page)
    home_page.load()
    home_page.successStories.open_successStories_navbar()
    home_page.successStories.validate_successStories_link()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'Become A Service Provider' Navbar")
def test_open_becomeAServiceProvider_navbar(page):
    home_page = HomePage(page)
    home_page.load()
    home_page.becomeAServiceProvider.open_successStories_navbar()
    home_page.becomeAServiceProvider.validate_successStories_link()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'About Us' Navbar")
@pytest.mark.parametrize("index", [0, 1, 2])
def test_open_aboutUs_navbar(page, index):
    home_page = HomePage(page)
    home_page.load()
    home_page.aboutUs.hover_aboutUs_navbar()
    home_page.aboutUs.open_aboutUs_navbarItem(index)
    home_page.aboutUs.validate_nav_item(index)
