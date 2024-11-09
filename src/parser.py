import json

class Parser:
    text: str
    headers = {}
    method_name: str
    endpoint: str
    version: str
    content_types: list
    body = {}
    
    def __init__(self):
        pass
        
    def parseRequest(self, text):
        try:
            self.text = text
            string_list = text.split("\n")
            self.method_name = string_list[0].split(" ")[0]
            self.endpoint = string_list[0].split(" ")[1]
            self.version = string_list[0].split(" ")[2].split("/")[1]
            self.body = json.loads(string_list[len(string_list) - 1])
            self.transformHeaders(string_list[1:len(string_list)-2])
        except:
            raise Exception("Incorrect header Format")
        # print(string_list)
        
    def printProperties(self):
        # print(self.text)
        print(self.method_name)
        print(self.endpoint)
        print(self.version)
        print("\n")
        print(self.body)
        print("\n")
        print(self.headers)
    
    def transformHeaders(self, lst : list):
        for header in lst:
            key = header.split(":")[0].strip(" ")
            value = header.split(":")[1].strip(" ")
            self.headers[key] = value

    
string = '''GET /endpoint YAGAMI/1.1
Content-Type: json
Content-Length: 648
Content-Encoding: gzip
Expires: Fri, 13 March 2024

{"Ujjwal" : "Singh"}'''    
    
parser = Parser()

parser.parseRequest(string)
parser.printProperties()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
