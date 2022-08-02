// Copyright (c) 2022, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Amount Request', {
	employee: function (frm) {
		frappe.call({
			method: 'erpnext.accounts.utils.get_balance_on',
			args: {
				party_type: "Employee",
				party: frm.doc.employee
			}, callback: function (r) {
				frm.set_value("party_balance", r.message)
			}
		})
	},

	validate: function (frm) {
		let total_amount = frm.doc.amount_request_detail.reduce(function (acc, item) { return acc + item.amount; }, 0);
		frm.set_value("total_amount", total_amount)
		frm.set_value("balance_after_request", total_amount - (frm.doc.party_balance || 0))
	},


});
