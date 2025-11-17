import pandas as pd

# Example contact dictionary
contact = {
    "Family": {
        "Abin": {"Phone": "123456789", "Email": "abin@gmail.com"},
        "Manita": {"Phone": "987654321", "Email": "manita@gmail.com"}
    },
    "Friends": {
        "Rajan": {"Phone": "555555555", "Email": "rajan@gmail.com"}
    }
}

def save_contacts_to_csv(contact):
    all_contacts = []
    
    # Loop through categories and people
    for category, group in contact.items():
        for name, details in group.items():
            # Merge category, name, and other details into one dictionary
            all_contacts.append({'Category': category, 'Name': name, **details})
    
    # Only save if there is at least one contact
    if all_contacts:
        df = pd.DataFrame(all_contacts)  # Create a DataFrame
        df.to_csv("contacts.csv", index=False)  # Save to CSV
        print("Contacts saved as contacts.csv")
    else:
        print("No contacts to save!")

# Call the function
save_contacts_to_csv(contact)
