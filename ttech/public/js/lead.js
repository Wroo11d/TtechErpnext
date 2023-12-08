// Copyright (c) 2023, Ttech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Lead', {
	refresh: function (frm) {
		hide_buttons(frm);
	},
	before_workflow_action: (frm) => {
		execute_workflow_action(frm);
	}
});

function hide_buttons(frm) {
	setTimeout(() => {
		$(`[data-label="${encodeURIComponent('Create')}"]`).addClass("hide")
		$(`[data-label="${encodeURIComponent('Action')}"]`).addClass("hide")
	}, 1000);
}

function execute_workflow_action(frm) {
	if (
		frm.doc.workflow_state === "Qualified" &&
		frm.selected_workflow_action === "Opportunity"
	) {
		frappe.model.open_mapped_doc({
			method: "ttech.hook.lead.create_opportunity",
			frm: frm
		});
	}

	if (
		frm.doc.workflow_state === "Qualified" &&
		frm.selected_workflow_action === "Customer"
	) {
		frappe.model.open_mapped_doc({
			method: "ttech.hook.lead.create_customer",
			frm: frm
		});
	}
}