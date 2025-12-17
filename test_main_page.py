from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.go_to_login_page()