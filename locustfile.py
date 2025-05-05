from locust import between, task, HttpUser,TaskSet

MIN_WAIT=0
MAX_WAIT=0

class StaticFileTask(TaskSet):
    @task
    def static_file(self):
        self.client.get("/")

class StaticFileOnly(HttpUser):
    tasks=[StaticFileTask]
    wait_time = between(MIN_WAIT, MAX_WAIT) 

class ReadTask(TaskSet):
    @task
    def get_user(self):
        self.client.get("/api/users")
    
class ReadOnly(HttpUser):
    tasks=[ReadTask]
    wait_time = between(MIN_WAIT, MAX_WAIT) 