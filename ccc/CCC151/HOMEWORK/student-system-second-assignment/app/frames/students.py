from PyQt5.QtWidgets import QFrame, QTableWidgetItem, QLineEdit
from PyQt5.uic import loadUi
from ..db import conn, cursor
from PyQt5.QtCore import Qt

class StudentFrame(QFrame):
    def __init__(self, parent):
        self.parent = parent 
        super().__init__(parent)
        loadUi("./app/ui/students_frame.ui", self)
        self.setGeometry(0, 110, 1000, 490)
        self.student_table.setColumnWidth(0, 90)
        self.student_table.setColumnWidth(1, 220)
        self.student_table.setColumnWidth(2, 100)
        self.student_table.setColumnWidth(3, 80)
        self.student_table.setColumnWidth(4, 120)
        self.cancel_button.hide()
        self.delete_button.hide()
        self.save_button.hide()
        self.edit_button.hide()
        self.no_students.hide()
        self.search_tab.textChanged.connect(self.on_searching)

        self.edit_button.clicked.connect(self.on_edit_button)
        self.create_button.clicked.connect(self.on_create_button)
        self.new_button.clicked.connect(self.on_new_button)
        self.save_button.clicked.connect(self.on_save_button)
        self.student_table.itemSelectionChanged.connect(self.on_item_select)
        self.delete_button.clicked.connect(self.on_delete_button)
        self.initialize_students()

    def on_item_select(self):
        self.create_button.hide()
        self.cancel_button.hide()
        self.save_button.hide()
        self.edit_button.show()
        self.delete_button.show()

        self.id_year.setEnabled(False)
        self.id_number.setEnabled(False)
        self.last_name.setEnabled(False)
        self.first_name.setEnabled(False)
        self.middle_name.setEnabled(False)
        self.gender.setEnabled(False)
        self.year_level.setEnabled(False)
        self.course.setEnabled(False)
        

        try: _id = self.student_table.item(self.student_table.selectedItems()[0].row(), 0).text()
        except: return
        cursor.execute("SELECT * FROM students WHERE id = %s", (_id,))
        _id, last_name, first_name, middle_name, gender, year_level, course = cursor.fetchone()
        self.current_selected_student = {"_id": _id, "last_name": last_name, "first_name": first_name}
        self.id_year.setText(_id[:4]); self.id_number.setText(_id[5:])
        self.last_name.setText(last_name); self.first_name.setText(first_name); self.gender.setText(gender)
        self.year_level.setCurrentIndex(year_level); self.course.setCurrentIndex([self.course.itemText(i) for i in range(self.course.count())].index("No Course" if course is None else course))

    def on_searching(self, text):
        if not len(text): 
            self.initialize_students()
            return
        
        self.student_table.clearContents()
        self.no_students.hide()
        if text.lower() == "not enrolled":
            cursor.execute("SELECT id, last_name, first_name, program, year_level FROM students WHERE program = null")
        elif text.lower() == "enrolled":
            cursor.execute("SELECT id, last_name, first_name, program, year_level FROM students WHERE program != null")
        elif text.lower().isdigit() and int(text) <= 4:
            cursor.execute("SELECT id, last_name, first_name, program, year_level FROM students WHERE year_level = %s", (int(text),))
        else:
            cursor.execute(f"SELECT id, last_name, first_name, program, year_level FROM students WHERE id LIKE %s OR last_name LIKE %s OR first_name LIKE %s OR middle_name LIKE %s OR gender LIKE %s OR program LIKE %s", (f"%{text}%",f"%{text}%",f"%{text}%",f"%{text}%",f"%{text}%",f"%{text}%",))
        students = cursor.fetchall()
        if not len(students):
            self.no_students.setText("No matches.")
            self.no_students.show()
            return
        for idx, (_id, last_name, first_name, program, year_level) in enumerate(students):
            self.student_table.insertRow(idx)
            self.student_table.setItem(idx, 0, QTableWidgetItem(_id))
            self.student_table.setItem(idx, 1, QTableWidgetItem(f"{last_name}, {first_name}"))
            self.student_table.setItem(idx, 2, QTableWidgetItem("No Program" if program is None else program))
            self.student_table.setItem(idx, 3, QTableWidgetItem(f"{year_level}"))
            self.student_table.setItem(idx, 4, QTableWidgetItem("ENROLLED" if program is not None else "NOT ENROLLED"))
        self.no_students.hide()

    def refresh_count(self):
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        self.parent.total_students.setText(f"TOTAL STUDENTS: {len(students)}")

    def delete_student(self):
        cursor.execute("DELETE FROM students WHERE id = %s", (f"{self.id_year.text()}-{self.id_number.text()}",))
        self.initialize_students()
        self.student_table.clearSelection()
        self.on_new_button()
        self.refresh_count()

    def on_delete_button(self):
        from . import ChoiceMessage
        ChoiceMessage("Are you sure you \nwant to delete \nthis student?", self.delete_student, self)

    def on_edit_button(self):
        self.edit_button.hide()
        self.save_button.show()
        self.last_name.setEnabled(True)
        self.first_name.setEnabled(True)
        self.middle_name.setEnabled(True)
        self.gender.setEnabled(True)
        self.year_level.setEnabled(True)
        self.course.setEnabled(True)

    def on_save_button(self):
        from . import Message
        if any(not len(i.text()) for i in [self.last_name, self.first_name]):
            if self.year_level.currentText() == "Year Level*" or self.course == "Course*":
                Message("Missing Fields!", self)
            else:
                Message("Missing Fields!", self)
            return 
        middle_name = None if not len(self.middle_name.text()) else self.middle_name.text().upper()

        cursor.execute("SELECT * FROM students WHERE last_name = %s AND first_name = %s", (self.last_name.text().upper(), self.first_name.text().upper()))
        result = cursor.fetchone()
        if result is not None:
            if self.last_name.text().upper() != self.current_selected_student["last_name"] and self.first_name.text().upper() != self.current_selected_student["first_name"]:
                
                Message("Similar first and last \nname detected.\nAction failed.", self)
                return
        
        cursor.execute(
            "UPDATE students SET last_name = %s, first_name = %s, middle_name = %s, gender = %s, year_level = %s, program = %s WHERE id = %s",
            (   self.last_name.text().upper(), 
                self.first_name.text().upper(), 
                middle_name, 
                self.gender.text().upper(), 
                int(self.year_level.currentText()[:1]), 
                self.course.currentText() if self.course.currentText() != "No Course" else None, 
                f"{self.id_year.text()}-{self.id_number.text()}",
            )
        )
        self.initialize_students()
        Message("Student Edited\nSuccessfully!", self)
    
    def on_create_button(self):
        from . import Message
        print(self.year_level.currentText())
        if any(not len(i.text()) for i in [self.id_year, self.id_number, self.last_name, self.first_name]):
            if self.year_level.currentText() == "Year Level*" or self.course == "Course*":
                Message("Missing Fields!", self)
            else:
                Message("Missing Fields!", self)
            return 
        
        if not len(self.id_year.text()) == 4 or not self.id_year.text().isdigit():
            Message("YEAR ID must be \na number and only \nhas 4 digits.", self)
            return
        if not len(self.id_number.text()) == 4 or not self.id_number.text().isdigit():
            Message("ID NUMBER must be \na number and only \nhas 4 digits.", self)
            return


        cursor.execute("SELECT EXISTS(SELECT 1 FROM students WHERE id = %s) AS id_exists, EXISTS (SELECT 1 FROM students WHERE last_name = %s AND first_name = %s)", (f"{self.id_year.text()}-{self.id_number.text()}",self.last_name.text().upper(), self.first_name.text().upper()))
        id_exists, name_exists = cursor.fetchone()
        if id_exists:
            return Message(f"Student with an ID of {self.id_year.text()}-{self.id_number.text()}\nalready exists.", self)
        if name_exists:
            return Message(f"Another student with this full name has been found")
        
        middle_name = None if not len(self.middle_name.text()) else self.middle_name.text().upper()

        cursor.execute(
            "INSERT INTO students (id, last_name, first_name, middle_name, gender, year_level, program) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (f"{self.id_year.text()}-{self.id_number.text()}", self.last_name.text().upper(), self.first_name.text().upper(), middle_name, self.gender.text().upper(), int(self.year_level.currentText()[:1]), self.course.currentText() if self.course.currentText() != "No Course" else None)
        )
        self.initialize_students()
        Message("Student Added\nSuccessfully!", self)
        self.no_students.hide()
        self.refresh_count()

    def initialize_students(self):
        self.no_students.hide()
        cursor.execute("SELECT id, last_name, first_name, program, year_level FROM students")
        self.student_table.clearContents()
        students = cursor.fetchall()
        if not len(students):
            self.no_students.setText("No Students. Try Adding One!")
            self.no_students.show()
        for idx, (_id, last_name, first_name, program, year_level) in enumerate(students):
            self.student_table.insertRow(idx)
            self.student_table.setItem(idx, 0, QTableWidgetItem(_id))
            self.student_table.setItem(idx, 1, QTableWidgetItem(f"{last_name}, {first_name}"))
            self.student_table.setItem(idx, 2, QTableWidgetItem("No Program" if program is None else program))
            self.student_table.setItem(idx, 3, QTableWidgetItem(f"{year_level}"))
            self.student_table.setItem(idx, 4, QTableWidgetItem("ENROLLED" if program is not None else "NOT ENROLLED"))


    def on_new_button(self): 
        self.create_button.show()
        self.save_button.hide()
        self.cancel_button.hide()
        self.edit_button.hide()
        self.id_year.setEnabled(True)
        self.id_number.setEnabled(True)
        self.last_name.setEnabled(True)
        self.first_name.setEnabled(True)
        self.middle_name.setEnabled(True)
        self.gender.setEnabled(True)
        self.year_level.setEnabled(True)
        self.course.setEnabled(True)

        self.student_table.clearSelection()

        self.student_title.setText("NEW STUDENT")
        self.id_year.clear()
        self.id_number.clear()
        self.last_name.clear()
        self.first_name.clear()
        self.middle_name.clear()
        self.gender.clear()
        self.course.setCurrentIndex(0)
        self.year_level.setCurrentIndex(0)

