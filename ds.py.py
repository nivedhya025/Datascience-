import pandas as ni
import matplotlib.pyplot as test
nd = ni.read_csv('gender_submission.csv')
print(nd)
Total_Pass = nd["Survived"].value_counts()
total = len(nd)
a = Total_Pass[0]
perc = (a / total) * 100
print(f"Percentage of non-survivors is: {perc:.2f}%")
Total_Pass.plot(kind = 'bar',color = ["violet","blue"])
test.xlabel("Survived people")
test.ylabel("Non-Survived people")
test.title("Survived passenger in the flight")
test.xticks(rotation = 0)
test.yticks(rotation = 24)
test.show()