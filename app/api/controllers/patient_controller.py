""" Patient Controller Module
"""
from typing import Dict
from app.interactor.dtos.create_patient_dtos \
    import CreatePatientInputDto
from app.interactor.use_cases.create_patient \
    import CreatePatientUseCase
from app.interactor.use_cases.get_patient \
    import GetPatientUseCase
from app.interactor.dtos.update_patient_dtos \
    import UpdatePatientInputDto
from app.interactor.use_cases.update_patient \
    import UpdatePatientUseCase
from app.interactor.use_cases.delete_patient \
    import DeletePatientUseCase
from app.infra.repositories.patient_repository \
    import PatientRepository
from app.api.presenters.create_patient_presenter \
    import CreatePatientPresenter
from app.api.presenters.get_patient_presenter \
    import GetPatientPresenter
from app.api.presenters.update_patient_presenter \
    import UpdatePatientPresenter
from app.api.presenters.delete_patient_presenter \
    import DeletePatientPresenter
from app.interactor.dtos.delete_patient_dtos \
    import DeletePatientOutputDto


class PatientController:
    """ Patient Controller Class
    """

    def __init__(self):
        self.repository = PatientRepository()

    def create_patient(self, request_data) -> Dict:
        presenter = CreatePatientPresenter()
        use_case = CreatePatientUseCase(presenter, self.repository)
        input_dto = CreatePatientInputDto(**request_data)
        return use_case.execute(input_dto)

    def get_patient(self, patient_id: str) -> Dict:
        presenter = GetPatientPresenter()
        use_case = GetPatientUseCase(presenter, self.repository)
        return use_case.execute(patient_id)

    def update_patient(self, patient_id: str, request_data) -> Dict:
        presenter = UpdatePatientPresenter()
        use_case = UpdatePatientUseCase(presenter, self.repository)
        input_dto = UpdatePatientInputDto(**request_data)
        return use_case.execute(patient_id, input_dto)

    def delete_patient(self, patient_id: str) -> DeletePatientOutputDto:
        presenter = DeletePatientPresenter()
        use_case = DeletePatientUseCase(presenter, self.repository)
        return use_case.execute(patient_id)
