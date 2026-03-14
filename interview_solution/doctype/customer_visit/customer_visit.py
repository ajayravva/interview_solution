import frappe
from frappe.model.document import Document
from frappe.utils import today


class CustomerVisit(Document):

    def validate(self):

        # Rule 1: Checkout cannot be earlier than Checkin
        if self.checkin_time and self.checkout_time:
            if self.checkout_time < self.checkin_time:
                frappe.throw("Checkout Time cannot be earlier than Checkin Time")

        # Rule 2: Visit Date cannot be in the future
        if self.visit_date and self.visit_date > today():
            frappe.throw("Visit Date cannot be in the future")

    def on_submit(self):

        frappe.enqueue(
            "interview_solution.background_job.create_visit_log",
            customer_name=self.customer_name
        )
