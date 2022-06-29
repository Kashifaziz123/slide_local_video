# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class slide_local_video(models.Model):
#     _name = 'slide_local_video.slide_local_video'
#     _description = 'slide_local_video.slide_local_video'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
