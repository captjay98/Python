#!/usr/bin/python3

from sqlite3 import connect
from sqlalchemy import create_engine
from sqlalchemy import MetaData, insert, select,  Table, ForeignKey, CheckConstraint, Numeric
from sqlalchemy import Integer, asc, desc,  String, Column, SmallInteger, Text, DateTime, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime


engine = create_engine("mysql://captjay98:81651515@localhost/market")


Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    orders = relationship("Order", backref='customer')


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price =  Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2),  nullable=False)
#     orders = relationship("Order", backref='customer')
    

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    line_items = relationship("OrderLine", secondary="order_lines", backref='order')
    

class OrderLine(Base):
    __tablename__ = 'order_lines'
    id =  Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.id'))
    item_id = Column(Integer(), ForeignKey('items.id'))
    quantity = Column(SmallInteger())
    item = relationship("Item")


Base.metadata.create_all(engine)






"""
engine = create_engine("mysql://captjay98:81651515@localhost/market")
engine.connect()

metadata = MetaData()

customers = Table('customers', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('first_name', String(100), nullable=False),
                  Column('last_name', String(100), nullable=False),
                  Column('username', String(50), nullable=False),
                  Column('email', String(100), nullable=False),
                  Column('address', String(200), nullable=False),
                  Column('town', String(50), nullable=False),
                  Column('created_on', DateTime(), default=datetime.now),
                  Column('updated_on', DateTime(),
                         default=datetime.now, onupdate=datetime.now)
                  )


items = Table('items', metadata,
              Column('id', Integer(), primary_key=True),
              Column('name', String(200), nullable=False),
              Column('cost_price', Numeric(10, 2), nullable=False),
              Column('selling_price', Numeric(10, 2),  nullable=False),
              Column('quantity', Integer(), nullable=False),
              CheckConstraint('quantity > 0', name='quantity_check')
              )


orders = Table('orders', metadata,
               Column('id', Integer(), primary_key=True),
               Column('customer_id', ForeignKey('customers.id')),
               Column('date_placed', DateTime(), default=datetime.now),
               Column('date_shipped', DateTime())
               )


order_lines = Table('order_lines', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('order_id', ForeignKey('orders.id')),
                    Column('item_id', ForeignKey('items.id')),
                    Column('quantity', Integer())
                    )

metadata.create_all(engine)

connection = engine.connect()


selection =  customers.select()
exec = connection.execute(selection)

print(selection)

for item in exec.fetchall():
    print(item)
'''
ins = customers.insert().values(
    first_name='Jamal',
    last_name='Ibrahim',
    username='captjay98',
    email='captjay98@gmail.com',
    address='Nagogo Street',
    town='Kaduna'
)
print(str(ins))
print(ins.compile().params)

ins1 = insert(customers).values(
    first_name='Khaleed',
    last_name='Abubakar',
    username='Golo1',
    email='iamgolo@mail.com',
    address='Kongo Campus',
    town='Zaria'
)

#exec = connection.execute(ins1)
# print(exec.inserted_primary_key)

ins3 = insert(customers)

exec = connection.execute(ins3,
                          first_name="Nana Khadijah",
                          last_name="Sanusi",
                          username="timsnyder",
                          email="Nanaskwali@yahoo.com",
                          address='Kinkinau',
                          town='Kaduna'
                          )

exec = connection.execute(ins3,
                          [
                              {
                                  "first_name":"Habib",
                                  "last_name":"Samaila",
                                  "username":"bib",
                                  "email":"Bibs@gmail.com",
                                  "address":'Millenium City',
                                  "town":'Kaduna'
                              },

                              {
                                  "first_name":"Muhammed",
                                  "last_name":"Musa BabaSaleh",
                                  "username":"babsal",
                                  "email":"babasal@yahoo.com",
                                  "address":'Gwarimpa',
                                  "town":'Abuja'
                              },
])
print(exec.inserted_primary_key)
print(exec.rowcount)

items_list = [
    {
        "name":"Phone",
        "cost_price":300000,
        "selling_price": 280000,
        "quantity": 4
    },
    {
        "name":"Water Bottle",
        "cost_price": 3000,
        "selling_price": 2900,
        "quantity": 15
    },
    {
        "name":"Oven",
        "cost_price": 90000,
        "selling_price": 820000,
        "quantity": 3
    },
    {
        "name":"Laptop",
        "cost_price": 750000,
        "selling_price": 700000,
        "quantity": 5
    },
    {
        "name":"Headphone",
        "cost_price": 25000,
        "selling_price": 24000,
        "quantity": 5
    },
    {
        "name":"Keyboard",
        "cost_price": 20000,
        "selling_price": 20000,
        "quantity": 10
    },
    {
        "name":"Monitor",
        "cost_price": 300000,
        "selling_price": 300000,
        "quantity": 5
    },
    {
        "name":"SmartWatch",
        "cost_price": 75000,
        "selling_price": 72000,
        "quantity": 3
    },
    
]

order_list = [
    {
        "customer_id": 1
    },
    {
        "customer_id": 1
    }
]

order_line_list = [
    {
        "order_id": 1,
        "item_id": 1,
        "quantity": 1
    }, 
    {
        "order_id": 1,
        "item_id": 2,
        "quantity": 2
    }, 
    {
        "order_id": 1,
        "item_id": 3,
        "quantity": 1
    },
    {
        "order_id": 2,
        "item_id": 1,
        "quantity": 1
    },
    {
        "order_id": 2,
        "item_id": 2,
        "quantity": 5
    },
]

exec = connection.execute(insert(items), items_list)
print(exec.rowcount
exec = connection.execute(insert(orders), order_list)
print(exec.rowcount))
exec = connection.execute(insert(order_lines), order_line_list)
print(exec.rowcount)

selection = select([customers]) #customers.select() 
print(str(selection))

exec = connection.execute(selection)
print(exec.first()
#for item in exec:
#    print(item, "\n \n")

selection = select([items]).where(
    items.c.cost_price > 150000)
print(str(selection))
exec = connection.execute(selection)
print(exec.fetchall())
for items in exec.fetchall():
    print(items, "\n \n")

s = select([items]).\
where(
    (items.c.cost_price + items.c.selling_price > 50) & 
    (items.c.quantity > 10)
)

s = select([items]).\
where(    
    or_(
        items.c.quantity >= 50,
        items.c.cost_price < 100,
    )
) 

s = select([items]).\
where(    
    and_(
        items.c.quantity >= 50,
        items.c.cost_price < 100,
        not_(
            items.c.name == 'Headphone'            
        ),        
    )
)

s = select([orders]).where(
    orders.c.date_shipped == None
)
s = select([orders]).where(
    orders.c.date_shipped != None
)

s = select([customers]).where(
    customers.c.first_name.in_(["Jamal", "Nana Khadijah"])
)

s = select([customers]).where(
    customers.c.first_name.notin_(["Jamal", "Nana Khadijah"])
)

s = select([items]).where(
    items.c.cost_price.between(10, 20)
)

s = select([items]).where(
    not_(items.c.cost_price.between(10, 20))
)

s = select([items]).where(
    items.c.name.like("Wa%")
)

s = select([items]).where(
    not_(items.c.name.like("wa%"))
)

s = select([items]).where(
    items.c.quantity > 10
).order_by(items.c.cost_price)

s = select([items]).where(
    items.c.quantity > 10
).order_by(asc(items.c.cost_price))

s = select([items]).where(
    items.c.quantity > 10
).order_by(desc(items.c.cost_price))


s = select([items]).order_by(
    items.c.quantity, 
    desc(items.c.cost_price)
)

s = select([items]).order_by(
    items.c.quantity
).limit(2)

s = select([items]).order_by(
    items.c.quantity
).limit(2).offset(2)

s = select([items.c.name, items.c.quantity]).where(
    items.c.quantity ==  50
)

s = select([
        items.c.name, 
        items.c.quantity, 
        items.c.selling_price * 5 
    ]).where(
    items.c.quantity ==  50
)

s = select([
        items.c.name, 
        items.c.quantity, 
        (items.c.selling_price * 5).label('price') 
    ]).where(
    items.c.quantity ==  50
)

print(customers.join(orders))

s = select([        
    customers.c.id,
    customers.c.first_name
]).select_from(
    customers
)

from sqlalchemy import and_
s = select([
            orders.c.id,
            orders.c.date_placed
]).select_from(
    orders.join(customers)
).where(
    and_(
        customers.c.first_name == "Jamal",
        customers.c.last_name == "Ibrahim",
    )
)

s = select([        
    customers.c.first_name,
    orders.c.id,
]).select_from(
    customers.outerjoin(orders)
)
print(s)
rs = connection.execute(s)
rs.keys()
print(rs.fetchall())
from sqlalchemy import update

selection = update(customers).where(
    customers.c.id == 5
).values(
    email = 'amiragift@mail.com',
)

print(selection)
exec = connection.execute(selection)

selection = select(customers)

print(selection)
exec = connection.execute(selection)
print(exec.fetchall())
from sqlalchemy import delete

selection = delete(customers).where(
    customers.c.id == 2
)

s = select([customers.c.town]).where(customers.c.id  < 10).distinct()
print(s)

s = select([        
    func.count(distinct(customers.c.town)),
    func.count(customers.c.town)
])

from sqlalchemy import cast, Date

s = select([
    cast(func.pi(), Integer),
    cast(func.pi(), Numeric(10,2)),
    cast("2010-12-01", DateTime),
    cast("2010-12-01", Date),
])

u = union(
    select([items.c.id, items.c.name]).where(items.c.name.like("Wa%")),
    select([items.c.id, items.c.name]).where(items.c.name.like("%e%")),
).order_by(desc("id"))

from sqlalchemy import union_all

s = union_all(
    select([items.c.id, items.c.name]).where(items.c.name.like("Wa%")),
    select([items.c.id, items.c.name]).where(items.c.name.like("%e%")),
).order_by(desc("id"))

s = select([items.c.id, items.c.name]).where(
    items.c.id.in_( 
        select([order_lines.c.item_id]).select_from(customers.join(orders).join(order_lines)).where(    
                and_(
                    customers.c.first_name == 'John',
                    customers.c.last_name == 'Green',
                    orders.c.id == 1
                )    
        )
    )
)

rom sqlalchemy.sql import text

s = text(

SELECT
    orders.id as "Order ID", orders.date_placed, items.id, items.name
FROM
    customers
INNER JOIN orders ON customers.id = orders.customer_id
INNER JOIN order_lines ON order_lines.order_id = orders.id
INNER JOIN items ON items.id= order_lines.item_id
where customers.first_name = :first_name and customers.last_name = :last_name

)
print(s)
rs = conn.execute(s, first_name="John", last_name='Green')
rs.fetchall()

s = select([items]).where(
    text("items.name like 'Wa%'")
).order_by(text("items.id desc"))

print(s)
rs = conn.execute(s)
rs.fetchall()

from sqlalchemy.exc import IntegrityError

'''A transaction is a way to execute a set of SQL statements such that either all of the statements are executed successfully or nothing at all. If any of the statement involved in the transaction fails then the database is returned to the state it was in before the transaction was initiated.

We currently have two orders in the database. To fulfill an order we need to perform following two actions:

Subtract the quantity of ordered items from the items table
Update the date_shipped column to contain the datetime value.
Both of these action must be performed as a unit to ensure that the data in the tables are correct.

The Connection object provides a begin() method, which starts the transaction and returns an object of type Transaction. The Transaction object in turn provides rollback() and commit() method, to rollback and commit the transaction, respectively.

In the following listing we define dispatch_order() method which accepts order_id as argument, and performs the above mentioned actions using transaction.'''
def dispatch_order(order_id):

    # check whether order_id is valid or not
    r = conn.execute(select([func.count("*")]).where(orders.c.id == order_id))
    if not r.scalar():
        raise ValueError("Invalid order id: {}".format(order_id))

    # fetch items in the order
    s = select([order_lines.c.item_id, order_lines.c.quantity]).where(
        order_lines.c.order_id == order_id
    )

    rs = conn.execute(s)
    ordered_items_list = rs.fetchall()

    # start transaction
    t = conn.begin()

    try:
        for i in ordered_items_list:
            u = update(items).where(
                items.c.id == i.item_id
            ).values(quantity = items.c.quantity - i.quantity)

            rs = conn.execute(u)

        u = update(orders).where(orders.c.id == order_id).values(date_shipped=datetime.now())
        rs = conn.execute(u)
        t.commit()
        print("Transaction completed.")

    except IntegrityError as e:
        print(e)
        t.rollback()
        print("Transaction failed.")
        '''
"""