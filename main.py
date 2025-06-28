from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
from datetime import datetime, timedelta

celebrity_names = [
    "Pacquiao, Emmanuel Dapidran, P.",
    "Soberano, Liza, S.",
    "Bernardo, Kathryn Chandria, B.",
    "Padilla, Daniel John, P.",
    "Lustre, Nadine, L.",
    "Reid, Robert James, R.",
    "Curtis, Anne, J.",
    "Pascual, Piolo, O.",
    "Geronimo, Sarah, G.",
    "Ganda, Vice, R.",
    "Rivera, Marian, D.",
    "Dantes, Dingdong, A.",
    "Locsin, Angel, C.",
    "Martin, Coco, M.",
]

pup_directors = [
    "Dr. Manuel A. Dela Cruz",
    "Dr. Maria Elena C. De Leon",
    "Dr. Jose R. De Vera",
    "Dr. Rhea Mae A. Villanueva",
    "Dr. Arnel A. De Guzman",
]

pup_positions = [
    "University President",
    "Vice President for Academic Affairs",
    "Vice President for Administration",
    "Registrar",
    "Director of Student Affairs",
    "Director of Admissions",
    "Director of Finance",
    "Director of Human Resources",
    "Director of Research",
    "Department Chair",
    "Program Coordinator",
    "Faculty Member",
    "Administrative Officer",
    "Guidance Counselor",
]

fields_of_expertise = [
    "Computer Science",
    "Business Administration",
    "Education",
    "Engineering",
    "Nursing",
    "Psychology",
    "Information Technology",
    "Marketing",
    "Finance",
    "Hospitality Management",
    "Environmental Science",
    "Graphic Design",
    "Architecture",
    "Law",
    "Medicine",
]

complete_addresses = [
    "123 Rizal Avenue, Quezon City, Metro Manila",
    "456 Magsaysay Boulevard, Cebu City, Cebu",
    "789 Bonifacio Street, Davao City, Davao del Sur",
    "101 Del Pilar Street, Makati, Metro Manila",
    "202 Burgos Street, Taguig, Metro Manila",
    "303 Aguinaldo Highway, Baguio, Benguet",
    "404 Calle Real, Iloilo City, Iloilo",
    "505 P. Burgos Street, Cagayan de Oro, Misamis Oriental",
    "606 Luna Street, Pasig, Metro Manila",
    "707 Quezon Avenue, Manila, Metro Manila",
]

real_subjects = [
    "Professional Ethics",
    "Data Structures",
    "Software Engineering",
    "Database Management Systems",
    "Operating Systems",
    "Web Development",
    "Network Security",
    "Artificial Intelligence",
    "Human-Computer Interaction",
    "Project Management",
    "Digital Marketing",
    "Financial Accounting",
    "Business Law",
    "Microeconomics",
    "Macroeconomics",
]

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def random_number(length):
    return ''.join(random.choice(string.digits) for i in range(length))

def generate_email(full_name):
    first_name = full_name.split(", ")[1].split(" ")[0].lower()
    return f"{first_name}@gmail.com"

def specific_date():
    return "28-06-2025"

def generate_time_range():
    start_hour = random.randint(8, 20) 
    start_minute = random.choice([0, 30])
    start_time = datetime.strptime(f"{start_hour}:{start_minute}", "%H:%M")
    end_time = start_time + timedelta(hours=3)
    return f"{start_time.strftime('%I:%M %p')} - {end_time.strftime('%I:%M %p')}"

driver = webdriver.Chrome()
driver.get("http://localhost/ocss/admin.php")

wait = WebDriverWait(driver, 20)

username = driver.find_element(By.NAME, "admin_username")
username.send_keys("admin")
time.sleep(2)

password = driver.find_element(By.NAME, "admin_pass")
password.send_keys("admin")
time.sleep(2)

login_button = driver.find_element(By.CLASS_NAME, "btn-success")
login_button.click()
time.sleep(2)

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
time.sleep(2)

menu_button = driver.find_element(By.XPATH, "//span[@onclick='openNav()']")
menu_button.click()
time.sleep(2)

employee_form_link = driver.find_element(By.XPATH, "/html/body/div[1]/ul/li[1]/a")
employee_form_link.click()
time.sleep(2)

emp_number = driver.find_element(By.NAME, "emp_number")
emp_number.send_keys(random_number(5))
time.sleep(2) 

full_name = random.choice(celebrity_names)
full_name_field = driver.find_element(By.NAME, "fname")
full_name_field.send_keys(full_name)
time.sleep(2) 

date_hired = driver.find_element(By.NAME, "date_hired")
date_hired.click()
time.sleep(2)
date_hired.send_keys(specific_date())
time.sleep(2)

status_dropdown = driver.find_element(By.NAME, "status")
status_options = ["Part-time Faculty", "Temporary", "Full-time Faculty"]
time.sleep(2)
random_status = random.choice(status_options)
status_dropdown.send_keys(random_status)
time.sleep(2)

field_expertise = driver.find_element(By.NAME, "background_field")
field_expertise.send_keys(random.choice(fields_of_expertise))
time.sleep(2)

address = driver.find_element(By.NAME, "address")
address.send_keys(random.choice(complete_addresses))
time.sleep(2)

contact_number = driver.find_element(By.NAME, "contact_no")
contact_number.send_keys("09" + random_number(9)) 
time.sleep(2)

email = driver.find_element(By.NAME, "email")
email.send_keys(generate_email(full_name))
time.sleep(2)

password_field = driver.find_element(By.NAME, "pass")
password_field.send_keys(random_string(10)) 
time.sleep(2)

submit_button = driver.find_element(By.NAME, "register_faculty")
submit_button.click()

time.sleep(2)

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
time.sleep(2)

menu_button = driver.find_element(By.XPATH, "//span[@onclick='openNav()']")
menu_button.click()
time.sleep(2)

add_subject_link = driver.find_element(By.XPATH, "//a[@data-toggle='modal' and @data-target='#subjectModal']")
add_subject_link.click()
time.sleep(2)

subject_code = driver.find_element(By.NAME, "subject_code")
subject_code.send_keys(f"SUB{random_number(3)}")
time.sleep(2)

subject_description = driver.find_element(By.NAME, "subject_description")
subject_description.send_keys(random.choice(real_subjects))
time.sleep(2)

unit_dropdown = driver.find_element(By.NAME, "unit")
unit_options = ["2", "3", "5"]
time.sleep(2)
random_unit = random.choice(unit_options)
unit_dropdown.send_keys(random_unit)
time.sleep(2)

lecture_dropdown = driver.find_element(By.NAME, "lecture")
lecture_options = ["2", "3"]
time.sleep(2)
random_lecture = random.choice(lecture_options)
lecture_dropdown.send_keys(random_lecture)
time.sleep(2)

laboratory_dropdown = driver.find_element(By.NAME, "laboratory")
laboratory_options = ["0", "2", "3"]
time.sleep(2)
random_laboratory = random.choice(laboratory_options)
laboratory_dropdown.send_keys(random_laboratory)
time.sleep(2)

submit_subject_button = driver.find_element(By.NAME, "add")
submit_subject_button.click()

time.sleep(2)


wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
time.sleep(2)

menu_button = driver.find_element(By.XPATH, "//span[@onclick='openNav()']")
menu_button.click()
time.sleep(2)

add_room_link = driver.find_element(By.XPATH, "//a[@data-toggle='modal' and @data-target='#roomModal']")
add_room_link.click()
time.sleep(2)

room_number = random.randint(101, 107)
room_input = driver.find_element(By.NAME, "room")
room_input.send_keys(str(room_number))
time.sleep(2)

submit_room_button = driver.find_element(By.NAME, "add_room")
submit_room_button.click()

time.sleep(2)

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
time.sleep(2)

menu_button = driver.find_element(By.XPATH, "//span[@onclick='openNav()']")
menu_button.click()
time.sleep(2)

add_time_link = driver.find_element(By.XPATH, "//a[@data-toggle='modal' and @data-target='#timeModal']")
add_time_link.click()
time.sleep(2)

time_range = generate_time_range()
time_input = driver.find_element(By.NAME, "class_time")
time_input.send_keys(time_range)
time.sleep(2)

submit_time_button = driver.find_element(By.NAME, "add_time")
submit_time_button.click()

time.sleep(2)

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
time.sleep(2)

menu_button = driver.find_element(By.XPATH, "//span[@onclick='openNav()']")
menu_button.click()
time.sleep(2)

add_day_link = driver.find_element(By.XPATH, "//a[@data-toggle='modal' and @data-target='#dayModal']")
add_day_link.click()
time.sleep(2)

short_days = {
    "Monday": "m",
    "Tuesday": "t",
    "Wednesday": "w",
    "Thursday": "th",
    "Friday": "f",
    "Saturday": "s"
}
assigned_day = random.choice(list(short_days.values())) 
day_input = driver.find_element(By.NAME, "assigned_day")
day_input.send_keys(assigned_day) 
time.sleep(2)

submit_day_button = driver.find_element(By.NAME, "add_day")
submit_day_button.click()

time.sleep(2)

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
time.sleep(2)

menu_button = driver.find_element(By.XPATH, "//span[@onclick='openNav()']")
menu_button.click()
time.sleep(2)

add_signatory_link = driver.find_element(By.XPATH, "//a[@data-toggle='modal' and @data-target='#signatoryModal']")
add_signatory_link.click()
time.sleep(2)

signatory_full_name = driver.find_element(By.NAME, "sname")
signatory_full_name.send_keys(random.choice(pup_directors)) 
time.sleep(2)

signatory_designation = driver.find_element(By.NAME, "sdesignation")
signatory_designation.send_keys(random.choice(pup_positions))
time.sleep(2)

submit_signatory_button = driver.find_element(By.NAME, "add_signatory")
submit_signatory_button.click()

time.sleep(2)

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@onclick='openNav()']")))
time.sleep(2)

menu_button = driver.find_element(By.XPATH, "//span[@onclick='openNav()']")
menu_button.click()
time.sleep(2)

create_schedule_link = driver.find_element(By.XPATH, "//a[@href='create_schedule.php']")
create_schedule_link.click()
time.sleep(2)

course_description_dropdown = driver.find_element(By.NAME, "subject_description")
course_description_options = course_description_dropdown.find_elements(By.TAG_NAME, "option")
random_course = random.choice(course_description_options[1:])
random_course.click()
time.sleep(2)

days_dropdown = driver.find_element(By.NAME, "day_description")
days_options = days_dropdown.find_elements(By.TAG_NAME, "option")
random_day = random.choice(days_options[1:])
random_day.click()
time.sleep(2)

time_dropdown = driver.find_element(By.NAME, "time_description")
time_options = time_dropdown.find_elements(By.TAG_NAME, "option")
random_time = random.choice(time_options[1:]) 
random_time.click()
time.sleep(2)

room_dropdown = driver.find_element(By.NAME, "room_description")
room_options = room_dropdown.find_elements(By.TAG_NAME, "option")
random_room = random.choice(room_options[1:])
random_room.click()
time.sleep(2)

professor_dropdown = driver.find_element(By.NAME, "fname")
professor_options = professor_dropdown.find_elements(By.TAG_NAME, "option")
random_professor = random.choice(professor_options[1:])
random_professor.click()
time.sleep(2)

save_button = driver.find_element(By.NAME, "add_schedule")
save_button.click()

time.sleep(3)


driver.quit()
