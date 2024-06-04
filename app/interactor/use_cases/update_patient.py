from typing import Dict
from app.interactor.dtos.update_patient_dtos \
    import UpdatePatientInputDto, UpdatePatientOutputDto
from app.interactor.interfaces.presenters.update_patient_presenter \
    import UpdatePatientPresenterInterface
from app.interactor.interfaces.repositories.patient_repository \
    import PatientRepositoryInterface


class UpdatePatientUseCase:
    def __init__(self, presenter: UpdatePatientPresenterInterface, repository: PatientRepositoryInterface):
        self.presenter = presenter
        self.repository = repository

    def execute(self, patient_id: str, input_dto: UpdatePatientInputDto) -> Dict:
        patient = self.repository.update(patient_id, input_dto)
        output_dto = UpdatePatientOutputDto(patient=patient)
        return self.presenter.present(output_dto)
