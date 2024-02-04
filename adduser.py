import csv
import requests
import time

fqdn = input("Enter yor Moodle FQDN (my.moodleserver.com)")
baseUrl = f'https://{fqdn}/webservice/rest/server.php'
wstoken = input("Please Enter Your Moodle Token:")
cohortId = input('Enter Your Cohort ID:')

# x = requests.post(url)

# print(x.text)


try:
    with open('test.csv', 'r') as csvfile:
        data = csv.DictReader(csvfile)
        for line in data:
            try:
                url = baseUrl + \
                    f'?wstoken={wstoken}&wsfunction=core_user_create_users&moodlewsrestformat=json&'
                addtoMoodle = requests.post(
                    url+f'users[0][username]={line["username"]}&users[0][password]={line["password"]}&users[0][firstname]={line["firstname"]}&users[0][lastname]={line["lastname"]}&users[0][email]={line["email"]}')
                print(addtoMoodle.text)
                print(line)
                time.sleep(10)
                url = baseUrl + \
                    f'?wstoken={wstoken}&wsfunction=core_cohort_add_cohort_members&moodlewsrestformat=json&members[0][cohorttype][type]=id&members[0][cohorttype][value]={cohortId}'
                addtoCohort = requests.post(
                    url+f'&members[0][usertype][type]=username&members[0][usertype][value]={line["username"]}')
                print(addtoCohort.text)
            except:
                print("An Error Occurred While adding Users!")
    csvfile.close()
except:
    print("An Error Occurred While Opening File!")
