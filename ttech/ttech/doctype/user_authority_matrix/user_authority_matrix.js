// Copyright (c) 2023, Ttech and contributors
// For license information, please see license.txt

frappe.ui.form.on('User Authority Matrix', {
	refresh: function(frm) {
		if(frm.doc.currency == "IQD"){
			frm.set_intro('This is auto generated, IQD Amount will be auto updated daily at 06:00 AM as per exchange rate.', 'red')
		}
	}
});
