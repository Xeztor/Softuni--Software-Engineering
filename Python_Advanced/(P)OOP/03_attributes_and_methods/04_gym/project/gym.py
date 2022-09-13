class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def get_obj_by_id(obj_list, id):
        for obj in obj_list:
            if obj.id == id:
                return obj

    def add_customer(self, customer):
        if customer in self.customers:
            return

        self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer in self.trainers:
            return

        self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment in self.equipment:
            return

        self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan in self.plans:
            return

        self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription in self.subscriptions:
            return

        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.get_obj_by_id(self.subscriptions, subscription_id)
        subs_customer = self.get_obj_by_id(self.customers, subscription.customer_id)
        subs_trainer = self.get_obj_by_id(self.trainers, subscription.trainer_id)
        trainer_plan = self.get_obj_by_id(self.plans, subs_trainer.id)
        plan_equipment = self.get_obj_by_id(self.equipment, trainer_plan.equipment_id)
        return f"{subscription}\n" \
               f"{subs_customer}\n" \
               f"{subs_trainer}\n" \
               f"{plan_equipment}\n" \
               f"{trainer_plan}"


