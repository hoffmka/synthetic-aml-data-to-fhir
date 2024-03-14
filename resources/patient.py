from fhir.resources.patient import Patient

class Patient(Patient):
    def __init__(self, id, gender=None):
        super().__init__(
            id=id,
        )
        self.gender = gender