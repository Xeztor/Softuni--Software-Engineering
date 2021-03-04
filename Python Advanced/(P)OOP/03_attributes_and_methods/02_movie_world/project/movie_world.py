class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        customers_info = [str(customer) for customer in self.customers]
        dvds_info = [str(dvd) for dvd in self.dvds]
        return '\n'.join(customers_info) + '\n' + '\n'.join(dvds_info) + '\n'

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) == self.customer_capacity():
            return

        self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) == self.dvd_capacity():
            return

        self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.get_customer_by_attr(id=customer_id)
        dvd = self.get_dvd_by_attr(id=dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.get_customer_by_attr(id=customer_id)
        dvd = self.get_dvd_by_attr(id=dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def get_customer_by_attr(self, id=None, name=None):
        if id:
            attr = 'id'
            desired_attr = id
        else:
            attr = 'name'
            desired_attr = name

        for customer in self.customers:
            if getattr(customer, attr) == desired_attr:
                return customer

    def get_dvd_by_attr(self, id=None, name=None):
        if id:
            attr = 'id'
            desired_attr = id
        else:
            attr = 'name'
            desired_attr = name

        for customer in self.dvds:
            if getattr(customer, attr) == desired_attr:
                return customer
