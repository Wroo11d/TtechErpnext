// Copyright (c) 2023, Ttech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Advance', {
	refresh: function(frm) {
		if(frm.doc.__islocal){
			frm.set_value('creator_id', frappe.session.user);
		}
		frm.set_query('currency', function(doc) {
			return {
				filters: {
					'name': ['in', ["IQD", "USD"]]
				}
			}
		})
		make_finance_field_reqd(frm);
	}
});

function make_finance_field_reqd(frm) {
	if(frm.doc.__islocal){
		frm.set_df_property('advance_account', 'reqd', 0);
		frm.set_df_property('cost_center', 'reqd', 0);
	}
	if(!frm.doc.__islocal && (!frm.doc.advance_account || !frm.doc.cost_center) && 
	(frappe.user.has_role("CFO") || frappe.user.has_role("Finance Manager") || frappe.user.has_role("Finance Officer"))){
		frm.dirty();
		frm.set_df_property('advance_account', 'reqd', 1);
		frm.set_df_property('cost_center', 'reqd', 1);
	}
}