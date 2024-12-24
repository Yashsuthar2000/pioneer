/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, onWillStart } from "@odoo/owl";
import { onMounted } from "@odoo/owl";
import { user } from "@web/core/user";
export class DeliveryDashboard extends Component {
    static template = "DeliveryDashboardMain";
    static props = ["*"];

    setup() {
        this.orm = useService("orm");
        this.grid_data = [];
        this.delivery_order_data = [];

        onWillStart (async () => {
            const data = await this.orm.call('pioneer.delivery.dashboard', 'get_dashboard_data', []);
            this.grid_data = data.grid_data;
            this.delivery_order_data = data.delivery_order_data;
            console.log("this.grid_data:::::::::::::::::::::::", this.grid_data)
            console.log("this.delivery_order_data:::::::::::::::::::::::", this.delivery_order_data)
        });
    }
}

registry.category("actions").add("delivery_dashboard", DeliveryDashboard);

