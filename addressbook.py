# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:36:44 2018

@author: Parul Mathur
"""

#!/usr/bin/python
#filename address-book.py
import time
import sys
import pickle
import os
import re


animation = ". |/-\\"

print("\n")
for i in range(30):
    time.sleep(0.1)
    if(i<28):
        sys.stdout.write("\r \tLOADING..." + animation[i % len(animation)])
        sys.stdout.flush()
    else:
        sys.stdout.write("\r \tLOADED :) nic,to see you")
    #do something
print("\n")




class Contact:
    #count=0
    def __init__(self,fname,lname,email,phone,address,soc_media):
        self.fname=fname
        self.lname=lname
        self.email=email
        self.phone=phone
        self.address=address
        self.soc_media=soc_media
        #self.count+=1
        
        
    def __str__(self):
        return "Name:{0} {1}\nEmail address:{2}\nPhone:{3}\naddress:{4}\nsocial media handle:{5}\n".format(self.fname,self.lname,self.email,self.phone,self.address,self.soc_media)
        
    def change_name(self,name):
        self.name=name
        
    def change_email(self,email):
        self.email=email
        
    def change_phone(self,phone):
        self.phone=phone
        
    def change_address(self,address):
        self.address=address
        
    def change_soc_handle(self,soc_media):
        self.soc_media=soc_media
        
def contact_full():                 #fuction to check contact list is full or not
    address_book_file=open("address_book_file","rb")
    list_contacts=pickle.load(address_book_file)
    count=1
    for i in list_contacts:
        count+=1
       # print(count," ",i);
    #print(int(count))
    if count<=3:
        return True
    else:
        return False
        
def add_contact():
    address_book_file=open("address_book_file","rb")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not contact_full():
        print("------contact list is full need to delete some contact----")
        address_book_file.close()
        return 
    elif not is_file_empty:
        list_contacts=pickle.load(address_book_file)
    else:
        list_contacts=[]
    try:
        contact=get_contact_info_from_user()
        address_book_file=open("address_book_file","wb")
        list_contacts.append(contact)
        list_contacts.sort(key=lambda contact:contact.lname)
        pickle.dump(list_contacts,address_book_file)
        print ("Contact added")
    except KeyboardInterrupt:
        print ("Contact not added")
    except EOFError:
        print ("Contact not added")
    finally:
        address_book_file.close()
    
def get_contact_info_from_user():
    try:
        fk=0
        while fk==0:
            contact_fname=input("Enter contact's first name\n")
            if not contact_fname[0].isupper():
                print('use first letter in uppercase\n')
            else:
                fk=1
        contact_lname=input("Enter contact's last name\n")
        fk=0
        while fk==0:
            contact_email=input("Enter contact's email\n")   #checking valid email or not
            match = re.match(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',contact_email)
            if match == None:
                print('!!-worng syntax-!!\nenter again\n')
            else:
                fk=1
        fl=0
        while fl==0:                                      #checking valid phone no.
            contact_phone=input("Enter contact's phone number(10 digits)\n") 
            length=len(contact_phone)
            if(length==10 and contact_phone.isdigit()):
                fl=1
                break;
            else:
                print("---number of digits are not 10----\n")
        contact_address=input("Enter contact's address\n")
        contact_social=input("enter contact's social media handle\n")
        contact=Contact(contact_fname,contact_lname,contact_email,contact_phone,contact_address,contact_social)
        return contact
    except EOFError as e:
        print("you are at the end of file")
        raise e
    except KeyboardInterrupt as e:
        #print "Keyboard interrupt. Contact not added"
        raise e
    
def display_contacts():                         #display all contacts in the file
    address_book_file=open("address_book_file","rb")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        list_contacts=pickle.load(address_book_file)
        for each_contact in list_contacts:
            print (each_contact)
    else:
        print ("No contacts in address book")
        return
    address_book_file.close()
    
def search_contact():                   #searching for contact
    #search_name=input("Enter the name\n")
    address_book_file=open("address_book_file","rb")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        search_name=input("Enter the first name\n")
        is_contact_found=False
        list_contacts=pickle.load(address_book_file)
        for each_contact in list_contacts:
            contact_name=each_contact.fname
            search_name=search_name.lower()
            contact_name=contact_name.lower()
            if(contact_name==search_name):
                print (each_contact)
                is_contact_found=True
                break
        if not is_contact_found:
            print ("No contact found with the provided search name")
    else:
        print ("Address book empty. No contact to search")
    address_book_file.close()

def delete_contact():                     #delete a contact
    #name=input("Enter the name to be deleted\n")
    address_book_file=open("address_book_file","rb")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        name=input("Enter the name to be deleted\n")
        list_contacts=pickle.load(address_book_file)
        is_contact_deleted=False
        for i in range(0,len(list_contacts)):
            each_contact=list_contacts[i]
            if each_contact.fname==name:
                del list_contacts[i]
                is_contact_deleted=True
                print( "Contact deleted")
                address_book_file=open("address_book_file","wb")
                if(len(list_contacts)==0):
                    address_book_file.write("")
                else:
                    pickle.dump(list_contacts,address_book_file)
                break
        if not is_contact_deleted:
            print ("No contact with this name found")
            
    else:
        print ("Address book is empty. can't delete any contact:(")
    address_book_file.close()
    
def modify_contact():                        #modify contact details other than name
    address_book_file=open("address_book_file","rb")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        name=input("Enter the name of the contact to be modified\n")
        list_contacts=pickle.load(address_book_file)
        is_contact_modified=False
        for each_contact in list_contacts:
            if each_contact.fname==name:
                do_modification(each_contact)
                address_book_file=open("address_book_file","wb")
                pickle.dump(list_contacts,address_book_file)
                is_contact_modified=True
                print ("Contact modified")
                break
        if not is_contact_modified:
            print ("No contact with this name found")
    else:
        print ("Address book empty. No contact to delete")
    address_book_file.close()
    
def do_modification(contact):         #getting details to maodify
    try:
        while True:
            print ("\n----Enter---\n* 1 to modify email\n* 2 to modify phone number\n* 3 to modify address\n* 4 to modify social handdle\n* 5 to quit without modifying")
            choice=input()
            if(choice=="1"):
                fk=0
                while fk==0:
                    new_email=input("Enter contact's email\n")
                    match = re.match(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',new_email)
                    if match == None:
                        print('!!-worng syntax-!!\nenter again\n')
                    else:
                        fk=1
                contact.change_email(new_email)
                break
            elif(choice=="2"):
                fl=0
                while fl==0:
                     new_phone=input("Enter contact's phone number(10 digits)\n")
                     length=len(new_phone)
                     if(length==10 and new_phone.isdigit()):
                         fl=1
                         break;
                     else:
                         print("---number of digits are not 10----\n")
                contact.change_phone(new_phone)
                break
            elif(choice=="3"):
                new_address=input("Enter new address\n")
                contact.change_address(new_address)
                break
            elif(choice=="4"):
                new_soc_handle=input("enter new social handle\n")
                contact.change_soc_handle(new_soc_handle)
                break
            elif(choice=="5"):
                False
                break
            else:
                print ("!!!--wrong choice--!!!")
                break
    except EOFError:
        print ("!!!--End of file: Error occurred--!!!!")
    except KeyboardInterrupt:
        print ("!!!!--Keyboard's Interrupt--!!!!!")
#first menu dispaly    
print ("------Enter your choice----- \n 'a' to add a contact\n 'b' to view contacts\n 'd' to delete a contact\n 'm' to modify a contact\n 's' to search for contact \n 'q' to quit")
while True:
    choice=input("Enter your choice\n")
    if choice == 'q':
        break
    elif(choice=='a'):
        add_contact()
    elif(choice=='b'):
        display_contacts()
    elif(choice=='d'):
        delete_contact()
    elif(choice=='m'):
        modify_contact()
    elif(choice=='s'):
        search_contact()
    else:
        print ("Incorrect choice. Need to enter the choice again")
        
