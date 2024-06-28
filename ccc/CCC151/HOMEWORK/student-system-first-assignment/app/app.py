import tkinter as tk
import ttkbootstrap as ttk 
from .db import programs, students
from .components import StudentInfo, ProgramInfo

class StudentTable(ttk.Treeview):
	def __init__(self, master):
		super().__init__(
			master=master, 
			bootstyle='dark', 
			height=12,
			columns=('ID', 'NAME', 'SEX', 'PROGRAM', 'YEAR_LEVEL'), show='headings'
		)
		self.heading('ID', text='ID')
		self.heading('NAME', text='NAME')
		self.heading('SEX', text='SEX')
		self.heading('PROGRAM', text='PROGRAM')
		self.heading('YEAR_LEVEL', text='YEAR LEVEL')
		
		self.column('ID', width=100)
		self.column('NAME', width=250)
		self.column('SEX', width=130)
		self.column('PROGRAM', width=100)
		self.column('YEAR_LEVEL', width=80)


class ProgramTable(ttk.Treeview):
	def __init__(self, master):
		super().__init__(
			master=master, 
			bootstyle='secondary', 
			height=12,
			columns=('CODE', 'NAME'), show='headings'
		)
		self.heading('CODE', text='CODE')
		self.heading('NAME', text='NAME')

		self.column('CODE', width=100)
		self.column('NAME', width=500)

class MainWindow(tk.Tk):
	def __init__(self):
		super().__init__()
		self.style = ttk.Style("vapor")
		self.title("Simple Student Information System")
		self.resizable(False, False)
		window_width = 1000
		window_height = 600
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		position_top = int(screen_height / 2 - window_height / 2)
		position_right = int(screen_width / 2 - window_width / 2)

		self.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

		self.students_tab()
		self.programs_tab()
		self.refresh_program_table()
		self.refresh_student_table()

	def delete_student_data(self):
		id, name, sex, program, year_level = self.students_table.item(self.students_table.selection(), 'values')
		students.remove(id)
		self.dialog(f"Successfully Deleted\nStudent #{id}")
		self.refresh_student_table()

	def confirmation(self, text, func):

		def del_student():
			func()
			toplevel.destroy()

		toplevel = ttk.Toplevel(self)
		toplevel.title("Confirmation")
		window_width = 300
		window_height = 500
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		position_top = int(screen_height / 2 - window_height / 2)
		position_right = int(screen_width / 2 - window_width / 2)

		ttk.Label(toplevel, text=text).pack(side='top', pady=30)
		buttons_frame = ttk.Frame(toplevel)
		yes_button = ttk.Button(buttons_frame, text="Yes", bootstyle='secondary', width=10, command=del_student)
		yes_button.pack(side='left', padx=10)
		cancel_button = ttk.Button(buttons_frame, text="Cancel", bootstyle='danger', width=10, command=toplevel.destroy)
		cancel_button.pack(side='right', padx=10)
		buttons_frame.pack(side='bottom', padx=20, pady=20, fill='x')
		toplevel.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

	def dialog(self, text):
		toplevel = ttk.Toplevel(self)
		toplevel.title("Message")
		window_width = 300
		window_height = 500
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		position_top = int(screen_height / 2 - window_height / 2)
		position_right = int(screen_width / 2 - window_width / 2)

		ttk.Label(toplevel, text=text).pack(side='top', pady=30)

		ttk.Button(toplevel, text='Ok', width=30, command=toplevel.destroy).pack(side='bottom', pady=10)
		toplevel.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')


	def students_tab(self):

		self.students_frame = tk.Frame(self)
		self.student_buttons = tk.Frame(self.students_frame)
		self.student_label = ttk.Label(self.student_buttons, text="STUDENTS", bootstyle='info', font=('Default', 15))
		self.student_label.pack(padx=10, pady=10, side='top')
		self.new_student_button = ttk.Button(self.student_buttons, bootstyle='primary', text="New Student", width=20, command=self.new_student_button_callback)
		self.new_student_button.pack(padx=10, pady=10, side='top')
		self.edit_student_button = ttk.Button(self.student_buttons, bootstyle='secondary', text='Edit Student', width=20, command=self.edit_student_button_callback)
		self.edit_student_button.pack(padx=10, pady=10, side='top')
		self.delete_student_button = ttk.Button(self.student_buttons, bootstyle='danger', text='Delete Student', width=20, command=self.delete_student_button_callback)
		self.delete_student_button.pack(padx=10, pady=10, side='top')

		self.students_table = StudentTable(self.students_frame)
		self.student_buttons.pack(side='left')
		self.student_key_search = tk.StringVar()
		self.student_search_tab = ttk.Entry(self.students_frame, width=80, textvariable=self.student_key_search)
		self.student_search_tab.pack(pady=10)
		self.students_table.pack(side='left', padx=10, pady=10, fill='x', expand=True)
		self.students_frame.pack(fill='x')

		self.student_key_search.trace_add("write", self.student_search)

	def student_search(self, *args):
		self.refresh_student_table(self.student_key_search.get())

	def refresh_student_table(self, keyword=None):
		self.students_table.delete(*self.students_table.get_children())
		data = students.get_all()
		for idx, student in enumerate(data):
			if keyword is not None:
				if not any(keyword.upper() in x for x in list(student.values())):
					continue
			if not student["PROGRAM"] in programs.get_program_ids()[1:]:
				student["PROGRAM"] = 'NOT ENROLLED'
			self.students_table.insert('', 'end', text=str(idx), values=[v for v in list(student.values())])

	def new_student_button_callback(self):
		StudentInfo(self, 'new')

	def edit_student_button_callback(self):
		if not self.students_table.selection():
			return self.dialog("Please select an item\nfrom the students first.")
		else:
			id, name, sex, program, year_level = self.students_table.item(self.students_table.selection(), 'values')
			StudentInfo(self, 'edit', {"ID": id, "NAME": name, "SEX": sex, "PROGRAM": program, "YEAR LEVEL": year_level})


	def delete_student_button_callback(self):
		self.confirmation(f"Do you wish to delete {self.students_table.item(self.students_table.selection(), 'values')[0]}?", self.delete_student_data)


	def programs_tab(self):
		self.program_frame = tk.Frame(self)
		self.program_buttons = tk.Frame(self.program_frame)
		self.program_label = ttk.Label(self.program_buttons, text="PROGRAMS", bootstyle='light', font=('Default', 15))
		self.program_label.pack(padx=10, pady=10, side='top')
		self.new_program_button = ttk.Button(self.program_buttons, bootstyle='primary', text="New Program", width=20, command=self.new_program_button_callback)
		self.new_program_button.pack(padx=10, pady=10, side='top')
		self.edit_program_button = ttk.Button(self.program_buttons, bootstyle='secondary', text='Edit Program', width=20, command=self.edit_program_button_callback)
		self.edit_program_button.pack(padx=10, pady=10, side='top')
		self.delete_program_button = ttk.Button(self.program_buttons, bootstyle='danger', text='Delete Program', width=20, command=self.delete_program_button_callback)
		self.delete_program_button.pack(padx=10, pady=10, side='top')

		self.program_table = ProgramTable(self.program_frame)
		self.program_buttons.pack(side='right')
		self.program_key_search = tk.StringVar()
		self.program_search_tab = ttk.Entry(self.program_frame, width=80, textvariable=self.program_key_search)
		self.program_search_tab.pack(pady=10)
		self.program_table.pack(side='right', padx=10, pady=10, fill='x', expand=True)
		self.program_frame.pack(fill='x')

		self.program_key_search.trace_add("write", self.program_search)

	def program_search(self, *args):
		self.refresh_program_table(self.program_key_search.get())

	def refresh_program_table(self, keyword=None):
		self.program_table.delete(*self.program_table.get_children())
		data = programs.get_all()
		for idx, program in enumerate(data):
			if keyword is not None:
				if not any(keyword.upper() in x for x in list(program.values())):
					continue
			self.program_table.insert('', 'end', text=str(idx), values=[v for v in list(program.values())])

	def new_program_button_callback(self):
		ProgramInfo(self, 'new')

	def edit_program_button_callback(self):
		if not self.program_table.selection():
			return self.dialog("Please select an item\nfrom the program table first.")
		else:
			id, name = self.program_table.item(self.program_table.selection(), 'values')
			ProgramInfo(self, 'edit', {"ID": id, "NAME": name})

	def delete_program_data(self):
		id, name= self.program_table.item(self.program_table.selection(), 'values')
		programs.remove(id)
		self.dialog(f"Successfully Deleted\n{id} Course")
		self.refresh_student_table()
		self.refresh_program_table()

	def delete_program_button_callback(self):
		self.confirmation(f"Do you wish to delete {self.program_table.item(self.program_table.selection(), 'values')[0]} Program?", self.delete_program_data)

	def start(self):
		self.mainloop()