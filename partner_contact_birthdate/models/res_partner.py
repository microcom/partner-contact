# -*- coding: utf-8 -*-
# Copyright (C) 2014-2015  Grupo ESOC <www.grupoesoc.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models
import logging


_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    """Partner with birth date in date format."""
    _inherit = "res.partner"

    # New birthdate field in date format
    birthdate_date = fields.Date("Birthdate")
