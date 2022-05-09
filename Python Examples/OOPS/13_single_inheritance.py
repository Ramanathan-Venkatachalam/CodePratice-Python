#Single Inheritance
#Base Class
class Mi:
    company = 'Mi India'
    website = 'www.mi-india.com'

    def contact_details(self):
        print('Address : GST Road, Chennai')

#Derived Class
class MiBook(Mi):
    def __init__(self):
        self.name = 'Mi Book Laptop'
        self.year = 2020

    def product_details(self):
        print('Name: ', self.name)
        print('Year: ',self.year)
        print('Company:',self.company)
        print('Website: ',self.website)

laptop = MiBook()
laptop.product_details() #Has variable/instance called from base class
laptop.contact_details() #Function called from base class