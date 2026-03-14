import frappe

def execute(filters=None):

    columns = [
        {"label": "ID", "fieldname": "name", "fieldtype": "Data", "width": 200},
        {"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Data", "width": 200},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 120},
        {"label": "Visit Duration", "fieldname": "visit_duration", "fieldtype": "Float", "width": 120},
    ]

    data = frappe.get_all(
        "Customer Visit",
        fields=["name", "customer_name", "status", "visit_duration"],
        order_by="creation desc"
    )

    return columns, data
