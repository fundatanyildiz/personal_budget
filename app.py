from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import tkcalendar

import model


class MyGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Personal Budget App')
        self.root.geometry("900x800")

        self.label1 = Label(self.root, text='Transaction Name')
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.transaction = Entry(self.root, font=('Arial', 18))
        self.transaction.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = Label(self.root, text='Transaction Type')
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.type = ttk.Combobox(self.root, font=('Arial', 18), values=["Income", "Expense"])
        self.type.grid(row=1, column=1, padx=10, pady=10)

        self.label3 = Label(self.root, text='Planned Budget')
        self.label3.grid(row=2, column=0, padx=10, pady=10)

        self.planned_bud = Entry(self.root, font=('Arial', 18))
        self.planned_bud.grid(row=2, column=1, padx=10, pady=10)

        self.label4 = Label(self.root, text='Actual Budget')
        self.label4.grid(row=3, column=0, padx=10, pady=10)

        self.actual_bud = Entry(self.root, font=('Arial', 18))
        self.actual_bud.grid(row=3, column=1, padx=10, pady=10)

        self.label5 = Label(self.root, text='Transaction Date')
        self.label5.grid(row=4, column=0, padx=10, pady=10)

        self.date = tkcalendar.DateEntry(self.root, selectmode='day')
        self.date.grid(row=4, column=1, padx=10, pady=10)
        # Create buttons
        self.submit = Button(self.root, text='Submit Data', command=self.submit_data)
        self.submit.grid(row=5, column=0, padx=10, pady=15)

        self.submit = Button(self.root, text='Show Data', command=self.show_data)
        self.submit.grid(row=5, column=1, padx=10, pady=15)

        self.view = Button(self.root, text='View Graphics', command=self.show_chart)
        self.view.grid(row=6, column=0, padx=10, pady=15)

        #  data table
        header = ['transaction_name', 'transaction_type', 'planned_budget', 'actual_budget', 'transaction_date',
                  'update_time']
        self.table = ttk.Treeview(self.root, columns=header, show='headings', height=12)
        self.table.column('transaction_name', width=120)
        self.table.column('transaction_type', width=120)
        self.table.column('planned_budget', width=100)
        self.table.column('actual_budget', width=100)
        self.table.column('transaction_date', width=150)
        self.table.column('update_time', width=200)
        # column heading
        for c in header:
            self.table.heading(c, text=c.title())
        self.table.grid(row=7, column=0, padx=25, pady=25, columnspan=10)

        self.root.mainloop()

    def submit_data(self):
        # insert data to db
        con = model.create_connection(model.filename)
        now = datetime.now()
        timestamp = now.strftime('%Y.%m.%d %H:%M:%S %p')
        con.cursor().execute(model.sql_insert_data,
                             (self.transaction.get(), self.type.get(), self.planned_bud.get(), self.actual_bud.get(),
                              self.date.get(), timestamp))
        con.commit()
        con.close()

    def show_data(self):
        # show data on GUI
        con = model.create_connection(model.filename)
        cur = con.cursor()
        cur.execute(model.sql_select_table_data)
        rows = cur.fetchall()
        self.table.delete(*self.table.get_children())
        for i in rows:
            self.table.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5]))
        con.close()

    def show_chart(self):
        con = model.create_connection(model.filename)
        df = pd.read_sql_query(model.sql_select_table_data, con)
        df.groupby(['transaction_type']).sum().plot(kind='pie', y='planned_budget', autopct='%1.0f%%')
        df.groupby(['transaction_type']).sum().plot(kind='pie', y='actual_budget', autopct='%1.0f%%')
        ex = df.groupby(['transaction_type']).get_group('Expense')
        ex.plot(kind='pie', y='actual_budget', labels=ex['transaction_name'], autopct='%1.0f%%')
        plt.show()


model.initialize_db()
MyGUI()
