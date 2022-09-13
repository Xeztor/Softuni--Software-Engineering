class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        return '\n'.join([str(doc) for doc in self.documents]) + '\n'

    @staticmethod
    def get_obj_by_attr_val(objects: list, **kwargs):
        attribute_name, target_value = kwargs.popitem()
        for obj in objects:
            if hasattr(obj, attribute_name) and getattr(obj, attribute_name) == target_value:
                return obj

    def add_category(self, category):
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic):
        if topic in self.topics:
            return

        self.topics.append(topic)

    def add_document(self, document):
        if document in self.documents:
            return

        self.documents.append(document)

    def edit_category(self, id, new_name):
        category = self.get_obj_by_attr_val(self.categories, id=id)
        category.edit(new_name)

    def edit_topic(self, id, new_topic, new_storage_folder):
        topic = self.get_obj_by_attr_val(self.topics, id=id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, id, new_file_name):
        doc = self.get_obj_by_attr_val(self.documents, id=id)
        doc.edit(new_file_name)

    def delete_category(self, id):
        category = self.get_obj_by_attr_val(self.categories, id=id)
        self.categories.remove(category)

    def delete_topic(self, id):
        topic = self.get_obj_by_attr_val(self.topics, id=id)
        self.topics.remove(topic)

    def delete_document(self, id):
        doc = self.get_obj_by_attr_val(self.documents, id=id)
        self.documents.remove(doc)

    def get_document(self, id):
        doc = self.get_obj_by_attr_val(self.documents, id=id)
        return str(doc)
