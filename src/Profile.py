import tornado.web

accountDatabase =  {
    "alice" : {
        "realname" : "Alice Smith",
        "dateOfBirth" : "Jan 1",
        "email" : "alice@example.com",
        "img" : "/static/Alice_image.png"
    },
    
    "bob" : {
        "realname" : "Bob Jones",
        "dateOfBirth" : "Dec 31",
        "email" : "bob@bob.xyz",
        "img" : "/static/Bob_image.png"
    },

    "carol" : {
        "realname" : "Carol Ling",
        "dateOfBirth" : "July 17",
        "email" : "carol@example.com",
        "img" : "/static/Carol_image.png"
    },

    "dave" : {
        "realname" : "Dave N. Port",
        "dateOfBirth" : "Mar 14",
        "email" : "dave@dave.dave",
        "img" : "/static/Dave_image.png"
    }
}

class Handler(tornado.web.RequestHandler):
    def get(self):
        p = self.request.path       #ex: /profile/alice
        uname = p.split("/")[2]
        realname = accountDatabase[uname]["realname"]
        dob = accountDatabase[uname]["dateOfBirth"]
        email = accountDatabase[uname]["email"]
        img = accountDatabase[uname]["img"]

        self.render( "ProfileTemplate.html", uname = uname, rname = realname, dob = dob, email = email, img = img)