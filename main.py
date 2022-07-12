# Time
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
links = ['https://sp.olx.com.br/sao-paulo-e-regiao/zona-sul/imoveis/venda/apartamentos?f=p&sd=2814&sd=2823&sd=2818&sd=2872&sd=2840&sd=2862&sd=2832&sd=2833&sd=2852&sd=2864&sd=2830&sd=2835&sd=2854&sd=2842&sd=2838&sd=2845&sd=2855&sd=2836&sd=2860&sd=2846&sd=2863&sd=2825&sd=2824&sd=2868&sd=2837&sd=2870&sd=2822&sd=2847',       # 0
         'https://sp.olx.com.br/sao-paulo-e-regiao/zona-leste/imoveis/venda/apartamentos?f=p&sd=2900&sd=2893&sd=2817&sd=2892&sd=2889&sd=2890&sd=2894&sd=2875&sd=2885&sd=2879&sd=2897&sd=2878&sd=2880&sd=2887&sd=2902&sd=2898&sd=2905&sf=1',   # 1
         'https://sp.olx.com.br/sao-paulo-e-regiao/zona-oeste/imoveis/venda/apartamentos?f=p&sd=2913&sd=2933&sd=2808&sd=2922&sd=2917&sd=2912&sd=2932&sd=2930&sd=2919&sd=2915&sd=2914&sd=2931&sd=2920&sd=2928&sd=2926&sd=2927&sd=2909&sd=2929&sf=1',
         'https://sp.olx.com.br/sao-paulo-e-regiao/zona-norte/imoveis/venda/apartamentos?f=p&sd=2791&sd=2795&sd=2799&sd=2801&sd=2792&sd=2794&sd=2782&sd=2783&sd=2786&sd=2781&sd=2784&sd=2796&sf=1',
         'https://sp.olx.com.br/sao-paulo-e-regiao/outras-cidades/guarulhos/imoveis/venda/apartamentos?f=p',
         'https://sp.olx.com.br/sao-paulo-e-regiao/abcd/imoveis/venda/apartamentos?f=p&sd=2775&sd=2774&sd=2776&sf=1',
         'https://mg.olx.com.br/belo-horizonte-e-regiao/zona-centro-sul/imoveis/venda/apartamentos?f=p&sd=1673&sd=1672&sd=1677&sd=1668&sd=1669&sd=1681&sd=1670&sd=1686&sd=1678&sd=1671&sd=1680&sd=1688&sd=1682&sd=1687&sd=1667&sd=1666&sd=1676&sd=1684&sd=1679&sd=1665&sd=1689&sd=1683&sf=1',
         'https://mg.olx.com.br/belo-horizonte-e-regiao/zona-oeste/imoveis/venda/apartamentos?f=p&sd=1587&sd=1582&sd=1569&sd=1562&sd=1585&sd=1586&sd=1563&sd=1583&sd=1577&sd=1572&sd=1564&sd=1578&sd=1591&sd=1573&sd=1574&sd=1566&sd=1558&sd=1596&sd=1593&sd=1565&sd=1568&sf=1',
         'https://mg.olx.com.br/belo-horizonte-e-regiao/zona-leste/imoveis/venda/apartamentos?f=p&sd=1508&sd=1504&sd=1514&sf=1',
         'https://mg.olx.com.br/belo-horizonte-e-regiao/grande-belo-horizonte/nova-lima/imoveis/venda/apartamentos?f=p&q=NOVA%20LIMA&sf=1',
         'https://rj.olx.com.br/rio-de-janeiro-e-regiao/centro/imoveis/venda/apartamentos?f=p&sd=2217&sd=2220&sd=2219&sd=2221&sf=1',
         'https://rj.olx.com.br/rio-de-janeiro-e-regiao/zona-norte/imoveis/venda/apartamentos?f=p&sd=2184&sd=2163&sd=2175&sd=2185&sd=2169&sd=2181&sf=1',
         'https://rj.olx.com.br/rio-de-janeiro-e-regiao/zona-oeste/imoveis/venda/apartamentos?f=p&sd=2151&sd=2146&sd=2144&sf=1',
         'https://rj.olx.com.br/rio-de-janeiro-e-regiao/zona-sul/imoveis/venda/apartamentos?f=p&sd=2232&sd=2234&sd=2231&sd=2219&sd=2225&sd=2220&sd=2227&sd=2230&sd=2226&sd=2228&sd=2233&sd=2224&sd=2235&sd=2217&sd=2229&sf=1']
# 13 Links


# Basic Function
def click_element(element):
    driver.find_element(By. XPATH, element).click()


def wait_element(element):
    wdw(driver, 40).until(ec.element_to_be_clickable((By. XPATH, element)))


def change_screen(screen):
    int(screen)
    driver.switch_to.window(driver.window_handles[screen])


def check_user(name, words):

    for word in words:
        if word.lower() in name.lower():
            return False
    return True


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

    print(name_user)

    words = ['Imobiliária', 'Imobiliaria', 'corretor', 'Consultor', 'corretora', 'CONSULTORA', 'Consultoria', 'imóveis',
             'imoveis']

    # Check if Real State
    if check_user(name_user, words):
        print('Not Real State')
    else:
        print('Probably a Real State\n')
        driver.close()
        change_screen(0)
        return False

    # Clear String
    clear_pt1 = string_number.replace('(', '')
    clear_pt2 = clear_pt1.replace(')', '')
    clear_pt3 = clear_pt2.replace(' ', '')
    clear_pt4 = clear_pt3.replace('-', '')

    print(clear_pt4)

    # Check Phone
    with open('db.txt', 'r') as dbr:
        db_read = dbr.readlines()
        if (str(clear_pt4) + '\n') in db_read:
            dbr.close()
            driver.close()
            change_screen(0)
            print('The Number already Sent')
            return False
        else:
            dbr.close()
            with open('db.txt', 'a+') as dbw:
                dbw.write(str(clear_pt4) + '\n')

    # If number don't have 11 numbers, continue
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

        first_message = 'Message 1\n'

        second_message = 'Message 2\n'

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

for n in range(9, 13):
    driver.get(links[n])
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
                if send_whatsapp() is False:
                    continue

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
