import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

############################################################## Dataset Description and Stats 

df = pd.read_csv("tips.csv")

print("Null values in the dataset:")
print(df.isnull().sum())
print("\nColumn information:")
print(df.info())
print("\nDescriptive statistics:")
print(df.describe())

############################################################## Plots 

def scatter_plot(data, color_column, palette, title, filename=None):
    if filename is None:
        filename = title + ".png"
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(x='total_bill', y='tip', hue=color_column, size='size', sizes=(20, 200), data=data, palette=palette)
    plt.title(title)
    plt.xlabel('Total Bill Paid')
    plt.ylabel('Tip')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    if not os.path.exists("Graphs"):
        os.makedirs("Graphs")
    plt.savefig(os.path.join("Graphs", filename))
    plt.show()

def pie(column, title, filename=None):
    if filename is None:
        filename = title + ".png"
    tips_by_column_data = df.groupby(column)['tip'].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(tips_by_column_data, labels=tips_by_column_data.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
    plt.gca().add_artist(plt.Circle((0, 0), 0.5, color='white'))
    plt.title(title)
    if not os.path.exists("Graphs"):
        os.makedirs("Graphs")
    plt.savefig(os.path.join("Graphs", filename))
    plt.show()

df_subset = df[df['day'].isin(['Thur', 'Fri', 'Sat', 'Sun'])]
scatter_plot(df_subset, 'day', 'Set1', 'Total Bill Paid vs. Tip with Different Colors and Sizes for Gender and Table Size')
scatter_plot(df, 'sex', 'Set2', 'Total Bill Paid vs. Tip with Different Colors and Sizes for Gender and Table Size')
scatter_plot(df, 'time', 'Set2', 'Total Bill Paid vs. Tip with Different Colors and Sizes for Meal Time and Table Size')
pie('day', 'Distribution of Tips by Day of the Week')
pie('sex', 'Distribution of Tips by Gender of the Person Paying the Bill')
pie('smoker', 'Average Tips Given by Smokers and Non-Smokers')
pie('time', 'Distribution of Tips by Meal Time (Lunch vs. Dinner)')


############################################################## Data Preprocessing

print("\nTransforming all categorical values into numerical values\n")
print(df.head())
print()
label_encoder = LabelEncoder()

df['sex'] = label_encoder.fit_transform(df['sex'])
df['smoker'] = label_encoder.fit_transform(df['smoker'])
df['day'] = label_encoder.fit_transform(df['day'])
df['time'] = label_encoder.fit_transform(df['time'])

print(df.head())
print()

############################################################## Model and Prediction

X = df[['total_bill', 'sex', 'smoker', 'day', 'time', 'size']]
y = df['tip']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
sample_input = [[24.50, 1, 0, 0, 1, 4]]
output = model.predict(sample_input)
print("Model Prediction for Sample Input:", output)
