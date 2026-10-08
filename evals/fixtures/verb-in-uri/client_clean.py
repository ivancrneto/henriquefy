class EduzzClient:
    def __init__(self, session):
        self.session = session

    def get_me(self):
        return self.session.get("/user/get_me")

    def set_me(self, data):
        return self.session.post("/user/set_me", json=data)
