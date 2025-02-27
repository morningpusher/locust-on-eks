from locust import HttpUser, TaskSet, task, between, constant

class UserBehavior(TaskSet):
    @task(1)
    def profile(self):
        self.client.get("/home", verify=False)

class WebsiteUser(HttpUser):
    tasks = {UserBehavior:1}
    wait_time = constant(0)
    max_wait = 3000
