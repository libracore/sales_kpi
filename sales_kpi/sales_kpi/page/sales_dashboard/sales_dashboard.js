frappe.pages['sales_dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: __('Sales Dashboard'),
		single_column: true
	});

	frappe.sales_dashboard.make(page);
	frappe.sales_dashboard.run(page);
    
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
	run: function(page) {
        get_opportunities(page);
        get_quotations_ytd(page);
        get_sales_orders_ytd(page);
        get_sales_invoices_ytd(page);
        get_quotations_py(page);
        get_sales_orders_py(page);
        get_sales_invoices_py(page);
	}
}

function get_opportunities(page) {
    frappe.call({
        "method": "sales_kpi.sales_kpi.page.sales_dashboard.sales_dashboard.get_opportunities",
        "callback": function(r) {
            var container = page.main.find(".opportunity_count").empty();
            if (r.message.opportunities != 'None') {
                //window.alert("Opportunities: " + r.message.toSource());
                $('<h1>' + r.message.opportunities.count + '</h1>').appendTo(container);
            } else {
                $('<h1>0</h1>').appendTo(container);
            }
        }
    });
}

function get_quotations_ytd(page) {
    frappe.call({
        "method": "sales_kpi.sales_kpi.page.sales_dashboard.sales_dashboard.get_quotations_ytd",
        "callback": function(r) {
            var container = page.main.find(".quotations_ytd").empty();
            if (r.message.quotations != 'None') {
                //window.alert("Opportunities: " + r.message.toSource());
                //var company = frappe.defaults.get_user_default("company");
                var currency = frappe.defaults.get_global_default("currency");
                $('<h1>' + currency + ' ' 
                    + r.message.quotations.sum.toLocaleString() 
                    + ' (' + r.message.quotations.count + ')</h1>').appendTo(container);
            } else {
                $('<h1>0</h1>').appendTo(container);
            }
        }
    });
}

function get_sales_orders_ytd(page) {
    frappe.call({
        "method": "sales_kpi.sales_kpi.page.sales_dashboard.sales_dashboard.get_sales_orders_ytd",
        "callback": function(r) {
            var container = page.main.find(".sales_orders_ytd").empty();
            if (r.message.orders != 'None') {
                var currency = frappe.defaults.get_global_default("currency");
                $('<h1>' + currency + ' ' 
                    + r.message.orders.sum.toLocaleString() 
                    + ' (' + r.message.orders.count + ')</h1>').appendTo(container);
            } else {
                $('<h1>0</h1>').appendTo(container);
            }
        }
    });
}

function get_sales_invoices_ytd(page) {
    frappe.call({
        "method": "sales_kpi.sales_kpi.page.sales_dashboard.sales_dashboard.get_sales_invoices_ytd",
        "callback": function(r) {
            var container = page.main.find(".sales_invoices_ytd").empty();
            if (r.message.invoices != 'None') {
                var currency = frappe.defaults.get_global_default("currency");
                $('<h1>' + currency + ' ' 
                    + r.message.invoices.sum.toLocaleString() 
                    + ' (' + r.message.invoices.count + ')</h1>').appendTo(container);
            } else {
                $('<h1>0</h1>').appendTo(container);
            }
        }
    });
}

function get_quotations_py(page) {
    frappe.call({
        "method": "sales_kpi.sales_kpi.page.sales_dashboard.sales_dashboard.get_quotations_py",
        "callback": function(r) {
            var container = page.main.find(".quotations_py").empty();
            if (r.message.quotations != 'None') {
                var currency = frappe.defaults.get_global_default("currency");
                $('<h1>' + currency + ' ' 
                    + r.message.quotations.sum.toLocaleString() 
                    + ' (' + r.message.quotations.count + ')</h1>').appendTo(container);
            } else {
                $('<h1>0</h1>').appendTo(container);
            }
        }
    });
}

function get_sales_orders_py(page) {
    frappe.call({
        "method": "sales_kpi.sales_kpi.page.sales_dashboard.sales_dashboard.get_sales_orders_py",
        "callback": function(r) {
            var container = page.main.find(".sales_orders_py").empty();
            if (r.message.orders != 'None') {
                var currency = frappe.defaults.get_global_default("currency");
                $('<h1>' + currency + ' ' 
                    + r.message.orders.sum.toLocaleString() 
                    + ' (' + r.message.orders.count + ')</h1>').appendTo(container);
            } else {
                $('<h1>0</h1>').appendTo(container);
            }
        }
    });
}

function get_sales_invoices_py(page) {
    frappe.call({
        "method": "sales_kpi.sales_kpi.page.sales_dashboard.sales_dashboard.get_sales_invoices_py",
        "callback": function(r) {
            var container = page.main.find(".sales_invoices_py").empty();
            if (r.message.invoices != 'None') {
                var currency = frappe.defaults.get_global_default("currency");
                $('<h1>' + currency + ' ' 
                    + r.message.invoices.sum.toLocaleString() 
                    + ' (' + r.message.invoices.count + ')</h1>').appendTo(container);
            } else {
                $('<h1>0</h1>').appendTo(container);
            }
        }
    });
}
