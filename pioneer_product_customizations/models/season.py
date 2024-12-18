from odoo import models, fields


class SeasonMaster(models.Model):
    _name = 'season.master'
    _description = 'Season Master'

    name = fields.Char(string='Season Name', required=True, help="Name of the season, e.g., WINTER 2024")
    code = fields.Char(string='Season Code', required=True, help="Unique code for the season, e.g., WIN")
