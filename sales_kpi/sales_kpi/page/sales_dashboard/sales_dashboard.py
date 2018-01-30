# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, libracore and contributors
# License: AGPL v3. See LICENCE

from __future__ import unicode_literals
import frappe
from frappe import throw, _
from datetime import datetime

def foo():
    pass

@frappe.whitelist()
def get_opportunities():
    sql_query = """SELECT COUNT(`name`) AS `count`
        FROM `tabOpportunity` 
        WHERE `status` = 'Open' """
    opportunities = frappe.db.sql(sql_query, as_dict=True)
    if opportunities:
        return {'opportunities': opportunities[0] }
    else:
        return {'opportunities': 'None' }

@frappe.whitelist()
def get_quotations_ytd():
    sql_query = """SELECT COUNT(`name`) AS `count`, IFNULL(SUM(`base_grand_total`), 0) AS `sum`
        FROM `tabQuotation` 
        WHERE `docstatus` = 1 AND `transaction_date` >= '{0}-01-01' AND `transaction_date` <= '{1}'""".format(
        datetime.now().year, 
        datetime.now().date())
    print(sql_query)
    quotations = frappe.db.sql(sql_query, as_dict=True)
    if quotations:
        return {'quotations': quotations[0] }
    else:
        return {'quotations': 'None' }

@frappe.whitelist()
def get_sales_orders_ytd():
    sql_query = """SELECT COUNT(`name`) AS `count`, IFNULL(SUM(`base_grand_total`), 0) AS `sum`
        FROM `tabSales Order` 
        WHERE `docstatus` = 1 AND `transaction_date` >= '{0}-01-01' AND `transaction_date` <= '{1}'""".format(
        datetime.now().year, 
        datetime.now().date())
    print(sql_query)
    orders = frappe.db.sql(sql_query, as_dict=True)
    if orders:
        return {'orders': orders[0] }
    else:
        return {'orders': 'None' }
        
@frappe.whitelist()
def get_sales_invoices_ytd():
    sql_query = """SELECT COUNT(`name`) AS `count`, IFNULL(SUM(`base_grand_total`), 0) AS `sum`
        FROM `tabSales Invoice` 
        WHERE `docstatus` = 1 AND `posting_date` >= '{0}-01-01' AND `posting_date` <= '{1}'""".format(
        datetime.now().year, 
        datetime.now().date())
    print(sql_query)
    invoices = frappe.db.sql(sql_query, as_dict=True)
    if invoices:
        return {'invoices': invoices[0] }
    else:
        return {'invoices': 'None' }

@frappe.whitelist()
def get_quotations_py():
    sql_query = """SELECT COUNT(`name`) AS `count`, IFNULL(SUM(`base_grand_total`), 0) AS `sum`
        FROM `tabQuotation` 
        WHERE `docstatus` = 1 AND `transaction_date` >= '{0}-01-01' AND `transaction_date` <= '{0}-{1}-{2}'""".format(
        (datetime.now().year - 1),
        datetime.now().month, datetime.now().day)
    print(sql_query)
    quotations = frappe.db.sql(sql_query, as_dict=True)
    if quotations:
        return {'quotations': quotations[0] }
    else:
        return {'quotations': 'None' }

@frappe.whitelist()
def get_sales_orders_py():
    sql_query = """SELECT COUNT(`name`) AS `count`, IFNULL(SUM(`base_grand_total`), 0) AS `sum`
        FROM `tabSales Order` 
        WHERE `docstatus` = 1 AND `transaction_date` >= '{0}-01-01' AND `transaction_date` <= '{0}-{1}-{2}'""".format(
        (datetime.now().year - 1),
        datetime.now().month, datetime.now().day)
    print(sql_query)
    orders = frappe.db.sql(sql_query, as_dict=True)
    if orders:
        return {'orders': orders[0] }
    else:
        return {'orders': 'None' }
        
@frappe.whitelist()
def get_sales_invoices_py():
    sql_query = """SELECT COUNT(`name`) AS `count`, IFNULL(SUM(`base_grand_total`), 0) AS `sum`
        FROM `tabSales Invoice` 
        WHERE `docstatus` = 1 AND `posting_date` >= '{0}-01-01' AND `posting_date` <= '{0}-{1}-{2}'""".format(
        (datetime.now().year - 1),
        datetime.now().month, datetime.now().day)
    print(sql_query)
    invoices = frappe.db.sql(sql_query, as_dict=True)
    if invoices:
        return {'invoices': invoices[0] }
    else:
        return {'invoices': 'None' }
