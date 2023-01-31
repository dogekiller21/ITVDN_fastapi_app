from setuptools import setup

setup(
    name="app-example",
    version="0.0.1",
    author="dogekiller21",
    author_email="dogekiller21@gmail.com",
    description="ITVDN FastApi-app",
    install_requires=[
        "fastapi==0.89.1",
        "uvicorn==0.20.0",
        "SQLAlchemy==2.0.0",
        "pytest==7.2.1",

    ],
    scripts=["app/main.py", "scripts/create_db.py"]
)