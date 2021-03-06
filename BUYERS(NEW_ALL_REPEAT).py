__author__ = 'eric'
# ##### Create by Eric Wang ######
# ##### Create date 8/10/2014 ####
# ##### For "DAU" feature test ######
# #####  Generate 30 days user data ######

import uuid
from Generic_lib import Data_gen
import time
import datetime
from datetime import date
import pymongo
import random
from Generic_lib import test_conf
import json

db = test_conf.current_database


def Feature_range(date_start, date_end):
    base_time = " 00:00:00"  # 00:00:00

    date_start_time = int(time.mktime(time.strptime(str(date_start + base_time), "%Y-%m-%d %H:%M:%S")))
    date_end_time = int(time.mktime(time.strptime(str(date_end + base_time), "%Y-%m-%d %H:%M:%S")))

    API_start = date_start
    API_end = date_end

    duration = int((date_end_time - date_start_time) / 86400) + 2

    return date_start_time, date_end_time, API_start, API_end, duration


def Input_data_gen(date_start, duration, post_enable):
    #users_daily = []

    amount_user = 0
    country_code = "CA"

    sum = 0
    for days in range(1, duration):
        users_daily_list = []


        current_date = str(
            datetime.datetime(*time.strptime(date_start, '%Y-%m-%d %H:%M:%S')[:6]) + datetime.timedelta(days - 1))

        cTime = int(time.mktime(time.strptime(str(current_date), "%Y-%m-%d %H:%M:%S")))

        # ###################### First_launches users ########################
        #for amount_user in range(1*days):
        for amount_user in range(10):

            country_code = random.choice(['CA'])
            distinct_id = str(country_code + "-" + str(uuid.uuid1()))


            #################### push distinct_id into retention list#####

            users_daily_list.append(distinct_id)



            ####################    DAU #############################

            YA0birth_users = Data_gen.package_generator("YA0charge", cTime, distinct_id, country_code)
            date_post(YA0birth_users, post_enable)

            # the following data should not be display on dashboard because they have same distinct_id as before
            YA0birth_users = Data_gen.package_generator("YA0charge", cTime, distinct_id, country_code)
            date_post(YA0birth_users, post_enable)


            ##### retention data as follow ####

            #print len(users_daily_list),amount_user + 1
        if len(users_daily_list) == (amount_user + 1):
            cTime = cTime + 86400



            for users_daily_id in users_daily_list:



                YA0birth_users = Data_gen.package_generator("YA0charge", cTime, users_daily_id, country_code)
                date_post(YA0birth_users, post_enable)





# #################################	Retention Event end ######################################



def date_post(event, post_enable):
    if post_enable == 1:
        global db

        db.events.insert(event)

    else:
        pass


if __name__ == '__main__':
    a = Input_data_gen(
        datetime.datetime.fromtimestamp(Feature_range(test_conf.Date_start, test_conf.Date_end)[0]).strftime(
            "%Y-%m-%d %H:%M:%S"),
        duration=int(Feature_range(test_conf.Date_start, test_conf.Date_end)[4]),
        post_enable=1)
    print a






