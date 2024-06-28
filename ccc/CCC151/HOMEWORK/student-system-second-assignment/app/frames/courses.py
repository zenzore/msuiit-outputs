from PyQt5.QtWidgets import QFrame, QTableWidgetItem
from PyQt5.uic import loadUi
from ..db import conn, cursor


class CourseFrame(QFrame):
    def __init__(self, parent):
        self.parent = parent 
        super().__init__(parent)
        loadUi("./app/ui/courses_frame.ui", self)
        self.setGeometry(0, 110, 1000, 490)
        self.program_table.setColumnWidth(0, 100)
        self.program_table.setColumnWidth(1, 492)
        self.save_button.hide()
        self.no_programs.hide()
        self.edit_button.hide()
        self.cancel_button.hide()
        self.delete_button.hide()
        self.program_table.itemSelectionChanged.connect(self.on_item_select)
        self.new_button.clicked.connect(self.on_new_button)
        self.edit_button.clicked.connect(self.on_edit_button)
        self.create_button.clicked.connect(self.on_create_button)
        self.delete_button.clicked.connect(self.on_delete_button)
        self.search_tab.textChanged.connect(self.on_searching)
        self.save_button.clicked.connect(self.on_save_button)
        self.initialize_programs()

    def on_searching(self, text):
        self.no_programs.hide()
        if not len(text): return self.initialize_programs()
        self.program_table.clearContents()
        cursor.execute("SELECT * FROM programs WHERE id LIKE %s OR name LIKE %s", (f"%{text}%", f"%{text}%"))
        programs = cursor.fetchall()
        if not len(programs):
            self.no_programs.show()
            return
        for idx, (course_id, course_name) in enumerate(programs):
            self.program_table.insertRow(idx)
            self.program_table.setItem(idx, 0, QTableWidgetItem(course_id))
            self.program_table.setItem(idx, 1, QTableWidgetItem(course_name))

    def on_create_button(self):
        from . import Message
        if not len(self.program_code.text()) or not len(self.program_name.text()):
            Message("There are some mising fields.", self)
            return
        course_id, course_name = self.program_code.text(), self.program_name.text()
        cursor.execute("SELECT * FROM programs WHERE id = %s OR name = %s", (course_id.upper(), course_name.upper()))
        course_exists = cursor.fetchone()
        if course_exists is not None:
            Message("Course Exists!", self)
            return 
        cursor.execute("INSERT INTO programs (id, name) VALUES (%s, %s)", (course_id.upper(), course_name.upper()))
        self.program_table.insertRow(0)
        self.program_table.setItem(0, 0, QTableWidgetItem(course_id.upper()))
        self.program_table.setItem(0, 1, QTableWidgetItem(course_name.upper()))
        self.refresh_count()
        self.no_programs.hide()
        Message("Program Created Successfully!", self)
        self.program_code.clear(); self.program_name.clear()
        self.parent.refresh_course_options()
        

    def refresh_count(self):
        cursor.execute("SELECT * FROM PROGRAMS")
        programs = cursor.fetchall()
        self.parent.total_courses.setText(f"TOTAL PROGRAMS: {len(programs)}")

    def delete_program(self):
        cursor.execute("DELETE FROM programs WHERE id = %s", (self.program_code.text(),))
        
        cursor.execute("UPDATE students SET program = %s WHERE program = %s", (None, self.program_code.text()))
        self.parent.student_frame.initialize_students()
        self.program_table.removeRow(self.program_table.selectedItems()[0].row())
        self.program_table.clearSelection()
        self.refresh_count()
        

    def on_delete_button(self):
        from . import ChoiceMessage
        ChoiceMessage("Are you sure you \nwant to delete \nthis program?", self.delete_program, self)

    def on_edit_button(self):
        self.edit_button.hide()
        self.save_button.show()
        self.program_code.setEnabled(True); self.program_name.setEnabled(True)

    def on_new_button(self):
        self.program_code.setEnabled(True); self.program_name.setEnabled(True)
        self.cancel_button.hide()
        self.program_title.setText("New Program")
        self.program_code.clear()
        self.program_name.clear()
        self.create_button.show()
        self.delete_button.hide()
    
    def on_save_button(self):
        from . import Message
        if not len(self.program_code.text()) or not len(self.program_name.text()):
            Message("There are some missing fields.", self)
            return
        course_id, course_name = self.program_code.text(), self.program_name.text()
        # SELECT COUNT(*) FROM programs WHERE id = %s AND name = %s
        cursor.execute("SELECT COUNT(*) FROM programs WHERE id = %s AND name = %s", (course_id.upper(), course_name.upper()))
        course_exists = cursor.fetchone()
        if course_exists[0] != 0:
            if course_id.lower() == self.current_selected_row[0].lower() and course_name.lower() == self.current_selected_row[1].lower():
                Message("No changes were made.", self)
                self.save_button.hide()
                self.edit_button.show()
            else:
                Message("That course already exists!", self)
            return 
        cursor.execute("UPDATE programs SET id = %s, name = %s WHERE id = %s", (self.program_code.text(), self.program_name.text(), course_id))
        Message("Program Successfully edited.", self)
        self.program_code.clear(); self.program_name.clear()
        self.parent.refresh_course_options()
        self.refresh_count()
        self.edit_button.show()
        self.save_button.hide()
        self.initialize_programs()
        
    

    def initialize_programs(self):
        cursor.execute("SELECT * FROM programs")
        self.program_table.clearContents()
        programs = cursor.fetchall()
        if not len(programs):
            self.no_programs.show()
        for idx, (course_id, course_name) in enumerate(programs):
            self.program_table.insertRow(idx)
            self.program_table.setItem(idx, 0, QTableWidgetItem(course_id))
            self.program_table.setItem(idx, 1, QTableWidgetItem(course_name))
        self.refresh_count()
        

    def on_item_select(self):
        self.create_button.hide()
        self.cancel_button.hide()
        self.save_button.hide()
        self.edit_button.show()

        self.program_code.setEnabled(False)
        self.program_name.setEnabled(False)

        self.program_title.setText("Program Information")
        try: _id = self.program_table.item(self.program_table.selectedItems()[0].row(), 0).text()
        except: return
        cursor.execute("SELECT * FROM programs WHERE id = %s", (_id,))
        course_id, course_name = cursor.fetchone()
        self.current_selected_row = [course_id, course_name]
        self.program_code.setText(course_id)
        self.program_name.setText(course_name)
        self.delete_button.show()
    
        