import pandas as pd
students = [["Alice",20,"A",85],["Bob",22,"B",78],["Charlie",19,"A",92],["David",21,"C",65],["Eva",20,"B",74]]
frame = pd.DataFrame(students, columns=["Name","Age","Grade","Marks"])
students_data = frame
print("All Students Data :","\n",students_data)
#Display the first 3 rows of the DataFrame
print("Head 3 :","\n",students_data.head(3))
#Select and display only the "Name" and "Marks" columns.
print("Name & Marks Only :","\n",students_data[["Name","Marks"]])
#Accesses rows where 'Grade' is 'A'
print("Students who have A as Grades :","\n",students_data[students_data["Grade"]=="A"])

#Here i used data from Grades csv Sheet
students_data1 = pd.read_csv("Grades.csv")
print("Data from Grades csv Sheet :","\n",students_data1)