import frappe

def execute():
	roles = ['CFO', 'Finance Manager', 'Finance Officer']
	for role in roles:
		if not frappe.db.exists('Role', role):
			role_doc = frappe.new_doc('Role')
			role_doc.role_name = role
			role_doc.flags.ignore_permissions = True
			role_doc.save()