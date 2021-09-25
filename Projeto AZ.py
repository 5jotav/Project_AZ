from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get('https://app.redeaz.com.br/')

navegador.find_element_by_tag_name('a').click()
