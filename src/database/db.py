from sqlalchemy import create_engine

engine = create_engine("sqlite:///./arch-project.db", echo=True)

print("Database engine created successfully!")
