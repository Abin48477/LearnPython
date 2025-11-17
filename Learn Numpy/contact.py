#function to save contacts to a CSV file
from turtle import pd


def save_contats_to_csv():
    all_contacts =[]
    for category,group in contact.items():
        for name,details in group.items():
            all_contacts.append({'Category':category,'Name': name, **details})
            if all_contacts:
                df=pd.DataFrame(all_contacts)
                df.to_csv("contacts.csv",index ='False')
                print("Contacts saved as")