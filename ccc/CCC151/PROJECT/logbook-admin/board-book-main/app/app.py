from PyQt5.QtWidgets import QMainWindow, QFrame, QListWidgetItem, QMessageBox, QTableWidgetItem
from PyQt5.uic import loadUi
import db

class Item(QListWidgetItem):
    def __init__(self, text, item_id):
        super().__init__(text)
        self.item_id = item_id 
    
    def id(self):
        return self.item_id


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BoardBook App")
        loadUi("./app/ui/window.ui", self)

        self.log_type = {"out": "in", "in": "out"}
        self.all_boarders = {"Boarder to Visit": 0}
        self.boarder_ids = []
        self.setGeometry(0, 0, 1263, 600)
        self.setFixedSize(1263, 600)

        self.boarder_search.textChanged.connect(self.on_boarder_search)
        self.boarder_button.clicked.connect(self.on_boarder_sign_in)
        self.visitor_lastname.textChanged.connect(self.on_visitor_lastname_changed)
        self.visitor_button.clicked.connect(self.on_visitor_sign_in)
        self.visitor_list.clicked.connect(self.on_visitor_list_selection)
        self.logs.setColumnWidth(0, 150)
        self.logs.setColumnWidth(1, 150)
        self.logs.setColumnWidth(2, 200)

        self.refresh_logs()
        self.refresh_boarders()

    def on_visitor_sign_in(self):
        last_name = self.visitor_lastname.text()
        first_name = self.visitor_firstname.text()
        middle_name = self.visitor_middlename.text()
        phone = self.visitor_phone.text()
        boarder_visit = self.visitor_boarder.currentIndex()
        visitor_reason = self.visitor_reason.text()
        if not len(last_name):
            QMessageBox.warning(self, "Last Name Required", "Last name must not be empty.")
            return 
        if not len(first_name):
            QMessageBox.warning(self, "First Name Required", "First name must not be empty.")
            return
        if not len(visitor_reason):
            QMessageBox.warning(self, "Reason for Visit Required", "Reason to visit must not be empty.")
            return
        if boarder_visit == 0:
            QMessageBox.warning(self, "No Selected Boarder", "Please select a boarder to visit.")
            return 
        boarder_id = self.boarder_ids[boarder_visit-1]
        db.cursor.execute("select id from visitor where last_name = %s and first_name = %s", (last_name.lower(), first_name.lower()))
        visitor = db.cursor.fetchone()
        if visitor is None:
            
            if not len(middle_name): middle_name = None
            if len(phone):
                if not phone.isdigit():
                    return QMessageBox.warning(self, "Invalid Phone", "Phone must be all numbers.")
            else:
                phone = None
            db.cursor.execute("insert into visitor (last_name, first_name, middle_name, phone_number) values (%s, %s, %s, %s)", (last_name, first_name, middle_name, phone))
        else:
            db.cursor.execute("update visitor set last_name = %s, first_name = %s, middle_name = %s, phone_number = %s where id = %s", (last_name.lower(), first_name.lower(), middle_name.lower(), phone.lower(), visitor[0]))
        
        db.cursor.execute("select id from visitor where last_name = %s and first_name = %s", (last_name.lower(), first_name.lower()))
        visitor = db.cursor.fetchone()

        db.cursor.execute('insert into visitor_logs (boarder, visitor) VALUES (%s, %s)', (boarder_id, visitor[0]))
        QMessageBox.information(self, "Success!", "Thank you for visiting!")
        self.refresh_boarders()
        self.refresh_logs()
        self.clean_all()

    def clean_all(self):
        self.visitor_lastname.clear()
        self.visitor_firstname.clear()
        self.visitor_boarder.setCurrentIndex(0)
        self.visitor_middlename.clear()
        self.visitor_phone.clear()
        self.visitor_reason.clear()

        
    
    def on_visitor_list_selection(self):
        item = self.visitor_list.selectedItems()[0].id()
        db.cursor.execute("select last_name, first_name, middle_name, phone_number from visitor where id = %s", (item,))
        last_name, first_name, middle_name, phone_number = db.cursor.fetchone()
        self.visitor_lastname.setText(last_name)
        self.visitor_firstname.setText(first_name)
        self.visitor_middlename.setText(middle_name)
        self.visitor_phone.setText(phone_number)
        self.visitor_list.clear()

        

    def on_visitor_lastname_changed(self, text):
        if not len(text):
            self.visitor_list.clear()
            return 
        db.cursor.execute("SELECT id, last_name, first_name from visitor where last_name like %s", (f"%{text}%".lower(),))
        visitors = db.cursor.fetchall()
        self.visitor_list.clear()
        if not len(visitors):
            self.visitor_list.clear() 
            return 
        for _id, last_name, first_name in visitors:
            self.visitor_list.addItem(Item(f"{last_name.upper()}, {first_name.upper()}", _id))
        
        
    def on_boarder_search(self, text):
        if not len(text):
            return self.boarder_list.clear()
        self.boarder_list.clear()
        text = f"%{text}%".lower()
        db.cursor.execute("select id, last_name, first_name from boarder WHERE last_name like %s or first_name like %s", (text, text))
        boarders = db.cursor.fetchall()
        if len(boarders):
            for _id, last_name, first_name in boarders:
                self.boarder_list.addItem(Item(f"{last_name}, {first_name}".upper(), _id))
        else:
            return

    def on_boarder_sign_in(self):
        if not len(self.boarder_list.selectedItems()):
            QMessageBox.information(self, "No selected boarder", "Please search for your name and click your name.")
            return
        db.cursor.execute("SELECT log_type from boarder_logs WHERE boarder = %s ORDER BY log_date DESC", (self.boarder_list.selectedItems()[0].id(),))
        log_type = db.cursor.fetchone()
        next_log = "in"
        if log_type is not None:
            log_type = log_type[0]
            if log_type == "in": next_log = "out"

        db.cursor.execute("INSERT INTO boarder_logs (boarder, log_type) VALUES (%s, %s)", (self.boarder_list.selectedItems()[0].id(), next_log))
        QMessageBox.information(self, f"Sign {next_log.upper()}", f"Sign {next_log.upper()} Successful!")
        self.refresh_logs()
        self.boarder_list.clear()
        self.boarder_search.clear()

    def refresh_logs(self):
        self.logs.clearContents()
        db.cursor.execute("select 'boarder' as source_table, CONCAT(boarder.last_name, ', ', boarder.first_name), log_type, log_date from boarder join boarder_logs on boarder.id = boarder_logs.boarder UNION ALL select 'visitor' as source_table, CONCAT(visitor.last_name, ', ', visitor.first_name)  as visitor_name , CONCAT(boarder.last_name, ', ', boarder.first_name) as boarder_name, log_date from boarder join visitor_logs on boarder.id = visitor_logs.boarder join visitor on visitor_logs.visitor = visitor.id ORDER BY log_date DESC")
        logs = db.cursor.fetchall()
        for idx, (table, col1, col2, log_date) in enumerate(logs):
            self.logs.insertRow(idx)
            log_date = log_date.strftime("%m-%d-%Y %I:%M %p")
            name = col1.split(" ")
            col1 = f"{name[0].upper()} {'.'.join([m[0].upper() for m in name[1:]])}".upper()
            if table == 'boarder':
                self.logs.setItem(idx, 0, QTableWidgetItem(log_date))
                self.logs.setItem(idx, 1, QTableWidgetItem(col1.upper()))
                self.logs.setItem(idx, 2, QTableWidgetItem(col2.upper()))
            else:
                name = col2.split(" ")
                col2 = f"{name[0].upper()} {'.'.join([m[0].upper() for m in name[1:]])}".upper()
                self.logs.setItem(idx, 0, QTableWidgetItem(log_date))
                self.logs.setItem(idx, 1, QTableWidgetItem(col1.upper()))
                self.logs.setItem(idx, 2, QTableWidgetItem(f"VISIT {col2}"))

    def refresh_boarders(self):
        self.visitor_boarder.clear()
        self.boarder_ids = []
        db.cursor.execute("select id, last_name, first_name from boarder")
        boarders = db.cursor.fetchall()
        for idx, (_id, last_name, first_name) in enumerate(boarders):
            self.all_boarders[f"{last_name}, {first_name}"] = idx + 1
            self.boarder_ids.append(_id)
        self.visitor_boarder.addItems(list(self.all_boarders.keys()))
        self.visitor_boarder.setCurrentIndex(0)


            