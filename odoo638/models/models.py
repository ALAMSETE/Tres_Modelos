# -*- coding: utf-8 -*-

from odoo import models, fields, api

class camiones638(models.Model):
	_name = 'odoo638.camiones638'
	_description = 'model camiones638'

	name = fields.Char('Matricula',required=True)
	marca = fields.Char(string='Marca',required=True)
	modelo = fields.Char(string='Modelo',required=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class coches638(models.Model):
	_name = 'odoo638.coches638'
	_description = 'model coches638'

	name = fields.Char('Matricula',required=True)
	marca = fields.Char(string='Marca',required=True)
	modelo = fields.Char(string='Modelo',required=True)

class tractores638(models.Model):
	_name = 'odoo638.tractores638'
	_description = 'model tractores638'

	name = fields.Char('Matricula',required=True)
	marca = fields.Char(string='Marca',required=True)
	modelo = fields.Char(string='Modelo',required=True)
