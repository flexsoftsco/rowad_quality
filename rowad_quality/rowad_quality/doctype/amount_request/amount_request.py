# -*- coding: utf-8 -*-
# Copyright (c) 2022, GreyCube Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AmountRequest(Document):
	def validate(self):
		total_amount=0
		for amount_request in self.amount_request_detail:
			total_amount+=amount_request.amount
		self.total_amount=total_amount
