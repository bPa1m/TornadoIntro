import tornado.web
import json

def read_dictionary_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            dictionary = json.loads(content)
            return dictionary
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return {}

def write_dictionary_to_file(dictionary, file_name):
    with open(file_name, 'w') as file:
        json.dump(dictionary, file)

file_name = "src\database.txt"

class Handler(tornado.web.RequestHandler):
    def get(self):
        db = read_dictionary_from_file(file_name)
        p = self.request.path       #ex: /profile/alice
        uname = p.split("/")[2]
        realname = db[uname]["realname"]
        dob = db[uname]["dateOfBirth"]
        email = db[uname]["email"]
        img = db[uname]["img"]
        self.render("ProfileTemplate.html", uname = uname, rname = realname, dob = dob, email = email, img = img)