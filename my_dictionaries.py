"""
This python code is from day 9 of my 100 day challenge
Made by: Jiwon Sin
"""

student_scores = {
  "Harry": 81,
	"Ron": 78,
	"Hermione": 99,
	"Draco": 74,
	"Neville": 62,
}

travel_logs = [
	{
		"country": "France",
		"visits": 12,
		"cities": ["Paris","Lille","Dijon"],
	},
	{
		"country": "Germany",
		"visits": 5,
		"cities": ["Berlin","Hamberg","Sttugart"],
	},
]

student_grades = {}

def classify_grades(score):
	if score > 100 or score < 0:
		return -1
	elif score > 90:
		return "Outstanding"
	elif score > 80:
		return "Exceeds Expections"
	elif score > 70:
		return "Acceptable"
	else:
		return "Fail"

def student():
	for student in student_scores:
		score = classify_grades(student_scores[student])
		student_grades[student] = score

	print(student_grades)

def add_new_country(country_name, visit_freq, cities_list):
	new_log = {}
	new_log["country"] = country_name
	new_log["visits"] = visit_freq
	new_log["cities"] = cities_list
	travel_logs.append(new_log)

add_new_country()