from time import sleep

# Selenium configuration
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.add_argument('--profile-directory=Default')
options.add_argument('--user-data-dir=C:/Temp/ChromeProfile')

driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
driver.maximize_window()
links_sp = ['https://sp.olx.com.br/sao-paulo-e-regiao/zona-sul/imoveis/venda/apartamentos?f=p&sd=2814&sd=2823&sd=2818&sd=2872&sd=2840&sd=2862&sd=2832&sd=2833&sd=2852&sd=2864&sd=2830&sd=2835&sd=2854&sd=2842&sd=2838&sd=2845&sd=2855&sd=2836&sd=2860&sd=2846&sd=2…',       # 0
            'https://sp.olx.com.br/sao-paulo-e-regiao/zona-leste/imoveis/venda/apartamentos?f=p&sd=2900&sd=2893&sd=2817&sd=2892&sd=2889&sd=2890&sd=2894&sd=2875&sd=2885&sd=2879&sd=2897&sd=2878&sd=2880&sd=2887&sd=2902&sd=2898&sd=2905&sf=1',   # 1
            'https://sp.olx.com.br/sao-paulo-e-regiao/zona-oeste/imoveis/venda/apartamentos?f=p&sd=2913&sd=2933&sd=2808&sd=2922&sd=2917&sd=2912&sd=2932&sd=2930&sd=2919&sd=2915&sd=2914&sd=2931&sd=2920&sd=2928&sd=2926&sd=2927&sd=2909&sd=2929&sf=1']

driver.get(links_sp[2])


# Basic Function
def click_element(element):
    driver.find_element(By. XPATH, element).click()


def wait_element(element):
    wdw(driver, 100).until(ec.element_to_be_clickable((By. XPATH, element)))


def change_screen(screen):
    int(screen)
    driver.switch_to.window(driver.window_handles[screen])


# Whatsapp Bot Function
def send_whatsapp():

    # Get name and number
    name = '//*[@id="miniprofile"]/div/div/div/div[2]/div/span'
    phone = '//*[@id="miniprofile"]/div/div/div/div[5]/div/a/div[2]'
    name2 = '//*[@id="miniprofile"]/div/div/div[2]/div[2]/div/div[1]/div/span'
    phone2 = '//*[@id="miniprofile"]/div/div/div[2]/div[5]/div/a/div[2]'

    try:
        name_user = wdw(driver, 5).until(ec.element_to_be_clickable((By.XPATH, name))).text
        string_number = wdw(driver, 5).until(ec.element_to_be_clickable((By.XPATH, phone))).text
    except Exception:
        name_user = wdw(driver, 5).until(ec.element_to_be_clickable((By.XPATH, name2))).text
        string_number = wdw(driver, 5).until(ec.element_to_be_clickable((By.XPATH, phone2))).text

    # Clear String
    clear_pt1 = string_number.replace('(', '')
    clear_pt2 = clear_pt1.replace(')', '')
    clear_pt3 = clear_pt2.replace(' ', '')
    clear_pt4 = clear_pt3.replace('-', '')

    # If number don't have 11 numbers, continue
    print(clear_pt4)
    if len(clear_pt4) != 11:
        print('Invalid Phone')

    else:

        number_for_send = f'55{clear_pt4}'
        sleep(2)
        driver.get(f'https://wa.me/{number_for_send}')

        first_button = '//*[@id="action-button"]'
        wait_element(first_button)
        click_element(first_button)

        second_button = '//*[@id="fallback_block"]/div/div/h4[2]/a'
        wait_element(second_button)
        click_element(second_button)

        after_login_whatsapp = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'

        wait_element(after_login_whatsapp)

        salutation = f'Olá {name_user}, tudo bem?\n'

        first_message = 'Meu nome é João Collado, Creci: 95.176, vi seu imóvel anunciado na OLX.' \
                        ' Gostaria de ajudar você a aumentar as chances de venda do seu imóvel, anunciando nas principais imobiliárias do país, a Loft, o 5º Andar e a EmCasa.' \
                        ' Caso não tenha anunciado em alguma delas, me informe seu nome completo e endereço do apartamento que iremos realizar o cadastro, para depois os funcionários delas te contatarem, pegarem mais informações e publicarem seu imóvel.' \
                        '\n'

        second_message = 'Obrigado pela atenção! Fico à disposição.\n'

        txt_box = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'

        find_text_box = driver.find_element(By.XPATH, txt_box)

        find_text_box.send_keys(salutation)
        sleep(1)
        find_text_box.send_keys(first_message)
        sleep(1)
        find_text_box.send_keys(second_message)

        print('Message Send')
        sleep(1)


number_announcement = 0
for n in range(1, 56):
    number_announcement += 1
    print(f'------ About announcement {number_announcement} -------')

    # Pages need to reload due to an OLX update
    if n == 1:
        print('Page 1, will not refresh')

    else:
        print(f'Page {number_announcement}, will refresh')
        driver.refresh()

    try:
        click_element(f'//*[@id="ad-list"]/li[{n}]/div/a/div/div[1]/div[1]/div/img')
        print('Clicked on the Ad')

    # if can't click in the ad, continue
    except Exception as e:
        print('Error to Click Ad, li =', n)
        number_announcement -= 1
        continue

    change_screen(1)

    # Try to find phone
    try:
        click_element('//*[@id="miniprofile"]/div/div/div/div[5]/div/a/span/div')
        print('Phone found')
        sleep(2)
        try:
            send_whatsapp()
        except Exception as e:
            print(e)
            print('There was an error sending the message')
    except Exception as e:
        # print(e)
        print('Phone not found')
        driver.close()
        change_screen(0)
        continue

    driver.close()
    change_screen(0)
