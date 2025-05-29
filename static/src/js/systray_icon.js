/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import {Dropdown} from '@web/core/dropdown/dropdown';
import {DropdownItem} from '@web/core/dropdown/dropdown_item';

class SystrayIcon extends Component {
   setup() {
       super.setup(...arguments);
       this.action = useService("action");
   }
   _openSaleModel() {
       this.action.doAction({
           type: "ir.actions.act_window",
           name: "Sale Order",
           res_model: "sale.order",
           view_mode: "form",
           views: [[false, "form"]],
           target: "new",
           });
           }
}
   SystrayIcon.template = "systray_icon";
   SystrayIcon.components = {Dropdown, DropdownItem };
   export const systrayItem = { Component: SystrayIcon,};
   registry.category("systray").add("SystrayIcon", systrayItem, { sequence: 1 });
