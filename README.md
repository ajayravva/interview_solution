# Interview Task – Frappe Assignment

This project implements multiple tasks using the **Frappe Framework** inside a custom app called **interview_solution**.

---

# Setup Instructions

1. Setup a local Frappe environment  
https://docs.frappe.io/framework/user/en/basics/architecture

2. Create a custom app

bench new-app interview_solution

3. Install the app on your site

bench --site site1.local install-app interview_solution

---

# Task 1 — Create Customer Visit DocType

DocType: **Customer Visit**

Fields:

Customer Name – Data  
Sales Person – Data  
Visit Date – Date  
Checkin Time – Datetime  
Checkout Time – Datetime  
Visit Duration – Float  
Status – Select  
Remarks – Small Text  

Status Options:

Planned  
Completed  
Cancelled  

Requirements Implemented:

- Visit Duration automatically calculated when Checkout Time is entered.
- Remarks field is mandatory when Status = Cancelled.
- Checkout Time visible only when Status = Completed.

Location:

interview_solution/doctype/customer_visit/

---

# Task 2 — Child Table with Validation

DocType: **Project Task**

Fields:

Project Name – Data  
Start Date – Date  
End Date – Date  

Child Table: **Task Items**

Fields:

Task Name – Data  
Assigned To – Data  
Estimated Hours – Float  

Validations Implemented:

- Duplicate Task Name entries are prevented.
- Estimated Hours mandatory if Assigned To is filled.

---

# Task 3 — Custom API

Created API function:

get_recent_visits()

Purpose:

Return the **10 most recent Customer Visit records**.

File:

interview_solution/api.py

API Endpoint:

http://localhost:8000/api/method/interview_solution.api.get_recent_visits

---

# Task 4 — Validation Logic

Server-side validations added in Customer Visit.

Rules:

- Checkout Time cannot be earlier than Checkin Time.
- Visit Date cannot be in the future.

File:

interview_solution/doctype/customer_visit/customer_visit.py

---

# Task 5 — Script Report

Created Script Report:

Visit Summary Report

Columns:

Customer Name  
Sales Person  
Visit Date  
Visit Duration  
Status  

Filters:

Visit Date  
Sales Person  

Location:

interview_solution/report/visit_summary_report/

---

# Task 6 — Scheduler Job

Created a daily scheduled job.

Logic:

Find records where

status = Planned  
AND visit_date < today  

Update status to:

Missed

File:

interview_solution/scheduler.py

---

# Task 7 — Client Script

When **Customer Name** is selected in Customer Visit:

Fetch and display the **Last Visit Date** for that customer.

File:

interview_solution/fixtures/client_script.json

---

# Task 8 — Background Job

When a **Customer Visit is submitted**:

Trigger a background job that logs:

Visit completed for customer: <customer_name>

DocType created:

Visit Log

Files:

interview_solution/background_job.py  
interview_solution/doctype/visit_log/

---

# Task 9 — Field Level Permission

Created Role:

Visit Manager

Rules:

- Only Visit Manager can edit the Status field.
- Other users cannot modify the Status field.

Configured using:

Role Permission Manager

---

# Task 10 — Visit Statistics API

Created API function:

get_visit_statistics()

Returns:

- Total Visits
- Completed Visits
- Cancelled Visits
- Average Visit Duration

File:

interview_solution/background_job.py

API Endpoint:

http://localhost:8000/api/method/interview_solution.background_job.get_visit_statistics

Example Response:

{
 "message": {
  "total_visits": 22,
  "completed_visits": 15,
  "cancelled_visits": 2,
  "average_visit_duration": 0.49
 }
}

---

# Author

Ajay Ravva
