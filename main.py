import json

dna = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"
criminal = {}

hair_color = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
face_shape = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eye_color = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}

for key, value in hair_color.items():
    if value in dna:
        criminal["hair_color"] = key

for key, value in face_shape.items():
    if value in dna:
        criminal["face_shape"] = key

for key, value in eye_color.items():
    if value in dna:
        criminal["eye_color"] = key

for key, value in gender.items():
    if value in dna:
        criminal["gender"] = key

for key, value in race.items():
    if value in dna:
        criminal["race"] = key

with open("data.json", "r") as data_file:
    data_list = json.loads(data_file.read())

for data in data_list:
    if data["hair_color"] == criminal["hair_color"] and data["eye_color"] == criminal["eye_color"] and data["face_shape"] == criminal["face_shape"] and data["gender"] == criminal["gender"] and data["race"] == criminal["race"]:
        print("The criminal who ate all the icecream is", data["name"])

