from app.models.user_institution import UserInstitution
from app.config import db


class UserInstitutionRepository:
    def __init__(self):
        self.db = db

    def get_user_institution(self, user_id: int):
        return self.db.query(UserInstitution).filter_by(user_id=user_id).first()

    def create_user_institution(self, user_institution: UserInstitution):
        self.db.add(user_institution)
        self.db.commit()
        self.db.refresh(user_institution)
        return user_institution

    def update_user_institution(self, user_institution: UserInstitution):
        self.db.merge(user_institution)
        self.db.commit()
        return user_institution