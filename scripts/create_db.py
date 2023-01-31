from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from app.config import DATABASE_URL


def main():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine.connect())

    session.execute(
        text("""CREATE TABLE IF NOT EXISTS users (
    id integer not null primary key,
    email varchar(256),
    password varchar(256),
    first_name varchar(256),
    last_name varchar(256),
    username varchar(256),
    created_at varchar(256)
    );"""
             )
    )

    session.execute(
        text("""CREATE TABLE IF NOT EXISTS auth_token (
    id integer not null primary key,
    token varchar(256),
    user_id integer references user,
    created_at varchar(256)
    );"""
             )
    )

    session.execute(
        text("""CREATE TABLE IF NOT EXISTS stream (
    id integer not null primary key,
    user_id integer references user,
    title varchar(256),
    topic varchar(256),
    status varchar(256),
    created_at varchar(256)
    );"""
             )
    )

    session.close()


if __name__ == "__main__":
    main()
