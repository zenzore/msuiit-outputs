from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5 import uic
from enum import Enum
from .db import conn, cursor

from .frames import CourseFrame, StudentFrame

class State(Enum):
    students = 1 
    courses = 2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Student Information System")
        uic.loadUi("./app/ui/main_window.ui", self)
        self.setWindowTitle("App")
        self.setGeometry(0, 0, 1000, 600)
        self.center()
        self.toggle_button.clicked.connect(self.toggle_state)
        self.state = State.courses
        self.course_frame = CourseFrame(self)
        self.student_frame = StudentFrame(self)
        self.student_frame.hide()
        self.refresh_course_options()

        self.student_frame.refresh_count()
        self.course_frame.refresh_count()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        x = (screen.width() - size.width()) // 2
        y = (screen.height() - size.height()) // 2
        self.move(x, y)

    def refresh_course_options(self):
        self.student_frame.course.clear()
        items = ["Course*", "No Course"]
        cursor.execute("SELECT id FROM programs")
        programs = cursor.fetchall()
        for program in programs:
            items.append(program[0])
        self.student_frame.course.addItems(items)

    def toggle_state(self):
        match self.state:
            case State.courses:
                # TODO: toggle to students
                self.toggle_button.setText("Students")
                self.state = State.students 
                self.student_frame.show()
                self.course_frame.hide()
            case State.students:
                # TODO: toggle to courses
                self.toggle_button.setText("Courses")
                self.state = State.courses
                self.course_frame.show()
                self.student_frame.hide()

    
            

        
        