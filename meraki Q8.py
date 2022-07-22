# Q8.Tumhare pass four employes ki details hai list mai:-
# ["neelam","programer","24","2400",]
# ["komal","trainer","24","20000"]
# ["anuradha","HR","25","40000"]
# ["Abhishek","manager","29","63000"]





import json


a={ 
     "emp1":{ "name":"nilam",
       "Designation":"programmer",
       "Age":"34",
       "salary":"24000",},

      "emp2":{ "name":"komal", 
        "Designation":"Trainer",
        "Age":"24",
        "salary":"20000" ,},
      "emp3":
       { "name":"anuradha",
         "Designation":"HR",
         "Age":"25",
         "salary":"40000",
         }}

file=open("employee_file.json","w")
json.dump(a,file,indent=4)