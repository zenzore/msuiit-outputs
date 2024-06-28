import os
import time

ENTER_PASSCODE = "\n\n\n\n\n\n\n\n\n\n  _____       _              ____                             _         \n | ____|_ __ | |_ ___ _ __  |  _ \x5c __ _ ___ ___  ___ ___   __| | ___ _  \n |  _| | '_ \x5c| __/ _ \x5c '__| | |_) / _` / __/ __|/ __/ _ \x5c / _` |/ _ (_) \n | |___| | | | ||  __/ |    |  __/ (_| \x5c__ \x5c__ \x5c (_| (_) | (_| |  __/_  \n |_____|_| |_|\x5c__\x5c___|_|    |_|   \x5c__,_|___/___/\x5c___\x5c___/ \x5c__,_|\x5c___(_) \n\n\n"

with open(f"./INSPIRATION.txt", "r") as f:
	INSPIRATION = f.read()

with open(f"./SAVING1.txt", "r") as f:
	SAVING_1 = f.read()

with open(f"./SAVING2.txt", "r") as f:
	SAVING_2 = f.read()

with open(f"./SAVING3.txt", "r") as f:
	SAVING_3 = f.read()

with open(f"./CONGRATS.txt", "r") as f:
	HEHE = f.read()

code = None
insp = None
saving = [SAVING_1, SAVING_2, SAVING_3]

os.system("cls")
code = input(f"{ENTER_PASSCODE}\n\n\nEnter Code: ")

while code.lower() != "2913":
	os.system("cls")
	code = input(f"{ENTER_PASSCODE}\n\n\nWRONG!!! TYPE AGAIN:")

os.system("cls")
insp = input(f"\n\n\n\n{INSPIRATION}\n\n\n\nEnter Answer: ")

while insp.lower() != "jhiah":
	os.system("cls")
	insp = input(f"\n\n\n\n{INSPIRATION}\n\n\n\nWRONG!!! TYPE AGAIN:")

j = 0
for i in range(10):
	if j >= 3:
		j = 0
	os.system("cls")
	print(f"\n\n\n\n{saving[j]}")
	j += 1
	time.sleep(1)

os.system("cls")
input(f"\n\n\n\n\n\n{HEHE}\n\n\n\n\n")

