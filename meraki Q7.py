# Q7.Text file data ko json file data mai convert karo,jaise ki
#  neeche diya hai?
#  Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29


import json


a={
    "Name": "Abhishek",
    "Designation": "CEO of navgurukul",
    "Gender":"male",
    "Age": "29"
    }
b=open("jsonfile.json","w")
json.dump(a,b,indent=4)

