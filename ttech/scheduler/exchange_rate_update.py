import frappe
import requests
from frappe.utils import flt, now

def update_exchange_rate():
	default_company_currency = frappe.db.get_single_value('Global Defaults', 'default_currency')
	try:
		url = "https://api.exchangerate-api.com/v4/latest/USD"
		response = requests.get(url)

		data = response.json()

		frappe.db.set_value('TTech Settings', 'TTech Settings', {
			'exchange_rate': data.get('rates')[default_company_currency],
			'last_updated_on': now()
		})
		frappe.db.commit()
		update_exchange_rate_in_matrix()

	except Exception as error:
		frappe.log_error("Exchange Rate Update Error", str(error))

def update_exchange_rate_in_matrix():
	exchange_rate = frappe.db.get_single_value('TTech Settings', 'exchange_rate')
	all_usd_rules = frappe.db.get_list('User Authority Matrix', filters={'currency':'USD'},
		fields=['name','maximum_allowed_amount', 'role', 'doctype_name'], ignore_permissions = True)

	for rule in all_usd_rules:
		iqd_rule_id = "{0}-{1}-{2}".format(rule.role, rule.doctype_name, 'IQD')

		frappe.db.set_value('User Authority Matrix', iqd_rule_id, {
			'last_updated_on' : now(),
			'maximum_allowed_amount' : flt(exchange_rate * rule.maximum_allowed_amount)
		})