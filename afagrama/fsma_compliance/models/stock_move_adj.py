from odoo import models, fields, api, _

# ______________Umar Aziz__________________________


class StockMoveAdj(models.Model):
    _inherit = "stock.move"

    def picking_put_in_pack(self):
        if self.picking_id:
            self.picking_id.put_in_pack()
            if self.picking_id.picking_type_id.show_reserved:
                view = self.env.ref('stock.view_stock_move_operations')
            else:
                view = self.env.ref('stock.view_stock_move_nosuggest_operations')

            return {
                'name': _('Detailed Operations'),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'stock.move',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'res_id': self.id,
                'context': dict(
                    self.env.context,
                    show_lots_m2o=self.has_tracking != 'none' and (
                    self.picking_type_id.use_existing_lots or self.state == 'done' or self.origin_returned_move_id.id),
                    # able to create lots, whatever the value of ` use_create_lots`.
                    show_lots_text=self.has_tracking != 'none' and self.picking_type_id.use_create_lots and not self.picking_type_id.use_existing_lots and self.state != 'done' and not self.origin_returned_move_id.id,
                    show_source_location=self.location_id.child_ids,
                    show_destination_location=self.location_dest_id.child_ids,
                    show_package=not self.location_id.usage == 'supplier',
                    show_reserved_quantity=self.state != 'done'
                ),
            }