"""
Good
Standard
Poor
"""
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from sklearn.model_selection import train_test_split
pio.templates.default = "plotly_white"

data = pd.read_csv("../data/kredi-train.csv")
# print(data.head())
# print(data.info()) # Bilgiler
# print(data.isnull()) # True - False
# print(data.isnull().sum()) # Toplam -- Hiç boş hücre yok.

#emre = data["Credit_Score"]#.value_counts() ## Credit_Score sütunu
emre = data["Credit_Score"].value_counts() #  Credit_Score sütunu unique değerlerin toplamı

# fig = px.box(data, 
#              x="Occupation",  
#              color="Credit_Score", 
#              title="Credit Scores Based on Occupation", 
#              color_discrete_map={'Poor':'red',
#                                  'Standard':'yellow',
#                                  'Good':'green'})
# fig.show()


# fig = px.box(data, 
#              x="Credit_Score", 
#              y="Annual_Income", 
#              color="Credit_Score",
#              title="Credit Scores Based on Annual Income", 
#              color_discrete_map={'Poor':'red',
#                                  'Standard':'yellow',
#                                  'Good':'green'})
# fig.update_traces(quartilemethod="exclusive")
# fig.show()


# fig = px.box(data, 
#              x="Credit_Score", 
#              y="Monthly_Inhand_Salary", 
#              color="Credit_Score",
#              title="Credit Scores Based on Monthly Inhand Salary", 
#              color_discrete_map={'Poor':'red',
#                                  'Standard':'yellow',
#                                  'Good':'green'})
# fig.update_traces(quartilemethod="exclusive")
# fig.show()


data["Credit_Mix"] = data["Credit_Mix"].map({"Standard": 1, 
                               "Good": 2, 
                               "Bad": 0})


x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary", 
                   "Num_Bank_Accounts", "Num_Credit_Card", 
                   "Interest_Rate", "Num_of_Loan", 
                   "Delay_from_due_date", "Num_of_Delayed_Payment", 
                   "Credit_Mix", "Outstanding_Debt", 
                   "Credit_History_Age", "Monthly_Balance"]])
y = np.array(data[["Credit_Score"]])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                    test_size=0.33, 
                                                    random_state=42)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(xtrain, ytrain)
print("Credit Score Prediction : ")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))

features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
print("Predicted Credit Score = ", model.predict(features))