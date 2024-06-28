import tkinter as tk 
import ttkbootstrap as ttk 
from ..db import programs, students


class ProgramInfo(tk.Toplevel):
	def __init__(self, master, mode: str, data: dict = None):
		super().__init__(master=master, width=300, height=300)
		self.mode = mode; self.data = data
		window_width = 300
		window_height = 250
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		position_top = int(screen_height / 2 - window_height / 2)
		position_right = int(screen_width / 2 - window_width / 2)


		self.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
		self.title('New Program' if mode == 'new' else 'Program Information')

		ttk.Label(self, bootstyle='light', font=('Default', 10), text="PROGRAM ID").pack(pady=10)
		self.id_entry = ttk.Entry(self, bootstyle='dark')
		self.id_entry.pack(padx=10, fill='x')

		ttk.Label(self, bootstyle='light', font=('Default', 10), text="PROGRAM NAME").pack(pady=10)
		self.name_entry = ttk.Entry(self, bootstyle='dark')
		self.name_entry.pack(padx=10, fill='x')

		self.buttons_frame = ttk.Frame(self)
		self.create_button = ttk.Button(self.buttons_frame, text="Create" if mode == 'new' else 'Save', bootstyle='secondary', width=10, command=self.create_button_callback)
		self.create_button.pack(side='left', fill='x', padx=10)
		self.cancel_button = ttk.Button(self.buttons_frame, text="Cancel", bootstyle='danger', width=10, command=self.destroy)
		self.cancel_button.pack(side='right', fill='x', padx=10)
		self.buttons_frame.pack(side='bottom', padx=10, pady=20, fill='x')

		if self.data is not None:
			self.id_entry.insert(0, self.data['ID'])
			self.id_entry.configure(state='disabled')
			self.name_entry.insert(0, self.data["NAME"])

	def dialog(self, text):
		toplevel = ttk.Toplevel(self)
		toplevel.title("Error")
		window_width = 300
		window_height = 500
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		position_top = int(screen_height / 2 - window_height / 2)
		position_right = int(screen_width / 2 - window_width / 2)

		ttk.Label(toplevel, text=text).pack(side='top', pady=30)

		ttk.Button(toplevel, text='Ok', width=30, command=toplevel.destroy).pack(side='bottom', pady=10)
		toplevel.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

	def create_button_callback(self):
		id, name = self.id_entry.get(), self.name_entry.get()
		current_data = {"ID": id, "NAME": name}
		if any(not len(x) for x in list(current_data.values())):
			return self.dialog("Missing Fields.")
		if self.mode == 'new':
			if programs.check(id):
				return self.dialog("Program code already exists!")
			programs.insert_one(current_data)
			self.dialog(f"Successfully created\nStudent #{id}")
			self.master.refresh_student_table()
			self.master.refresh_program_table()
			self.destroy()
		else:
			if current_data == self.data:
				return self.dialog("No changes were made.")
			programs.edit(current_data)
			self.dialog(f"Successfully Edited\n'{id}'")
			self.master.refresh_student_table()
			self.master.refresh_program_table()
			self.destroy()



