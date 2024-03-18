from locust import events

from TaskSetLib.CategoryNavigate import CategoryNavigate
from TaskSetLib.ViewCart import ViewCart
from UserLib.GuestHttpUser import GuestHttpUser
from UserLib.RegisteredHttpUser import RegisteredHttpUser
from TaskSetLib.MyAccountNavigate import MyAccountNavigate
from CommonLib.UserLoader import UserLoader
from CommonLib.LogModule import Logger
# from CommonLib.EventInfluxHandlers import EventInfluxHandlers


@events.test_start.add_listener
def on_test_start(**kwargs):
    if kwargs['environment'].parsed_options.logfile:
        Logger.init_logger(__name__, kwargs['environment'].parsed_options.logfile)
    UserLoader.load_users()
    # EventInfluxHandlers.init_influx_client()
    Logger.log_message("......... Initiating Load Test .......")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    Logger.log_message("........ Load Test Completed ........")


class UserGroupA(RegisteredHttpUser):
    weight = 1
    RegisteredHttpUser.tasks = [MyAccountNavigate, CategoryNavigate, ViewCart]


class UserGroupB(GuestHttpUser):
    weight = 4
    GuestHttpUser.tasks = [CategoryNavigate, ViewCart]



# perf_user_1@gmail.com,perf_user_1_12@@
# perf_user_2@gmail.com,perf_user_2_12@@
# perf_user_3@gmail.com,perf_user_3_12@@
# perf_user_4@gmail.com,perf_user_4_12@@
# perf_user_5@gmail.com,perf_user_5_12@@


