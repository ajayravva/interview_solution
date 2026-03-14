import frappe
from frappe.utils import today

def update_missed_visits():
    visits = frappe.get_all(
        "Customer Visit",
        filters={
            "status": "Planned",
            "visit_date": ["<", today()]
        },
        fields=["name"]
    )

    for visit in visits:
        frappe.db.set_value("Customer Visit", visit.name, "status", "Missed")

    frappe.db.commit()
