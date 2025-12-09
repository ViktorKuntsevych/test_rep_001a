# Ver 001e
# git checkout -b Brainch001b

import tkinter as tk
from tkinter import messagebox

class My_ShoppingList:
    def __init__(self, root):

        self.root = root
        self.root.title("My Shopping List     Retford Computers (c)")
        self.root.geometry("400x600") 
        self.root.config(bg="#f0f0f0") 

        main_frame = tk.Frame(root, padx=15, pady=15, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True)

        input_frame = tk.Frame(main_frame, bg="#f0f0f0")
        input_frame.pack(fill=tk.X, pady=10)

        tk.Label(input_frame, text="Item Name:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.item_name_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=30)
        self.item_name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)


        tk.Label(input_frame, text="Quantity:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.quantity_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=10)
        self.quantity_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        input_frame.columnconfigure(1, weight=1)


        self.add_button = tk.Button(
            main_frame,
            text="Add to List",
            font=("Helvetica", 12, "bold"),
            command=self.add_item_to_list,
            bg="#4CAF50", 
            fg="white",   
            relief=tk.RAISED,
            bd=2
        )
        self.add_button.pack(fill=tk.X, pady=10, ipady=5)


        list_frame = tk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(list_frame, text="Shopping List:", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack(anchor="w")


        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.shopping_list_text = tk.Text(
            list_frame,
            height=15,
            font=("Courier", 12), 
            yscrollcommand=scrollbar.set,
            bg="#ffffff", 
            relief=tk.SUNKEN,
            bd=2
        )
        self.shopping_list_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.shopping_list_text.yview)

    def add_item_to_list(self):

        item_name = self.item_name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()

        if not item_name:
            messagebox.showwarning("Input Error", "Please enter an item name.")
            return
        
        try:
            if not quantity or int(quantity) <=0:
                quantity = "1"
        except ValueError:
            # Input is not a number
            quantity = "1" 

        list_entry = f"{item_name} : {quantity}\n"
        self.shopping_list_text.insert(tk.END, list_entry)

        self.item_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

        self.item_name_entry.focus_set()


if __name__ == "__main__":

    root = tk.Tk()
    app = My_ShoppingList(root)
    root.mainloop()

