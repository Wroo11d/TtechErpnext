import frappe
from frappe.permissions import add_permission, update_permission_property

def execute():
	print("Started Copying All Finance Roles to CFO.....")

	cfo_perm = ['read', 'write', 'create', 'select', 'delete', 'cancel', 'amend', 'print', 
		'email', 'report', 'import', 'export', 'share']

	all_accounts_manager_allowed_doctype = frappe.db.get_list('DocPerm', 
		filters={'role': 'Accounts Manager'}, 
		fields=['*'], ignore_permissions = True)
	for doc_type in all_accounts_manager_allowed_doctype:
		print("Copying Perm from {0} for Accounts Manager.....".format(doc_type.parent))
		add_permission(doc_type.parent, "CFO", permlevel=doc_type.permlevel, ptype=None)
		for perm in cfo_perm:
			update_permission_property(doc_type.parent, "CFO", doc_type.permlevel, perm, doc_type[perm])

	print("All Accounts Manager Perms Copied to CFO")


	all_accounts_user_allowed_doctype = frappe.db.get_list('DocPerm', 
		filters={'role': 'Accounts User'}, 
		fields=['*'], ignore_permissions = True)
	for doc_type in all_accounts_manager_allowed_doctype:
		print("Copying Perm from {0} for Accounts User.....".format(doc_type.parent))

		add_permission(doc_type.parent, "CFO", permlevel=doc_type.permlevel, ptype=None)
		for perm in cfo_perm:
			update_permission_property(doc_type.parent, "CFO", doc_type.permlevel, perm, doc_type[perm])

	print("All Accounts User Role Copied to CFO")