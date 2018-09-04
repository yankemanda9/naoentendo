from splinter import Browser

browser = Browser('chrome')

def setUp():
    browser.visit('http://google.com')

setUp()

def login_gmail_to_google():
    browser.click_link_by_id('gb_70')
    browser.fill('identifier', 'email do gmail')
    browser.click_link_by_id('identifierNext')
    browser.is_element_not_present_by_id('password',1)
    browser.fill('password','aqui vai a senha')
    browser.click_link_by_id('passwordNext')

def login_to_github():
    browser.click_link_by_href('/login?return_to=%2Fonidata')
    browser.fill('login', 'seu email@hotmail.com')
    browser.fill('password', 'aqui vai a senha')
    browser.is_element_not_present_by_id('password', 2)
    browser.find_by_name('commit').click()

def pesquisar():
    browser.fill('q', 'github/onidata')

    if browser.find_by_tag('gsr'):
        browser.click_link_by_id('gsr').click()

    browser.find_by_name('btnK').click()

    if browser.is_text_present('https://github.com/onidata'):
        browser.click_link_by_href('https://github.com/onidata')

login_gmail_to_google()
setUp()
pesquisar()
login_to_github()