// Copyright (c) 2023, Ttech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Advance', {
	refresh: function(frm) {
		frm.set_value('creator_id', frappe.session.user);
		frm.set_query('currency', function(doc) {
			return {
				filters: {
					'name': ['in', ["IQD", "USD"]]
				}
			}
		})
	}
});