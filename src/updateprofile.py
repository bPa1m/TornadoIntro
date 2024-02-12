import tornado.web
import json
import base64
from Profile import read_dictionary_from_file
from Profile import write_dictionary_to_file

class Handler(tornado.web.RequestHandler):
    def post(self):
        J=json.loads(self.request.body)
        username = J["username"]
        firstName = J["firstName"]
        lastName = J["lastName"]
        dob = J["birthDate"]
        ppic = base64.b64decode(J["pic"])
        tester = False

        db = read_dictionary_from_file("src\database.txt")
        if username in db:
            db[username]['realname'] = firstName + " " +  lastName
            db[username]['dateOfBirth'] = dob
            tester = True
            fh = open("html\Alice_image.png", "wb")
            fh.write(ppic)
            fh.close()
            write_dictionary_to_file(db, "src\database.txt")

        print("WE GOT:",username,firstName,lastName,dob,ppic[:20])
        resp={"Valid Input": tester}
        self.write( json.dumps(resp) )
        