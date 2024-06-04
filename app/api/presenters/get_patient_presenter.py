from typing import Dict
from app.interactor.dtos.get_patient_dtos import GetPatientOutputDto
from app.interactor.interfaces.presenters.get_patient_presenter import GetPatientPresenterInterface


class GetPatientPresenter(GetPatientPresenterInterface):
    def present(self, output_dto: GetPatientOutputDto) -> Dict:
        return output_dto.patient
