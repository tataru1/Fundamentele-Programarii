from repository.DataRepo import DataRepo

class GekochterGerichtRepo(DataRepo):
    def __init__(self, filename):
        super().__init__(filename)

    def convert_to_string(self, list):
        return map(lambda x: str(x), list)

    def convert_from_string(self, string):
        objectList = []
        return map(lambda x: objectList.append(x), string)



