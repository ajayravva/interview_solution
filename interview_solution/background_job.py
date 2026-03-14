import frappe

def create_visit_log(customer_name):

    message = f"Visit completed for customer: {customer_name}"

    log = frappe.get_doc({
        "doctype": "Visit Log",
        "log_message": message
    })

    log.insert(ignore_permissions=True)

    frappe.db.commit()


@frappe.whitelist()
def get_visit_statistics():

    total_visits = frappe.db.count("Customer Visit")

    completed_visits = frappe.db.count("Customer Visit", {
        "status": "Completed"
    })

    cancelled_visits = frappe.db.count("Customer Visit", {
        "status": "Cancelled"
    })

    avg_duration = frappe.db.sql("""
        SELECT AVG(visit_duration)
        FROM `tabCustomer Visit`
    """)[0][0]

    return {
        "total_visits": total_visits,
        "completed_visits": completed_visits,
        "cancelled_visits": cancelled_visits,
        "average_visit_duration": avg_duration
    }
