# Copyright (c) 2023, Ttech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
from frappe.utils import flt

class UserAuthorityMatrix(Document):
	def after_insert(self):
		if self.currency == "USD":
			self.insert_user_authority_matrix_for_company_currency()

	def insert_user_authority_matrix_for_company_currency(self):
		default_company_currency = frappe.db.get_single_value('Global Defaults', 'default_currency')
		exchange_rate = frappe.db.get_single_value('TTech Settings', 'exchange_rate')
		if not default_company_currency:
			frappe.throw("Please enter default currency in <b>Global Defaults</b>")

		rule_id = "{0}-{1}-{2}".format(self.role, self.doctype_name, self.currency)
		if frappe.db.exists('User Authority Matrix', rule_id):
			iqd_rule = frappe.new_doc('User Authority Matrix')
			iqd_rule.role = self.role
			iqd_rule.doctype_name = self.doctype_name
			iqd_rule.currency = default_company_currency
			iqd_rule.maximum_allowed_amount = flt(self.maximum_allowed_amount * exchange_rate)
			iqd_rule.flags.ignore_permissions = True
			iqd_rule.insert()