from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.observation import Observation
from fhir.resources.quantity import Quantity
from fhir.resources.reference import Reference

class Observation(Observation):
    def __init__(self, id, patientid, code_system, code_code, code_display, value, unit, text=None, effectiveDateTime=None):
        super().__init__(
            id=id,
            status="final",
            category=[CodeableConcept.construct(
                coding=[
                    Coding.construct(
                        system="http://terminology.hl7.org/CodeSystem/observation-category",
                        code="exam",
                        display="Exam"
                    )
                ]
            )],
            code=CodeableConcept.construct(
                coding=[
                    Coding.construct(
                        system=code_system,
                        code=code_code,
                        display=code_display
                    )
                ],
                text=text
            ),
            subject = Reference.construct(reference="Patient/"+patientid),
            effectiveDateTime = effectiveDateTime,
            valueQuantity = Quantity.construct(
                value = value,
                unit = unit,
            ),
        )
