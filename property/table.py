import django_tables2 as tables
class Mytable(tables.Table):
    area = tables.Column()
    bedrooms = tables.Column()
    bathrooms = tables.Column()
    stories = tables.Column()
    mainroad = tables.Column()
    guestroom = tables.Column()
    basement = tables.Column()
    hotwaterheating = tables.Column()
    airconditioning = tables.Column()
    parking = tables.Column()
    prefarea = tables.Column()
    furnishingstatus = tables.Column()
    predictedprice = tables.Column()
    
    