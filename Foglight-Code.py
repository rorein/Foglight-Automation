import requests
from easygui import passwordbox
import csv
import lxml
import lxml.etree

####################################PART 1 --> Logging into the Foglight website

USER = input('username: ')
PASSWORD = passwordbox('password: ')

URL = 'url here'


def main():
    login_data = {
        'user': USER,
        'password': PASSWORD,
        'login': 'login',
    }
    r = requests.session()
    p = r.post(URL, login_data)
    # print(p.text) <- to view the  HTML on the page

    p = r.get('url here')


if __name__ == '__main__':
    main()

####################################PART 2 --> need access to Foglight "definitions" page



####################################PART 3 --> need to be able to run extraction


####################################PART 4 --> save it to CSV (part 1)
#XML: C:\Users\rorein\Desktop\SAS Stuff\Excel Docs\citems.xml


####################################PART 5 --> save it to CSV (part 2)
# with open('extraction.csv', 'w', newline='') as fp:
#     a = csv.writer(fp, delimiter=',')
#     data = [['Me', 'You'], #example data to be replaced with Foglight data (xml file)
#             ['293', '219'],
#             ['54', '13']]
#     a.writerows(data)
#     print(data) #to confirm what is inside the CSV file
