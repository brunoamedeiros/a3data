import csv
from sqlalchemy.orm import Session
from app.infra.db_models.patient_db_model import PatientsDBModel
from app.infra.db_models.user_db_model import UserDBModel
from app.infra.config import settings
from app.infra.security import security
# from app.infra.repositories.patient_repository import index_patient


def load_db(session: Session) -> None:
    if not session.query(PatientsDBModel).first():
        with open("/app/csv/patients.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                patient = PatientsDBModel(
                    id=row["Id"],
                    birthdate=row["BIRTHDATE"],
                    deathdate=row["DEATHDATE"] if row["DEATHDATE"] else None,
                    ssn=row["SSN"],
                    drivers=row["DRIVERS"] if row["DRIVERS"] else None,
                    passport=row["PASSPORT"] if row["PASSPORT"] else None,
                    prefix=row["PREFIX"] if row["PREFIX"] else None,
                    first=row["FIRST"],
                    middle=row["MIDDLE"] if "MIDDLE" in row else None,
                    last=row["LAST"],
                    suffix=row["SUFFIX"] if row["SUFFIX"] else None,
                    maiden=row["MAIDEN"] if "MAIDEN" in row else None,
                    marital=row["MARITAL"] if row["MARITAL"] else None,
                    race=row["RACE"],
                    ethnicity=row["ETHNICITY"],
                    gender=row["GENDER"],
                    birthplace=row["BIRTHPLACE"],
                    address=row["ADDRESS"],
                    city=row["CITY"],
                    state=row["STATE"],
                    county=row["COUNTY"],
                    fips=row["FIPS"] if "FIPS" in row else None,
                    zip=row["ZIP"],
                    lat=row["LAT"],
                    lon=row["LON"],
                    healthcare_expenses=row["HEALTHCARE_EXPENSES"],
                    healthcare_coverage=row["HEALTHCARE_COVERAGE"],
                    income=row["INCOME"]
                )
                session.add(patient)

                # index_patient(patient)
            session.commit()

    # Add a new superuser for testing
    user = session.query(UserDBModel).filter(
        UserDBModel.email == settings.FIRST_SUPERUSER).first()
    if not user:
        superuser = UserDBModel(
            email=settings.FIRST_SUPERUSER,
            password=security.get_password_hash(
                settings.FIRST_SUPERUSER_PASSWORD),
            is_superuser=True,
            full_name="Admin User"
        )

        session.add(superuser)
        session.commit()
