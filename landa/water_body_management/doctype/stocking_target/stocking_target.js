// Copyright (c) 2022, Real Experts GmbH and contributors
// For license information, please see license.txt

{% include "landa/water_body_management/stocking_controller.js" %}


frappe.ui.form.on("Stocking Target", {
	refresh: function (frm) {
		if (frm.is_new() && !frm.doc.year) {
			landa.utils.set_default_year(frm);
		}
		frm.add_custom_button(__("Create Stocking Measure"), () =>
			frappe.model.open_mapped_doc({
				method:
					"landa.water_body_management.doctype.stocking_target.stocking_target.create_stocking_measure",
				frm: frm,
			})
		);
	},
});

cur_frm.script_manager.make(landa.StockingController);
