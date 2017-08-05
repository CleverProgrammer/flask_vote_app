from run import db, Fighter

# Create all the tables
db.create_all()

# create fighters
conor = Fighter(name='Conor McGregor')
floyd = Fighter(name='Floyd Mayweather')

# add fighters to session
db.session.add(conor)
db.session.add(floyd)

# commit the fighters to database
db.session.commit()
