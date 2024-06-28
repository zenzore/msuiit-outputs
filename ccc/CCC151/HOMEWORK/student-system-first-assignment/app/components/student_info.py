import tkinter as tk
import ttkbootstrap as ttk
from ..db import programs, students


class StudentInfo(ttk.Toplevel):
	def __init__(self, master, mode: str, data: dict=None):
		super().__init__(master=master, width=300, height=500)
		self.data = data
		self.mode = mode
		window_width = 300
		window_height = 500
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		position_top = int(screen_height / 2 - window_height / 2)
		position_right = int(screen_width / 2 - window_width / 2)
		


		self.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
		self.title('New Student' if mode == 'new' else 'Student Information')
		ttk.Label(self, bootstyle='light', font=('Default', 10), text="ID NUMBER").pack(pady=10)
		self.id_entry = ttk.Entry(self, bootstyle='dark')
		self.id_entry.pack(padx=10, fill='x')
		ttk.Label(self, bootstyle='light', font=('Default', 10), text="STUDENT NAME").pack(pady=10)
		self.name_entry = ttk.Entry(self, bootstyle='dark')
		self.name_entry.pack(padx=10, fill='x')
		ttk.Label(self, bootstyle='light', font=('Default', 10), text="STUDENT SEX").pack(pady=10)
		self.sex_option = ttk.Combobox(self, values=["Male", "Female", "Prefer not to say"], state='readonly', bootstyle='dark')
		self.sex_option.pack(fill='x', padx=10)
		ttk.Label(self, bootstyle='light', font=('Default', 10), text="STUDENT PROGRAM").pack(pady=10)
		self.program_option = ttk.Combobox(self, values=programs.get_program_ids(), state='readonly', bootstyle='dark')
		self.program_option.pack(fill='x', padx=10)
		ttk.Label(self, bootstyle='light', font=('Default', 10), text="YEAR LEVEL").pack(pady=10)
		self.yearlevel_option = ttk.Combobox(self, values=["First Year", "Second Year", "Third Year", "Fourth Year"], state='readonly', bootstyle='dark')
		self.yearlevel_option.pack(fill='x', padx=10)

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
			self.sex_option.set(self.data["SEX"])
			self.program_option.set(self.data["PROGRAM"])
			self.yearlevel_option.set(self.data["YEAR LEVEL"])


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
		id, name, sex, program, year_level = self.id_entry.get(), self.name_entry.get(), self.sex_option.get(), self.program_option.get(), self.yearlevel_option.get()
		program = "NOT ENROLLED" if not program in programs.get_program_ids()[1:] else program
		current_data = {"ID": id, "NAME": name, "SEX": sex, "PROGRAM": program, "YEAR LEVEL": year_level}
		if len(id) != 9:
			return self.dialog("Invalid ID format.")
		if any(not len(x) for x in list(current_data.values())):
			return self.dialog("Missing Fields.")
		if self.mode == 'new':
			
			if students.check(id):
				return self.dialog("ID already exists!")
			students.insert_one(current_data)
			self.dialog(f"Successfully created\nStudent #{id}")
			self.master.refresh_student_table()
			self.destroy()
		else:
			if current_data == self.data:
				return self.dialog("No changes were made.")
			else:
				students.edit(current_data)
				self.dialog(f"Successfully Edited\nStudent #{id}")
				self.master.refresh_student_table()
				self.destroy()




