// Copyright (c) 2023, Ttech and contributors
// For license information, please see license.txt

frappe.ui.form.on('TTech Settings', {
	refresh: function(frm) {
		frm.set_intro('Exchange Rate Updates Automaticaly Daily at 06:00 AM, Only System Manager can Manually Update it')
		if(frappe.user.has_role('System Manager')){
			frm.set_df_property('exchange_rate',  'read_only', 0);
		}
	}
});
