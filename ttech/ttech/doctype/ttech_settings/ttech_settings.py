# Copyright (c) 2023, Ttech and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt, now
from frappe.model.document import Document

class TTechSettings(Document):
	def on_update(self):
		self.db_set('last_updated_on', now())
		self.update_exchange_rate_in_matrix()

	def update_exchange_rate_in_matrix(self):
		all_usd_rules = frappe.db.get_list('User Authority Matrix', filters={'currency':'USD'},
			fields=['name','maximum_allowed_amount', 'role', 'doctype_name'], ignore_permissions = True)

		for rule in all_usd_rules:
			iqd_rule_id = "{0}-{1}-{2}".format(rule.role, rule.doctype_name, 'IQD')

			frappe.db.set_value('User Authority Matrix', iqd_rule_id, {
				'last_updated_on' : now(),
				'maximum_allowed_amount' : flt(self.exchange_rate * rule.maximum_allowed_amount)
			})