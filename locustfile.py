from locust import HttpUser, task, between

class FastApiUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def access_root(self):
        self.client.get("/")
