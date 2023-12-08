// Copyright (c) 2023, Ttech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Opportunity', {
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
		['Site Survey', 'Gather Requirements'].includes(frm.selected_workflow_action)
	) {
		frappe.call({
			method: "ttech.hook.opportunity.create_todo",
			args: {
				doc: frm.doc,
				workflow_action: frm.selected_workflow_action
			},
			callback: function (r) {
			}
		});
	}
}