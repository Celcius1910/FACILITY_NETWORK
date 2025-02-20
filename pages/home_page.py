from playwright.sync_api import Page
from utils.config import *
import allure


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        # instance
        self.findYourService = self.FindYourService_Navbar(self)
        self.successStories = self.SuccessStories_Navbar(self)
        self.becomeAServiceProvider = self.BecomeAServiceProvider_Navbar(self)
        self.aboutUs = self.AboutUs_Navbar(self)

        # navbar elements
        self.findYourService_navbar = "#w-dropdown-toggle-0"
        self.findYourService_navbarItem = ".dropdown--services-grid-item"
        self.serviceName = ".dropdown--services-label"
        self.navbar = ".navbar1_link"
        self.phoneNumber = ".nav-phone"
        self.aboutUs_navbar = "#w-dropdown-toggle-1"
        self.aboutUs_navbarItem = ".navbar1_dropdown-link"

    def load(self):
        with allure.step(title="Open browser"):
            self.page.goto(BASE_URL)

    class FindYourService_Navbar:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def hover_findYourServices(self):
            with allure.step(title="Hover 'Find Your Services'"):
                self.page.hover(self.parent.findYourService_navbar)

        def open_navbar_item(self, index: int):
            product_locator = self.page.locator(self.parent.serviceName).nth(index)
            product_name = product_locator.inner_text()
            with allure.step(title=f"Click Navbar Item '{product_name}'"):
                navbar_item_locator = self.page.locator(
                    self.parent.findYourService_navbarItem
                ).nth(index)
                navbar_item_locator.click()

        def validate_nav_item(self, index: int):
            product_locator = self.page.locator(self.parent.serviceName).nth(index)
            product_name = product_locator.inner_text()
            with allure.step(title=f"Validate '{product_name}'"):
                title = self.page.locator(".heading-style-h1")
                assert (
                    title.inner_text() == "Lorem Services"
                ), f"'{product_name}' is not opened!"

    class SuccessStories_Navbar:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def open_successStories_navbar(self):
            successStories_navbar = self.page.locator(self.parent.navbar).nth(0)
            with allure.step(title=f"Click 'Success Stories' Navbar"):
                successStories_navbar.click()

        def validate_successStories_link(self):
            with allure.step(title=f"Validate 'Success Stories' Navbar"):
                actual_url = self.page.url
                assert (
                    actual_url == f"{BASE_URL}/industries-we-serve"
                ), "'Success Stories' page is not opened!"

    class BecomeAServiceProvider_Navbar:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def open_successStories_navbar(self):
            successStories_navbar = self.page.locator(self.parent.navbar).nth(1)
            with allure.step(title=f"Click 'Become A Service Provider' Navbar"):
                successStories_navbar.click()

        def validate_successStories_link(self):
            with allure.step(title=f"Validate 'Become A Service Provider' Navbar"):
                actual_url = self.page.url
                assert (
                    actual_url == f"{BASE_URL}/become-a-partner"
                ), "'Become A Service Provider' page is not opened!"

    class AboutUs_Navbar:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def hover_aboutUs_navbar(self):
            with allure.step(title=f"Hover 'About Us' Navbar"):
                self.page.hover(self.parent.aboutUs_navbar)

        def open_aboutUs_navbarItem(self, index: int):
            aboutUs_navbarItem_locator = self.page.locator(
                self.parent.aboutUs_navbarItem
            ).nth(index)
            aboutUs_navbarItem_name = aboutUs_navbarItem_locator.inner_text()
            with allure.step(title=f"Click Navbar Item '{aboutUs_navbarItem_name}'"):
                navbar_item_locator = self.page.locator(
                    self.parent.aboutUs_navbarItem
                ).nth(index)
                navbar_item_locator.click()

        def validate_nav_item(self, index: int):
            aboutUs_navbarItem_locator = self.page.locator(
                self.parent.aboutUs_navbarItem
            ).nth(index)
            aboutUs_navbarItem_name = aboutUs_navbarItem_locator.inner_text()
            with allure.step(title=f"Validate '{aboutUs_navbarItem_name}'"):
                title = self.page.locator(".heading-style-h1")
                if index == 0:
                    navbarItem = "Resources"
                elif index == 1:
                    navbarItem = "Careers"
                elif index == 2:
                    navbarItem = "Contact Us"
                else:
                    raise ValueError(
                        f"Invalid index {index}: Expected 0 (Resources), 1 (Careers), or 2 (Contuct Us)"
                    )

                assert (
                    title.inner_text() == f"{navbarItem}"
                ), f"'{navbarItem}' is not opened!"
