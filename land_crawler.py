from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import time

# options = Options()
# options.headless = True
# browser = webdriver.Firefox(options=options)
try:
    browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
    browser.get('https://new.land.naver.com/complexes/107901')
    summary = browser.find_elements_by_css_selector('div.list_complex_info ')[-1]
    print('------Summary------')
    print(summary.text)
    print('-------------------')

    total_elements_length = 0
    while True:
        current_elements = browser.find_elements_by_css_selector('div.item')
        current_elements_length = len(current_elements)
        if total_elements_length == current_elements_length:
            break

        total_elements_length = current_elements_length
        browser.execute_script('arguments[0].scrollIntoView(false);', current_elements[-1])
        time.sleep(1.5)

    targets = browser.find_elements_by_css_selector('div.item')
    for e in targets:
        print('---------')
        print(e.text)

        target_tag = 'a.item_link'
        if '네이버에서' in e.text:
            target_tag = 'a.label'

        e.find_element_by_css_selector(target_tag).click()
        details = browser.find_element_by_css_selector('div.detail_panel')
        print(details.text)

except Exception as err:
    print("Throws Exception!")
    print(err)

finally:
    print('Finished')
    browser.quit()


