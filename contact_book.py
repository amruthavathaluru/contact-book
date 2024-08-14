import tkinter as tk
from tkinter import messagebox, simpledialog
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name and phone and email and address:
        contact = {
            'Name': name,
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        contacts.append(contact)
        update_contact_list()
        clear_fields()
    else:
        messagebox.showerror("Error", "Please enter all contact details.")
def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        contacts.pop(selected_index)
        update_contact_list()
    except IndexError:
        messagebox.showerror("Error", "Select a contact to delete.")
def update_contact():
    try:
        selected_index = contact_list.curselection()[0]
        updated_name = name_entry.get()
        updated_phone = phone_entry.get()
        updated_email = email_entry.get()
        updated_address = address_entry.get()
        contact = {
            'Name': updated_name,
            'Phone': updated_phone,
            'Email': updated_email,
            'Address': updated_address
        }
        contacts[selected_index] = contact
        update_contact_list()
        clear_fields()
    except IndexError:
        messagebox.showerror("Error", "Select a contact to update.")
def search_contact():
    search_query = simpledialog.askstring("Search", "Enter a name or keyword:")
    if search_query:
        search_results = []
        for contact in contacts:
            if search_query.lower() in contact['Name'].lower():
                search_results.append(contact)
        
        if search_results:
            show_search_results(search_results)
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")
def show_search_results(results):
    search_results_window = tk.Toplevel(root)
    search_results_window.title("Search Results")
    results_listbox = tk.Listbox(search_results_window)
    results_listbox.pack()
    for result in results:
        results_listbox.insert(tk.END, f"{result['Name']}: {result['Phone']}")
def view_contact():
    try:
        selected_index = contact_list.curselection()[0]
        selected_contact = contacts[selected_index]
        details = "\n".join([f"{key}: {value}" for key, value in selected_contact.items()])
        messagebox.showinfo("Contact Details", details)
    except IndexError:
        messagebox.showerror("Error", "Select a contact to view.")
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
root = tk.Tk()
root.title("Contact Book")
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()
phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()
address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()
view_button = tk.Button(root, text="View Contact", command=view_contact)
view_button.pack()
search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.pack()
update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack()
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()
contact_list = tk.Listbox(root)
contact_list.pack()
contacts = []
root.mainloop()
