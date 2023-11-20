import frappe
from frappe.permissions import add_permission, update_permission_property

def execute():
	print("Started Copying All Sales Roles to Project Manager....")

	fo_perm = ['read', 'write', 'create', 'select', 'delete', 'submit', 'cancel', 'amend', 'print', 
		'email', 'report', 'import', 'export', 'share']

	all_accounts_manager_allowed_doctype = frappe.db.get_list('DocPerm', 
		filters={'role': 'Sales Manager'}, 
		fields=['*'], ignore_permissions = True)
	for doc_type in all_accounts_manager_allowed_doctype:
		print("Copying Perm from {0} for Sales Manager.....".format(doc_type.parent))
		add_permission(doc_type.parent, "Project Manager", permlevel=doc_type.permlevel, ptype=None)
		for perm in fo_perm:
			update_permission_property(doc_type.parent, "Project Manager", doc_type.permlevel, perm, doc_type[perm])

	print("All Sales Manager Perms Copied to Project Manager")


	all_accounts_user_allowed_doctype = frappe.db.get_list('DocPerm', 
		filters={'role': 'Sales User'}, 
		fields=['*'], ignore_permissions = True)
	for doc_type in all_accounts_manager_allowed_doctype:
		print("Copying Perm from {0} for Sales User.....".format(doc_type.parent))

		add_permission(doc_type.parent, "Project Manager", permlevel=doc_type.permlevel, ptype=None)
		for perm in fo_perm:
			update_permission_property(doc_type.parent, "Project Manager", doc_type.permlevel, perm, doc_type[perm])

	print("All Sales User Role Copied to Project Manager")