from locust import task, SequentialTaskSet
from CommonLib.LogModule import *
from CommonLib.UtilHelper import UtilHelper


class CategoryNavigate(SequentialTaskSet):

    def on_start(self):
        self.header = UtilHelper.get_base_header_with_cookie(self.user.get_cookie())

    @task
    def navigate_to_women_category(self):
        with self.client.get("/index.php?id_category=3&controller=category", headers=self.header,
                             catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to navigate to women category, EXCEPTION: " + response.text)
                Logger.log_message("Failed to navigate to women category, Status Code-" +
                                   str(response.status_code), LogType.ERROR)

    @task
    def navigate_to_dresses_category(self):
        with self.client.get("/index.php?id_category=8&controller=category", headers=self.header,
                             catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to navigate to dresses category, EXCEPTION: " + response.text)
                Logger.log_message("Failed to navigate to dresses category, Status Code-" +
                                   str(response.status_code), LogType.ERROR)

    @task
    def navigate_to_shirt_category(self):
        with self.client.get("/index.php?id_category=5&controller=category", headers=self.header,
                             catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to navigate to shirt category, EXCEPTION: " + response.text)
                Logger.log_message("Failed to navigate to shirt category, Status Code-" +
                                   str(response.status_code), LogType.ERROR)

    # @task
    # def logout(self):
    #     with self.client.get("/index.php?mylogout=", data={"mylogout": ""}, headers=self.header,
    #                          catch_response=True) as response:
    #         if response.status_code == 200:
    #             if "Please enter your email address to create an account" in response.text:
    #                 response.success()
    #             else:
    #                 response.failure("Failed to logout, EXCEPTION: " + response.text)
    #                 Logger.log_message("Failed to logout, Status Code-" +
    #                                str(response.status_code), LogType.ERROR)

    @task
    def exit_task_execution(self):
        self.interrupt()
