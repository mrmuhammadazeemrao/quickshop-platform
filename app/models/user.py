from sqlalchemy import Column, Integer, String, Index, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base
from passlib.context import CryptContext

# Initialize the password hashing context
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    profile_image = Column(String, nullable=True)

    orders = relationship("Order", back_populates="user")
    cart = relationship("Cart", back_populates="user")

    # Index on the email for faster lookups
    Index("idx_user_email", email)

    # Ensure that the email is unique using a UniqueConstraint
    UniqueConstraint(email, name="uq_user_email")

    def verify_password(self, plain_password):
        return password_context.verify(plain_password, self.password_hash)

    def set_password(self, raw_password):
        self.password_hash = password_context.hash(raw_password)
