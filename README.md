# Linear Regression

## Introduction

Linear Regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. It assumes a linear relationship between the variables, aiming to find the best-fitting straight line that predicts the dependent variable based on the independent variables. Linear Regression is widely used for predictive analysis and understanding the relationship between variables in various fields, including economics, finance, and social sciences.

The following project uses Linear Regression for predicting amount of tip given by customer at a dining. A detailed description about the dataset will be described later.

## Requirements

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Dataset Description

The dataset contains information about restaurant bills, including the total bill, tip amount, gender of the person giving the tip, smoker status, day of the week, time of day, and size of the dining party. Each feature is described as follows:

```bash
total_bill:            Total bill of the customers.
tip:                   Amount of tip given.
sex:                   Gender of the person giving the tip.
smoker:                Smoker status (yes/no).
day:                   Day of the week when the transaction occurred (Thursday to Sunday).
time:                  Time of day when the transaction occurred (lunch or dinner).
size:                  Number of people for dining.
```
Statistics of the dataset are also shown during program execution, as well as null values inside the data columns.

## Training and Testing

Run the model.py file after installing the given requirements.

Dataset information composing of null value counts, feature descriptions, and statistics are shown during program execution. The data was first preprocessed, transforming all categorical values into numerical values before going into training. After cleaning and training, statistical graphs are presented, and the loss during training is also shown. Lastly testing phase prompts runs shortly for runtime prediction of amount of tips. 

The model trained over above dataset acheived an average of 0.69 loss. L2 Loss was used.

## Graphical Results

![Average Tips Given by Smokers and Non-Smokers](Graphs/Average%20Tips%20Given%20by%20Smokers%20and%20Non-Smokers.png)
![Distribution of Tips by Day of the Week](Graphs/Distribution%20of%20Tips%20by%20Day%20of%20the%20Week.png)
![Distribution of Tips by Gender of the Person Paying the Bill](Graphs/Distribution%20of%20Tips%20by%20Gender%20of%20the%20Person%20Paying%20the%20Bill.png)
![Distribution of Tips by Meal Time (Lunch vs. Dinner)](Graphs/Distribution%20of%20Tips%20by%20Meal%20Time%20(Lunch%20vs.%20Dinner).png)
![Total Bill Paid vs. Tip with Different Colors and Sizes for Gender and Table Size](Graphs/Total%20Bill%20Paid%20vs.%20Tip%20with%20Different%20Colors%20and%20Sizes%20for%20Gender%20and%20Table%20Size.png)
![Total Bill Paid vs. Tip with Different Colors and Sizes for Meal Time and Table Size](Graphs/Total%20Bill%20Paid%20vs.%20Tip%20with%20Different%20Colors%20and%20Sizes%20for%20Meal%20Time%20and%20Table%20Size.png)




