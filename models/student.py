from odoo import api, fields, models

class MyModelName(models.Model):
    _name = "school.student"
    _description = "My Model Names"

    name = fields.Char(string="Name", required=True)
    age = fields.Char(string="Age", required=True)
    dob = fields.Char(string="Date of Birth", required=True)
    address = fields.Char(string="Address", required=True)
    fa_name = fields.Char(string="Father Name", required=True)
    ma_name = fields.Char(string="Mother Name", required=True)
    photo = fields.Char(string="Photo", required=True)

    # application_ids = fields.One2many(inverse_name='student_id',
    #                                   comodel_name='school.application',)

    # application_ids = fields.Many2one(comodel_name='school.application', )

    application_ids = fields.Many2many(comodel_name='school.application', )

