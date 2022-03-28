from __future__ import unicode_literals
from frappe import _


def get_data():
    config = [
        {'label': _('Rowad Quality'), 
        'items': [
                {
                    "type": "doctype",
                    "name": "SOP",
                    "label": _("SOP")
                },
                {
                    "type": "doctype",
                    "name": "Leave Application",
                    "label": _("Leave Application")
                }     
            ]
        },
        {'label': _('Transaction'), 
        'items': [
                {
                    "type": "doctype",
                    "name": "Material Request",
                    "label": _("Material Request")
                },
                {
                    "type": "doctype",
                    "name": "Payment Request",
                    "label": _("Payment Request")
                } ,
                {
                    "type": "doctype",
                    "name": "Amount Request",
                    "label": _("Amount Request")
                } ,
                {
                    "type": "doctype",
                    "name": "Quality Issues Request",
                    "label": _("Quality Issues Request")
                }, 
                {
                    "type": "doctype",
                    "name": "Change Control Request",
                    "label": _("Change Control Request")
                }                                             
                               
            ]
        }        
    ]
    return config    