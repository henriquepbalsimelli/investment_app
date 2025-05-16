from fastapi import HTTPException
from app.config import db
from app.models.institution import Institution


class InstitutionRepository:
    def __init__(self):
        self.db = db

    def create_institution(self, institution_data):
        """
        Create a new institution in the database.
        """
        try:
            new_institution = Institution(**institution_data)
            self.db.add(new_institution)
            self.db.commit()
            self.db.refresh(new_institution)
            return new_institution
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))