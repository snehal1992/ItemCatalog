from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///itemcatalogwithusers.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

User2 = User(name="Rafael Nadal", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User2)
session.commit()

#Category 1
category1 = Category(name = "Skateboard")
session.add(category1)
session.commit()

#Item 1 
item1 = Item(user_id=1, name="Rimable Bamboo Drop", 
	description="Rimable Bamboo longboard Use upgraded"+ 
	"bamboo/maple hybrid deck with a little more concave"+
	".More durable and elastic!",
	category=category1)
session.add(item1)
session.commit()

#Category2
category2 = Category(name = "Baseball")
session.add(category2)
session.commit()

#Item2
item2 = Item(user_id=1, name="Rukket 6pc Baseball", 
	description="Rukket Sports Baseball"+ 
	" Hitting Net and Softball Hitting Net"+ 
	" PRO BUNDLE Includes the Original Sock It!",
    category=category2)

session.add(item2)
session.commit()

#Category3
category3 = Category(name = "Tennis")
session.add(category3)
session.commit()

#Item3
item3 = Item(user_id=2, name="12-Pack KEVENZ Green Advanced"+ 
	" Training Tennis Balls", 
	description="Natural rubber for consistent feel"+ 
	" and reduced shock",
    category=category3)
session.add(item3)
session.commit()

#Category4
category4 = Category(name = "Soccer")
session.add(category4)
session.commit()

#Item4
item4 = Item(user_id=2, name="adidas MLS Glider Soccer Ball", 
	description="Machine stitched construction and"+ 
	" internal nylon wound carcass for maximum durability"+
	" and long-lasting performance",
    category=category4)
session.add(item4)
session.commit()

#Category5
category5 = Category(name = "Badminton")
session.add(category5)
session.commit()

#Item5
item5 = Item(user_id=1, name="Senston - 2 Player Badminton" 
	" Racket Set Carbon Shaft Racket Set- Including"+ 
	" 1 Badminton Bag", 
	description="Incude 2 rackets ,1 racket cover ."+
	" (Badminton racket has the Stringing about 20lbs)",
    category=category5)
session.add(item5)
session.commit()

#Category6
category6 = Category(name = "Volleyball")
session.add(category6)
session.commit()

#Item6
item6 = Item(user_id=2, name="Puredrop Volleyball Training Equipment Aid", 
	description="With the aid it becomes very easy to practice" 
	" arm swing technique and tosses multiple times in a row." 
	" The elastic cord guides the ball back after every swing.",
    category=category6)
session.add(item6)
session.commit()


