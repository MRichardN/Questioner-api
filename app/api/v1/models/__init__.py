

question_list = [{
    "id": 1,
    "title": "Continuous integraion",
    "body": "How do we integrate Travis for continuous integration?",
    "createdOn": "1800hrs",
    "createdBy": 1,
    "meetup" : 1,
    "votes": 5
    },
     {
        "id": 2,
        "title": "Flask",
        "body": "How to install flask?",
        "createdOn": "1300hrs",
        "createdBy": 2,
        "meetup" : 2,
        "votes": 4
        }]



user_list = [{
    "id" : 1,  
    "firstname" : "John", 
    "lastname" : "Doe" , 
    "othername" : "Kinuthia" , 
    "email" : "johndoe@gmail.com" , 
    "phonenumber" : "0722454545", 
    "username" : "JohnDK" ,  
    "registered" : "1800hrs" , 
    "isAdmin" : False 
},
{
    "id" : 2,  
    "firstname" : "James", 
    "lastname" : "Orengo" , 
    "othername" : "Waithera" , 
    "email" : "orengoj@gmail.com" , 
    "phonenumber" : "0722554545", 
    "username" : "OrengoJW" ,  
    "registered" : "0900hrs" , 
    "isAdmin" : True 
}
]


meetup_list = [
    {
        "id": 1, 
        "createdOn" : "1800hrs" ,   
        "location" : "Andela" ,
        "topic" : "TDD" , 
        "happeningOn" : "0800hrs" ,   # // when the meetup is holding 
         
        #"images" :  // [String, String] , // OPTIONAL: URL to the image location 
        #"Tags" : [String, String, ....]

    },
     {
        "id": 2, 
        "createdOn" : "2300hrs" ,   
        "location" : "PAC" , 
        "topic" : "Postgress" , 
        "happeningOn" : "10:00Am" ,   # // when the meetup is holding 

        #"images" :  // [String, String] , // OPTIONAL: URL to the image location 
        #"Tags" : [String, String, ....]

    }
]


rsvp_list = [{
    "id" : 1,
    "meetup" : 1,
    "user" : 1,
    "response" : "This is a sample response"
}]
