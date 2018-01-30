frappe.pages['sales_dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: __('Sales Dashboard'),
		single_column: true
	});

	frappe.sales_dashboard.make(page);
	frappe.sales_dashboard.run();
    
    // add the application reference
    frappe.breadcrumbs.add("Sales KPI");
}

frappe.sales_dashboard = {
	start: 0,
	make: function(page) {
		var me = frappe.sales_dashboard;
		me.page = page;
		me.body = $('<div></div>').appendTo(me.page.main);
		var data = "";
		$(frappe.render_template('sales_dashboard', data)).appendTo(me.body);

	},
	run: function() {

	}
}
