import pandas as pd
import os

class DB:
	def __init__(self, filename: str, columns: list):
		self.columns = columns
		self.filename = f"./app/db/{filename}.csv"
		self.initialize()

	def initialize(self):
		if not os.path.exists(self.filename):
			df = pd.DataFrame(columns=self.columns)
			df.to_csv(self.filename, index=False)

	def get_all(self):
		df = pd.read_csv(self.filename)
		return df.to_dict('records')

	def check(self, id_to_check):
		df = pd.read_csv(self.filename)
		# Check if any row in the DataFrame has the given ID
		if (df['ID'] == id_to_check.upper()).any():
			return True
		else:
			return False

	def insert_one(self, data):
		for key in list(data.keys()):
			data[key] = data[key].upper()
		df = pd.read_csv(self.filename)
		new_df = pd.DataFrame([data])

		df = pd.concat([df, new_df], ignore_index=True)
		df.to_csv(self.filename, index=False)
		return True

	def edit(self, data):
		df = pd.read_csv(self.filename)
		for key in list(data.keys()):
			data[key] = data[key].upper()
		for index, row in df.iterrows():
			if row['ID'] == data['ID']:
				# Update values in the row
				for key in data.keys():
					df.at[index, key] = data[key]
				break  # Exit loop after updating the row

		df.to_csv(self.filename, index=False)
		return True

	def remove(self, id_to_remove):
		df = pd.read_csv(self.filename)
		df = df[df["ID"] != id_to_remove]
		df.to_csv(self.filename, index=False)

	def get_program_ids(self):
		df = pd.read_csv(self.filename)
		rows = ["No Program"]
		for row in df.to_dict('records'):
			rows.append(row["ID"])
		return rows

# Example usage
programs = DB('programs', ["ID", "NAME"])
students = DB('students', ["ID", "NAME", "SEX", "PROGRAM", "YEAR LEVEL"])
