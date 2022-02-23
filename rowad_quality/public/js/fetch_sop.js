cur_frm.cscript.sop_cf = function(doc) {
    if(doc.sop_cf) {
        frappe.db.get_value('SOP', doc.sop_cf, 'description')
        .then(r => {
            if (r.message.description) {
                cur_frm.set_value('sop_description_cf', r.message.description)
            }
        })
    };
}