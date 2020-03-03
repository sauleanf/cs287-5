# Homework 05
# Filip Saulean


"""
*** DESCRIBE YOUR CODE ORGANIZATION HERE ***
"""


#################### PLEASE  DO NOT MODIFY CODE HERE #####################
import sys, os, string
import math, random
import csv, json
from collections import Counter
# Please do not use other imports in this homework
##########################################################################


# *** PLEASE DEFINE ANY OTHER FUNCTIONS HERE ***
def load_data():
    """looks for the text file at ../data/diabetes_study_rz03__data.txt and
    returns a dictionary of lists where key corresponds to a column and 
    an index corresponds to a row. (e.g. data["NP"][4] returns the 5th value for
    the column "NP" """
    filename = os.path.join(os.getcwd(), "..", "data",
        "diabetes_study_rz03__data.txt")
    
    # skeleton of the returned dictionary
    data = {'NP': [], 'BP': [], 'PG': [], 'SI': [], 'class': [],
        'age': [], 'SFT': [], 'BMI': []}
    
    # iterates over the lines of the txt file 
    with open(filename) as diabetes_data:
        for line in diabetes_data.read().split("\n")[:-1]:
            # loads each line as a dictionary
            line_data = json.loads(line)

            # adds the value to each column
            for key, value in line_data.items():
                data[key].append(value)
    return data


def correlation_coefficient(X,Y):
    """Compute and return (as a float) the Pearson correlation coefficient
    between two lists of numbers X and Y.
    """
    pass


# *** YOUR WORK HERE ***
data_dict = load_data()
verified_keys = ['NP', 'BP', 'PG', 'SI', 'class', 'age', 'SFT', 'BMI']

counts = {'NP': [], 'BP': []}

for key in ["NP"]:
    data_dict[key] = sorted(data_dict[key])
    for i in list(dict.fromkeys(data_dict[key])):
        counts[key].append(data_dict[key].count(i))

# *** PROBLEM 1.3 BELOW THIS IMPORT ONLY ***
import matplotlib.pyplot as plt
p = list(dict.fromkeys(data_dict[key]))
print(p)
plt.scatter(p, counts["NP"], label='skitscat', color='k', s=25, marker="o")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
