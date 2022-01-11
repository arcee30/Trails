import os, sys, csv
import pandas as pd
import numpy as np


# flatten a nested list into a single list
def flatten(t):
    return [item for sublist in t for item in sublist]


# load the dataset of PDS room directories into a pandas dataframe
df = pd.read_csv("Room Directory - Sheet1.csv")
# get the rooms
rooms = df.iloc[:, 1:2].values
rooms = flatten(rooms)
# get the classes
classes = df.iloc[:, -1].values
# arrays to store input and output data
inputs = []
types = []


# find the room the user is looking for
def checkRoom(room):
    # the command below will throw an exception if the input is not an integer
    int(room)
    if int(room) not in rooms:
        raise ValueError('A very specific bad thing happened.')

