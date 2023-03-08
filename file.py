import json

f = open('data/xaa')

line = f.readline()

while line:
    line = 'asdf'

    company = ''

    while line !='    },\n':
        line = f.readline()

        if line == "":
            break

        company += line

        json_object = json.loads(company.strip().strip(','))

        kood = json_object['ariregistri_kood']

        piirkond = json_object['yldandmed']['piirkond_tekstina']

        tegevusalad = json_object['yldandmed']['teatatud_tegevusalad'][0]['emtak_kood']

    print(kood, piirkond, tegevusalad)