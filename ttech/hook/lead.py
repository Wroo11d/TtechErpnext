import frappe
from erpnext.crm.doctype.lead.lead import make_opportunity, make_customer

@frappe.whitelist()
def create_opportunity(source_name, target_doc=None):
    opportunity = make_opportunity(source_name, target_doc=target_doc)
    opportunity.insert(ignore_permissions = True)
    opportunity.save()

@frappe.whitelist()
def create_customer(source_name, target_doc=None):
    customer = make_customer(source_name, target_doc=target_doc)
    customer.customer_group = "All Customer Groups"
    customer.territory = "All Territories"
    customer.insert(ignore_permissions = True)
    customer.save()