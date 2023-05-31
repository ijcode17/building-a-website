from odoo import fields, models


class Teachers(models.Model):
    _name = "academy.teachers"
    _description = "Academy Teachers"

    name = fields.Char()
