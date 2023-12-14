# -*- coding: utf-8 -*-

from odoo import models, fields, api


class proyecto_odoo_empresa(models.Model):
    _name = 'proyecto_odoo_empresa.empresas_contratadoras'
    _description = 'proyecto_odoo_empresa.empresas_contratadoras'
    name = fields.Integer(string="Codigo del contrato", required=True)
    empresa = fields.Char(string="Nombre de la empresa")
    pago = fields.Integer(string="Pago por hora")
    horas = fields.Integer(string="Número de horas")
    pago_total = fields.Integer(string="Total",compute="_pago_total",store=True)
    description = fields.Text()
    tipo_pago = fields.Many2many("project.tags", string="Tipo de pago")
    proyecto = fields.Many2many("project.project", "proyecto_empresa_rel", "empresa_id", "proyecto_id", string="Proyectos")
    
    @api.depends('pago','horas')
    def _pago_total(self):
        for r in self:
            if r.pago > 0:
                r.pago_total = r.pago * r.horas
    
class proyecto_odoo_proyecto(models.Model):
    _inherit = 'project.project'
    
    empresa_contratadora_id = fields.Many2many('proyecto_odoo_empresa.empresas_contratadoras', 'proyecto_empresa_rel', 'proyecto_id', 'empresa_id', string = 'Empresa contratadora')
    tasks_ids = fields.One2many('project.task', 'project_id', string = 'Tareas')

    
