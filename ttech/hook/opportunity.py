import frappe
import json

@frappe.whitelist()
def create_todo(doc, workflow_action = None):
	doc = json.loads(doc)
	todo = frappe.new_doc("ToDo")
	todo.description = workflow_action
	todo.owner = frappe.session.user
	todo.reference_type = doc.get('doctype')
	todo.reference_name = doc.get('name')
	todo.insert()
	return todo