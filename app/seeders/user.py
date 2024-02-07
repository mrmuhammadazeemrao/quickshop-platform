from sqlalchemy.orm import Session
from faker import Faker
from app.models.user import User
from app.core.database import Base, get_db, engine
from passlib.hash import bcrypt

fake = Faker()
password_context = bcrypt


def create_dummy_users(db: Session, num_users: int = 10):
    for _ in range(num_users):
        user = User(
            name=fake.name(),
            email=fake.email(),
            password_hash=password_context.hash(fake.password()),
            profile_image=fake.image_url(),
        )
        db.add(user)
    db.commit()


if __name__ == "__main__":
    # Create tables
    Base.metadata.create_all(bind=engine)

    # Create a session using the get_db function
    with next(get_db()) as db:
        create_dummy_users(db, num_users=50)
