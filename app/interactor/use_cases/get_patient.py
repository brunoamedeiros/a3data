from typing import Dict
from app.interactor.dtos.get_patient_dtos \
    import GetPatientOutputDto
from app.interactor.interfaces.presenters.get_patient_presenter \
    import GetPatientPresenterInterface
from app.interactor.interfaces.repositories.patient_repository \
    import PatientRepositoryInterface


class GetPatientUseCase:
    def __init__(self, presenter: GetPatientPresenterInterface, repository: PatientRepositoryInterface):
        self.presenter = presenter
        self.repository = repository

    def execute(self, patient_id: str) -> Dict:
        patient = self.repository.get_by_id(patient_id)
        output_dto = GetPatientOutputDto(patient=patient)
        return self.presenter.present(output_dto)
