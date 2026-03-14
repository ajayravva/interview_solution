import frappe

@frappe.whitelist()
def get_recent_visits():
    visits = frappe.get_all(
        "Customer Visit",
        fields=[
            "name",
            "customer_name",
            "visit_date",
            "checkin_time",
            "checkout_time",
            "visit_duration"
        ],
        order_by="creation desc",
        limit=10
    )
    return visits
