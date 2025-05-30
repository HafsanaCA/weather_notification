/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";

class WeatherSystray extends Component {
    static template = "weather_systray.weatherSystray";

    setup() {
        this.state = useState({
            city: "",
            main: "",
            description: "",
            temp: "",
            temp_min: "",
            temp_max: "",
            icon: "",
            updated_at: "",
            hasData: false,
        });

        onWillStart(() => this.fetchWeatherData());
    }

    async fetchWeatherData() {
        try {
            const result = await rpc("/weather/notification/check");
            const main = result.main;
            const weather = result.weather[0];

            this.state.city = result.name;
            this.state.main = weather.main;
            this.state.description = weather.description;
            this.state.temp = (main.temp - 273.15).toFixed(1);
            this.state.temp_min = (main.temp_min - 273.15).toFixed(1);
            this.state.temp_max = (main.temp_max - 273.15).toFixed(1);
            this.state.icon = weather.icon;
            this.state.updated_at = new Date(result.dt * 1000).toLocaleString();
            this.state.hasData = true;
        } catch (error) {
            console.error("Error fetching weather data:", error);
            this.state.hasData = false;
        }
    }
}

export const systrayItem = {
    Component: WeatherSystray,
};

registry.category("systray").add("weather_systray.WeatherSystray", systrayItem, { sequence: 1 });
