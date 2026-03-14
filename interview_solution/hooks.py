app_name = "interview_solution"
app_title = "Interview Solution"
app_publisher = "ajay ravva"
app_description = "Frappe Interview Tasks"
app_email = "ajayravva001@gmail.com"
app_license = "MIT"

scheduler_events = {
    "daily": [
        "interview_solution.scheduler.update_missed_visits"
    ]
}
