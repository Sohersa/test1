# -*- coding: utf-8 -*-

from odoo import models,fields,api

class Course(models.Model):
    _name = 'site.course'
    _description = "Cursos en linea"

    name = fields.Char(string="Titulo",required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users',
        ondelete="set null", string="Responsible", index=True)
    session_id = fields.One2many('site.session','course_id', string="Sessions")
class Session(models.Model):
    _name = 'site.session'
    _description = "Site sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('site.course',
        ondelete="cascade", string="Course", required=True)