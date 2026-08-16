from app.database.db_connection import engine, Base
from app.database.vendor_entity import VendorEntity
from app.models.compliance_check_entity import ComplianceCheckEntity

def create_tables():

    Base.metadata.create_all(bind=engine)

    print("Database tables created successfully.")


if __name__ == "__main__":
    create_tables()