class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        pass

    def add_category(self, category):
        if category not in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            return

        self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            return

        self.documents.append(document)

    def edit_category(self, id):
        pass

    def edit_topic(self):
        pass

    def edit_document(self):
        pass

    def delete_category(self):
        pass

    def delete_topic(self):
        pass

    def delete_document(self):
        pass

    def get_document(self):
        pass

