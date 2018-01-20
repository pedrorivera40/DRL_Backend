from flask import jsonify

from dao.person_dao import PersonDao

class PersonHandler:

    def getAllAccounts(self):
        dao = PersonDao()
        data = dao.get_persons()
        data = self.build_person_dictionaries(data)
        if len(data) == 0: return jsonify(ERROR = "Persons not found."), 404
        return jsonify(Person = data)


    def build_person_dictionaries(self, data):
        if len(data) == 0 or data[0] == None :
            return []
        result = []
        for element in data:
            t = {
                'PID' : int(element[0]),
                'PName' : element[1],
                'PLastName' : element[2],
                'PAge' : element[3],
            }
            result.append(t)
        return result