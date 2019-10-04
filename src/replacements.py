{
    ".py": {
        "from osv import osv, fields": [regex("^from osv import osv, fields$"), "from odoo import models, fields, api"],
        "from osv import fields, osv": [regex("^from osv import fields, osv$"), "from odoo import models, fields, api"],
        "(osv.osv)": [regex("\(osv\.osv\)"), "(models.Model)"],
        "from osv.orm import except_orm": [regex("^from osv\.orm import except_orm$"), "from odoo.exceptions import except_orm"],
        "from tools import config": [regex("^from tools import config$"), "from odoo.tools import config"],
        "from tools.translate import _": [regex("^from tools\.translate import _$"), "from odoo import _"],
        "import tools": [regex("^import tools$"), "from odoo import tools"],
        "name_get()": [regex("^    def name_get\(self,.*?\):"), "    @api.multi\n    def name_get(self):"],
        "": ["", ""],
    },
    ".xml": {
        "<openerp>": ["<openerp>", "<odoo>"],
        "</openerp>": ["</openerp>", "</odoo>"],
    }
}
