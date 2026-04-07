from app.data.db import Base, engine, SessionLocal
from app.data.models import CampusInfo
from app.data.campus_data import CAMPUS_INFO_SEED


def seed_data():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        db.query(CampusInfo).delete()
        db.commit()

        rows = [CampusInfo(**item) for item in CAMPUS_INFO_SEED]

        db.add_all(rows)
        db.commit()

        print(f"Database seeded successfully with {len(rows)} records.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_data()