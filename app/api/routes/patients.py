from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.api.controllers.patient_controller import PatientController
from app.interactor.dtos.create_patient_dtos import CreatePatientInputDto
from app.interactor.dtos.update_patient_dtos import UpdatePatientInputDto
from app.interactor.dtos.delete_patient_dtos import DeletePatientOutputDto
from app.domain.entities.patient import Patient
from app.domain.entities.user import User
from elasticsearch import Elasticsearch
from app.infra.config import settings

router = APIRouter()
controller = PatientController()
es = Elasticsearch(settings.ELASTICSEARCH_URL)


@router.post("/", response_model=Patient)
async def create_patient(patient_data: CreatePatientInputDto, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ Create new patient. """
    try:
        result = controller.create_patient(patient_data.model_dump())

        if not result:
            raise HTTPException(
                status_code=400, detail="Patient already exists")
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{patient_id}", response_model=Patient)
async def get_patient(patient_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ Retrieve a patient by ID. """
    try:
        result = controller.get_patient(patient_id)
        if not result:
            raise HTTPException(status_code=404, detail="Patient not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{patient_id}", response_model=Patient)
async def update_patient(patient_id: str, patient_data: UpdatePatientInputDto, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ Update a patient by ID. """
    try:
        result = controller.update_patient(
            patient_id, patient_data.model_dump())
        if not result:
            raise HTTPException(status_code=404, detail="Patient not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{patient_id}", response_model=DeletePatientOutputDto)
async def delete_patient(patient_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """ Delete a patient by ID. """
    try:
        result = controller.delete_patient(patient_id)
        if not result.success:
            raise HTTPException(status_code=404, detail=result.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.get("/search/")
# async def search_patients(query: str):
#     response = es.search(index="patients", body={
#         "query": {
#             "multi_match": {
#                 "query": query,
#                 "fields": ["name", "id"]
#             }
#         }
#     })

#     return {"results": response["hits"]["hits"]}
