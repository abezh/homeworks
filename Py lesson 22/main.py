import json
from faker import Faker


class Fake:
    def __init__(self):
        self.fake = Faker()

    def generate_data(self, num):
        active_data = []
        inactive_data = []

        for i in range(num):
            name = self.fake.name()
            email = self.fake.email()
            address = self.fake.address()
            active = self.fake.boolean()
            data = {
                "name": name,
                "email": email,
                "address": address,
                "active": active
            }
            if active:
                active_data.append(data)
            else:
                inactive_data.append(data)

        return {"active_students": active_data, "inactive_students": inactive_data}

    def to_json(self, data, file):
        with open(file, "w") as json_file:
            json.dump(data, json_file, indent=4)


fake_instance = Fake()
fake_info = fake_instance.generate_data(5)
fake_instance.to_json(fake_info, 'fake_info.json')
