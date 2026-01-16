#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():

    # Clear existing data
    Plant.query.delete()

    aloe = Plant(
        name="Aloe",
        image="./images/aloe.jpg",
        price=11.50,
    )

    zz_plant = Plant(
        name="ZZ Plant",
        image="./images/zz-plant.jpg",
        price=25.98,
    )

    snake_plant = Plant(
        name="Snake Plant",
        image="./images/snake-plant.jpg",
        price=18.75,
    )

    peace_lily = Plant(
        name="Peace Lily",
        image="./images/peace-lily.jpg",
        price=22.00,
    )

    monstera = Plant(
        name="Monstera",
        image="./images/monstera.jpg",
        price=30.00,
    )

    spider_plant = Plant(
        name="Spider Plant",
        image="./images/spider-plant.jpg",
        price=14.25,
    )

    # Add each plant individually
    db.session.add(aloe)
    db.session.add(zz_plant)
    db.session.add(snake_plant)
    db.session.add(peace_lily)
    db.session.add(monstera)
    db.session.add(spider_plant)

    db.session.commit()

 
