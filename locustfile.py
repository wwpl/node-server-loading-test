from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    host="http://container_node_dfasdfasd:3000"
    @task
    def hello_world(self):
        self.client.get("/")