import xml.etree.ElementTree as ET
import csv

tree = ET.parse(r"~path here~\citems.xml")
root = tree.getroot()

# open a file for writing

Foglight_data = open(r'~path here~\output.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Foglight_data)
data_head = []

count = 0
for member in root.findall('Host'):
    name = []
    id = []
    if count == 0:
        vmname = member.find('name').tag
        data_head.append(vmname)
        #PhoneNumber = member.find('PhoneNumber').tag
        #data_head.append(PhoneNumber)
        #EmailAddress = member.find('EmailAddress').tag
        #data_head.append(EmailAddress)
        ID = member[3].tag
        data_head.append(ID)
        csvwriter.writerow(data_head)
        count = count + 1
    vmname = member.find('name').text
    name.append(name)
    #PhoneNumber = member.find('PhoneNumber').text
    #name.append(PhoneNumber)
    #EmailAddress = member.find('EmailAddress').text
    #name.append(EmailAddress)
    ID = member[3][0].text
    id.append(ID)
    #City = member[3][1].text
    #id.append(City)
    #StateCode = member[3][2].text
    #id.append(StateCode)
    #PostalCode = member[3][3].text
    #id.append(PostalCode)
    name.append(id)
    csvwriter.writerow(name)
Foglight_data.close()
