'''
Right now, if there is only one field that grows a specific crop,
then that field is classified as inefficient
NEED to think more on that later!!!
'''
import os
import sys

sys.path.append('../models')
sys.path.append('../algorithm')
from fields import *
from field_cluster import *

# hard code testing data
allFields = []
f1 = Field("Almonds", 0.25, {"coordinates":[
        {
          "lat": 34.8927691487864, 
          "lng": -120.29890875936135
        }, 
        {
          "lat": 34.89275201732019, 
          "lng": -120.29910292321898
        }, 
        {
          "lat": 34.893193168599346, 
          "lng": -120.29922284822712
        }, 
        {
          "lat": 34.89323885463827, 
          "lng": -120.29900298664428
        }, 
        {
          "lat": 34.892831966808316, 
          "lng": -120.29890304864779
        }, 
        {
          "lat": 34.8927691487864, 
          "lng": -120.29890875936135
        }
      ]}, 1)
f2 = Field("Almonds", 0.3, {"coordinates":[
        {
          "lat": 35.8927691487864, 
          "lng": -119.29890875936135
        }, 
        {
          "lat": 35.89275201732019, 
          "lng": -119.29910292321898
        }, 
        {
          "lat": 35.893193168599346, 
          "lng": -119.29922284822712
        }, 
        {
          "lat": 35.89323885463827, 
          "lng": -119.29900298664428
        }, 
        {
          "lat": 35.892831966808316, 
          "lng": -119.29890304864779
        }, 
        {
          "lat": 35.8927691487864, 
          "lng": -119.29890875936135
        }
      ]}, 2)
f3 = Field("Almonds", 0.2, {"coordinates":[
        {
          "lat": 3.8927691487864, 
          "lng": -11.29890875936135
        }, 
        {
          "lat": 3.89275201732019, 
          "lng": -11.29910292321898
        }, 
        {
          "lat": 3.893193168599346, 
          "lng": -11.29922284822712
        }, 
        {
          "lat": 3.89323885463827, 
          "lng": -11.29900298664428
        }, 
        {
          "lat": 3.892831966808316, 
          "lng": -11.29890304864779
        }, 
        {
          "lat": 3.8927691487864, 
          "lng": -11.29890875936135
        }
      ]}, 3)
f1.set_mean()
f2.set_mean()
f3.set_mean()
allFields.append(f1)
allFields.append(f2)
allFields.append(f3)

alg(allFields)

for f in allFields:
    print(f.serialize())