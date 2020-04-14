import datetime

testing_var = datetime.time
testing_list = [int(testing_var)]
for number in testing_list:
    testing_var = int(number) + 12
    testing_list.append(testing_var)

print (testing_var)

