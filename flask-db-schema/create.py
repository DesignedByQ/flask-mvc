from app import db, Users, Cars

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry

db.session.add(testuser)
db.session.commit()

car1 = Cars(number_plate="ijjhj", owner=testuser.id)
car2 = Cars(number_plate="sjllkn", owner=testuser.id)

db.session.add(car1)
db.session.add(car2)
db.session.commit()

print(testuser.cars)

print(car1.userbr.first_name, car2.userbr.last_name)