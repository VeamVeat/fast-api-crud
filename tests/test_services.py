from pydantic import BaseModel

from tests.utils.test_settings_database import SessionTesting


class TestBaseService:
    def __init__(
            self,
            db_session: SessionTesting,
            item_schema: BaseModel,
            db_model
    ):
        self.db_session = db_session
        self.item_schema = item_schema
        self.db_model = db_model

    def create_item(self):
        db_item = self.db_model(**self.item_schema.dict())
        self.db_session.add(db_item)
        self.db_session.commit()
        self.db_session.refresh(db_item)
        return db_item
