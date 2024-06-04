from app.interactor.dtos.delete_patient_dtos \
    import DeletePatientOutputDto
from app.interactor.interfaces.presenters.delete_patient_presenter \
    import DeletePatientPresenterInterface
from app.interactor.interfaces.repositories.patient_repository \
    import PatientRepositoryInterface


class DeletePatientUseCase:
    def __init__(self, presenter: DeletePatientPresenterInterface, repository: PatientRepositoryInterface):
        self.presenter = presenter
        self.repository = repository

    def execute(self, patient_id: str) -> DeletePatientOutputDto:
        result = self.repository.delete(patient_id)
        return self.presenter.present(result)
