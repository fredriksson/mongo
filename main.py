__author__ = 'eric'
import First_lanuch
import pymongo
import datetime
import Fetch_API
import time
import Test_data

##### first launch test cases #####


conn = pymongo.Connection('localhost', 27017)


def First_oupt_API(date_start,date_end,feature_name):

    Pacific_return = Fetch_API.URL_gen(feature_name,date_start,date_end,"pacific")

    GMT_return = Fetch_API.URL_gen(feature_name,date_start,date_end,"GMT")



    return Pacific_return,GMT_return




'''
def Result_judgment(Sum_of_input,Sum_of_ouput_Pacific):

    print Sum_of_input
    print Sum_of_ouput_Pacific



    if Sum_of_input == Sum_of_ouput_Pacific[0] or Sum_of_input == Sum_of_ouput_Pacific[1]:

        print "GMT pass!"

    else:
        print "Test failed!"

        return False
'''


date_start = "2010-7-1" # local time

date_end = "2010-7-4"
def bug_reproduce(date_start,date_end,feature_name):

        test_result_pass = []
        test_result_failed = []



        #### Data Base init ####

        #db = conn.ymca

        #db.events.remove({"properties.YA0token":"8416e32af87f11e284c212313b0ace15"})

        print "Test Cases name:",feature_name

        """input_data = First_lanuch.first_launch_gen(feature_name,datetime.datetime.fromtimestamp(First_lanuch.Feature_range(date_start, date_end)[0]).strftime("%Y-%m-%d %H:%M:%S"),
                                              First_lanuch.Feature_range(date_start, date_end)[4], post_enable=1)"""


        input_data = Test_data.Input_data_gen(datetime.datetime.fromtimestamp(Test_data.Feature_range(date_start, date_end)[0]).strftime("%Y-%m-%d %H:%M:%S"),
                                              duration = int(Test_data.Feature_range(date_start, date_end)[4]), post_enable=1)







        output_data = First_oupt_API(date_start,date_end,feature_name)[1]

        len_1 = len(input_data[1])

        len_2 = len(output_data[1])

        print "Number of input:",len_1,"Number of output:",len_2

        if len_1 == len_2:
            for pos in range(len_1):

                #print "input",input_data[1][pos]
                #print "output",output_data[1][pos]

                off_set = int(output_data[1][pos]['ts']) + 25200  # offset + 7 hours
                #print off_set

                if input_data[1][pos]['ts'] == off_set and input_data[1][pos]['user'] == output_data[1][pos]['users']:  ########## when TS from API = TS from list, and

                    result_pass =  "Test Result of:" + feature_name + " " + str(pos) +" ==============PASS=============="
                    #print result_pass

                    test_result_pass.append(result_pass)


                else:

                    result_failed =  "Test Result of:" + feature_name + " " + str(pos) + " ==============Failed=============="

                    #print result_failed

                    test_result_failed.append(result_failed)



        else:
            pass

            #print "input output not equal =================Failed=================="



        return test_result_pass,test_result_failed








if __name__ == '__main__':





    #while bug_reproduce() != False:






    bug_reproduce(date_start,date_end,feature_name = "first_launches")

    #bug_reproduce(date_start,date_end,feature_name = "user_start")







