import random
import string
import requests
import bs4

def new_pw():
    
    digits = random.randint(8, 20) #must be >8 && <20

    letters_list = [string.printable]
    letters_list_to_str = "".join(letters_list)

    pw = "".join(random.choices(letters_list_to_str, k=digits))
    return pw

def new_email():
    link = 'https://tempail.com/'
    response = requests.get(link)
    
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    div_mail = soup.find('div', class_="bb").find('input', class_="adres-input")
    mail = div_mail.get('data-clipboard-text')
    return mail

def new_name():
    
    digits_fn = random.randint(4, 10) #must be >4 && <10

    letters_list = [string.ascii_lowercase, string.ascii_uppercase]
    letters_list_to_str = "".join(letters_list)

    first_name = "".join(random.choices(letters_list_to_str, k=digits_fn))
    return first_name


def date_of_birth():
    year = random.randint(1970,2003)
    month = random.randint(1,12)
    day = random.randint(1,28)
    date = str(day) + "/" + str(month) + "/" + str(year)
    return date

ID = dict() 

ID['firstName'] = new_name()
ID['lastName'] = new_name()
ID['email'] = new_email()
ID['pw'] = new_pw()
ID['dateOfBirth'] = date_of_birth()


print()
print("Congratulations for your new baby!")
print("------------------------------------")
print("NAME: " + str(ID['firstName']))
print("LAST NAME: " + str(ID['lastName']))
print("MAIL: " + str(ID['email']))
print("PASSWORD: " + str(ID['pw']))
print("DATE OF BIRTH: " + str(ID['dateOfBirth']))
print()