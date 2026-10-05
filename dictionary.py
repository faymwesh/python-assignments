student = {
    1:{
    "name" : "Faith",
    "phone" : "0712345678",
    "age" : 20,
    "location": "Syokimau",
    "dob":"2001-05-10"
    },
    2:{
    "name" : "leon",
    "phone": "0716208656",
    "age" : 21,
    "location" : "syokimau",
    "dob" :"2001-04-12"
    },
    3:{
        "name" : "john",
        "phone" : "0712456789",
        "age" : 22,
        "location" :"syokimau",
        "dob" : "2002-05-06",
       
    },
 4 : { 
     " name" : "rose",
       "phone" : "0723678808",
        "age" : 23,
        "location" : "syokimau",
        "dob" :"2003-05-12",
    },
5: { 
    "name" :"jane",
    "phone": "07223456787",
    "ages" : 24,
    "location" : "syokimau",
    "dob" : "2004-06-05",
    
    
    }



 }


# add
student [6] = {
    "name" : "peace",
    "phone" :"0743226788",
    "age" :24,
    "location":"syokimau",
    "dob" : "2002-06-04",
}

#edit
student[1]["phone"] = "0712989800"

#delete
del student[2]

print(student)

