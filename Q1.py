from os import system, remove
import csv
from prettytable import PrettyTable


class ENTRY:
    def __init__(self, attributes):
        self.Fname = attributes[0]
        self.Lname = attributes[1]
        self.Roll = attributes[2]
        self.Course = attributes[3]
        self.Sem = attributes[4]
        self.ExamType = attributes[5]
        self.TotalMarks = attributes[6]
        self.ScoredMarks = attributes[7]

    def __str__(self) -> str:
        s = f"{self.Fname},{self.Lname},{self.Roll},{self.Course},{self.Sem},{self.ExamType},{self.TotalMarks},{self.ScoredMarks}"
        return s


EnteriesDYNAMIC = []


def initialize(Enteries):
    try:
        with open("entries.csv", mode="r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                E = ENTRY(row)
                Enteries.append(E)
    except:
        print("No Previous Session Found")


def save(Enteries):
    remove("entries.csv")
    try:
        with open("entries.csv", mode="w") as file:
            csvwriter = csv.writer(file)
            for entry in Enteries:
                csvwriter.writerow(str(entry).split(","))
    except:
        print("No Entries to save")


def display(Enteries):
    t = PrettyTable(
        ["FName", "Lname", "Roll", "Course", "Sem", "Exam", "Total", "Scored"]
    )
    for entry in Enteries:
        s = f"{entry}"
        pieces = list(map(str, s.split(sep=",")))
        t.add_row(pieces)
    print(t)


def add_entry() -> list:
    print("Enter details")
    attributes = []
    temp = input("Enter First name : ")
    attributes.append(temp)
    temp = input("Enter Last name : ")
    attributes.append(temp)
    temp = input("Enter Roll number : ")
    attributes.append(temp)
    temp = input("Enter Course name : ")
    attributes.append(temp)
    temp = input("Enter Sem : ")
    attributes.append(temp)
    temp = input("Enter Exam Type : ")
    attributes.append(temp)
    temp = input("Enter Total Marks : ")
    attributes.append(temp)
    temp = input("Enter Scored Marks : ")
    attributes.append(temp)
    E = ENTRY(attributes)
    return E


def rem_entry(Fname, Lname):
    t = PrettyTable(
        [
            "Entry No.",
            "FName",
            "Lname",
            "Roll",
            "Course",
            "Sem",
            "Exam",
            "Total",
            "Scored",
        ]
    )
    count = 1
    for E in EnteriesDYNAMIC:
        if E.Fname == Fname and E.Lname == Lname:
            s = f"{E}"
            pieces = list(map(str, s.split(sep=",")))
            pieces.insert(0, count)
            count = count + 1
            t.add_row(pieces)
    print(t)
    if count == 1:
        print("No Entries for the given details")
        return
    print("Which Entry No. You Want to remove?")
    which = int(input("Enter Entry No. : "))
    count2 = 1
    for E in EnteriesDYNAMIC:
        if E.Fname == Fname and E.Lname == Lname:
            if count2 == which:
                EnteriesDYNAMIC.remove(E)
                break
            count2 = count2 + 1


def updt_entry(Fname, Lname):
    t = PrettyTable(
        [
            "Entry No.",
            "FName",
            "Lname",
            "Roll",
            "Course",
            "Sem",
            "Exam",
            "Total",
            "Scored",
        ]
    )
    count = 1
    for E in EnteriesDYNAMIC:
        if E.Fname == Fname and E.Lname == Lname:
            s = f"{E}"
            pieces = list(map(str, s.split(sep=",")))
            pieces.insert(0, count)
            count = count + 1
            t.add_row(pieces)
    print(t)
    if count == 1:
        print("No Entries for the given details")
        return
    print("Which Entry No. You Want to update?")
    which = int(input("Entry Entry No. : "))
    idx = -1
    count2 = 1
    for E in EnteriesDYNAMIC:
        if E.Fname == Fname and E.Lname == Lname:
            if count2 == which:
                idx = EnteriesDYNAMIC.index(E)
                break
            count2 = count2 + 1
    EnteriesDYNAMIC[idx] = add_entry()


def search(Fname, Lname):
    t = PrettyTable(
        ["FName", "Lname", "Roll", "Course", "Sem", "Exam", "Total", "Scored"]
    )
    for E in EnteriesDYNAMIC:
        if E.Fname == Fname and E.Lname == Lname:
            s = f"{E}"
            pieces = list(map(str, s.split(sep=",")))
            t.add_row(pieces)
    print(t)


initialize(EnteriesDYNAMIC)
input("Press Enter to continue...")
while True:
    system("clear")
    print("<----- Select Option ----->")
    print("Choice 1 : Exit")
    print("Choice 2 : Display Marks Directory")
    print("Choice 3 : Add Entry")
    print("Choice 4 : Search Entry")
    print("Choice 5 : Remove Entry")
    print("Choice 6 : Update Entry")
    try:
        choice = int(input())
    except:
        continue
    if choice == 1:
        save(EnteriesDYNAMIC)
        print("Bye!")
        break
    if choice == 2:
        display(EnteriesDYNAMIC)
        input("Press Enter to continue...")
    if choice == 3:
        EnteriesDYNAMIC.append(add_entry())
        print("Entry added")
        input("Press Enter to continue...")
    if choice == 4:
        print("Enter details")
        Fname = input("Enter First name : ")
        Lname = input("Enter Last name : ")
        search(Fname, Lname)
        input("Press Enter to continue...")
    if choice == 5:
        print("Enter details")
        Fname = input("Enter First name : ")
        Lname = input("Enter Last name : ")
        try:
            rem_entry(Fname, Lname)
            print("Entry Removed")
            input("Press Enter to continue...")
        except:
            print("Could not remove Entry")
            input("Press Enter to continue...")
    if choice == 6:
        print("Enter details")
        Fname = input("Enter First name : ")
        Lname = input("Enter Last name : ")
        try:
            updt_entry(Fname, Lname)
            print("Entry Updated")
            input("Press Enter to continue...")
        except:
            print("Could not update Entry")
            input("Press Enter to continue...")
