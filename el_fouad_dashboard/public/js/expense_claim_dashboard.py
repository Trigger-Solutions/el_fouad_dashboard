
from __future__ import unicode_literals

from frappe import _


def get_data(data):
	return {
        'fieldname': 'reference_name',
		'internal_links': {
			'Employee Advance': ['advances', 'employee_advance'],
			'Vehicle Log': 'vehicle_log'
		},
		'transactions': [
			{
				'label': _('Payment'),
				'items': ['Payment Entry', 'Journal Entry']
			},
			{
				'label': _('Reference'),
				'items': ['Employee Advance','Vehicle Log']
			},
		]
	}
