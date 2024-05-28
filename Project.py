import tkinter as tk
from tkinter import simpledialog

class Trie():
    def __init__(self): 
        self.branches = {}
        self.is_end = False    #Flag to signal end of word
        self.number = None
    
class DirectoryApp(tk.Tk):
    # creating main Window
    def __init__(self):
        super().__init__()
        self.title("Team Sonic App")    #crating Title of window
        self.directory = Directory()

        self.label = tk.Label(self, text="PhoneBook Pro", font=("Helvetica", 20))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.entry_frame = tk.Frame(self)
        self.entry_frame.grid(row=1, column=0, padx=10, pady=10)

        self.name_label = tk.Label(self.entry_frame, text="Enter Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.entry_frame)        #Input bar for name
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.number_label = tk.Label(self.entry_frame, text="Enter Number:")
        self.number_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.number_entry = tk.Entry(self.entry_frame)      #Input bar for number
        self.number_entry.grid(row=1, column=1, padx=5, pady=5)

        #Creating Buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add/Edit Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.display_button = tk.Button(self.button_frame, text="Display All Contacts", command=self.display_contacts)
        self.display_button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        self.message_label = tk.Label(self, text="", fg="black")
        self.message_label.grid(row=2, column=0, columnspan=2, pady=5)

        self.close_button = tk.Button(self, text="Close", command=self.destroy)
        self.close_button.grid(row=3, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get().strip()    #Getting name input
        number = self.number_entry.get().strip()    #getting number input
        # Input error handling
        if len(number) != 11:
            self.show_message("Please enter a valid 11-digit number.", success=False)
            return
        #   processing Input
        self.directory.add_or_edit(name, number)
        self.show_message("Contact added/edited successfully", success=True)
        #   clearing input Tabs
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)

    def search_contact(self):
        # search_input
        prefix = self.name_entry.get().strip()  
        get_lst = self.directory.search_contact(prefix)
        if get_lst == []:
            self.show_message("No contacts found with this name.", success=False)
            return
        # processing input
        if len(get_lst) == 1:
            name, number = get_lst[0]
            self.show_message(f"Name: {name}, Number: {number}", success=True)
        else:
            names = ""
            for i, (name, number) in enumerate(get_lst):
                names += f"{i+1}. {name}\n"
            selected_name = simpledialog.askstring("Selection", f"Did you mean?\n{names}\nEnter the name you want to search for:")
            get_lst = self.directory.search_contact(selected_name)
            name, number = get_lst[0]
            self.show_message(f"Name: {name}, Number: {number}", success=True)

    def delete_contact(self):
        # getting input to be deleted
        name = self.name_entry.get().strip()
        # processing input
        check = self.directory.search_contact(name)
        # Checking and displaying Results
        if check:
            if len(check) == 1:
                name, number = check[0]
                self.show_message(f"Name: {name}, Number: {number}", success=True)
            else:
                names = ""
                for i, (name, number) in enumerate(check):
                    names += f"{i+1}. {name}\n"
                selected_name = simpledialog.askstring("Selection", f"Did you mean?\n{names}\nEnter the name you want to delete:")
                check = self.directory.search_contact(selected_name)
                name, number = check[0]
            self.directory.delete_contact(name)
            self.show_message(f"Contact '{name}' deleted successfully", success=True)
        else:
            self.show_message(f"No contact found with the name '{name}'", success=False)

    def display_contacts(self):
        lst = self.directory.display_contacts() # return a lst of tuple having name and numbers
        if lst: #checks if get_lst is empty
            #count = 0
            contacts = ""
            for name, number in lst:
                #count += 1
                contacts += f"{name}: {number}\n"
            self.show_message(contacts + f"\nTotal number of contacts: {len(lst)}", success=True) #   Display string of all names and numbers
        else:
            self.show_message("No contacts found in the directory", success=False) #if lst is empty
            
    # show_message to Display all errors in red and all successful operations in Green
    def show_message(self, message, success=True):
        if success:
            self.message_label.config(text=message, fg="green")
        else:
            self.message_label.config(text=message, fg="red")

class Directory:

    def __init__(self):
        self.root = Trie()

    def add_or_edit(self, name, number):
        node = self.root
        for letter in name:
            if letter not in node.branches:
                node.branches[letter] = Trie()    #Creating an object as the value
            node = node.branches[letter]
        node.is_end = True                 #Sets end of word to True when the word ends
        node.number = number           #Storing the number of the contact as its attribute

    def search_contact(self, prefix):
        node = self.root
        for letter in prefix:
            if letter not in node.branches:
                return []
            node = node.branches[letter]
        return self.search_helper(node, prefix, [])

    def search_helper(self, node, prefix, outlst):       #Recursively goes into the depth of a node 
        if node.is_end == True:
            outlst.append((prefix, node.number))

        for letter in node.branches:
            self.search_helper(node.branches[letter], prefix + letter, outlst)
        return outlst

    def display_contacts(self):
        return self.display_helper(self.root, '', [])

    def display_helper(self, node, name, outlst):
        if node.is_end == True:     #If the word has ended, it appends a tuple to the output list containing the name and number 
            outlst.append((name, node.number))
        for letter in node.branches:
            self.display_helper(node.branches[letter], name + letter, outlst)      #Goes into depth of each child node to pick word 
        return outlst

    def delete_contact(self, name):
        return self.delete_helper(self.root, name, 0)     #Calls delete_helper to delete contact 

    def delete_helper(self, node, name, index):
        if index == len(name):  #checks if whole name has been deleted and then marks end as True/False
            if not node.is_end:
                return False
            node.is_end = False
            return len(node.branches) == 0
        
        letter = name[index]    
        if letter not in node.branches: #Ends the process if name doesnot exists
            return False

        should_delete_current_node = self.delete_helper(node.branches[letter], name, index + 1) # recursively deletes each node of name
        if should_delete_current_node:
            if len(node.branches[letter].branches) == 0:
                del node.branches[letter]
                return len(node.branches) == 0
        
        return should_delete_current_node

def main():
    app = DirectoryApp()
    app.mainloop()

main()
