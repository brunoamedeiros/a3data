""" This module is responsible for creating a new Patient
"""


from typing import Dict
from app.interactor.dtos.create_patient_dtos \
    import CreatePatientInputDto, CreatePatientOutputDto
from app.interactor.interfaces.presenters.create_patient_presenter \
    import CreatePatientPresenterInterface
from app.interactor.interfaces.repositories.patient_repository \
    import PatientRepositoryInterface


class CreatePatientUseCase():
    """ This class is responsible for creating a new Patient
    """

    def __init__(self, presenter: CreatePatientPresenterInterface, repository: PatientRepositoryInterface):
        self.presenter = presenter
        self.repository = repository

    def execute(self, input_dto: CreatePatientInputDto) -> Dict:
        """ This method is responsible for creating a new patient

        Args:
            input_dto (CreatePatientInputDto): The input data transfer object

        Returns:
            Dict 
        """
        patient = self.repository.create(input_dto)
        output_dto = CreatePatientOutputDto(patient=patient)
        return self.presenter.present(output_dto)
