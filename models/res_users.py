import requests
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ResUsers(models.Model):
    _inherit = "res.users"

    api_key = fields.Char(string='API Key', help="API key from OpenWeatherMap")
    location_set = fields.Selection(
        selection=[('auto', 'Use Browser Location'), ('manual', 'Manual Location')],
        string="Set Location",
        default='auto',
        help="Setting and managing locations"
    )
    city = fields.Char(string='City', help="City of the user")

    @api.constrains('city', 'api_key', 'location_set')
    def _check_city(self):
        """Validate the city if manual location is selected and API key is provided."""
        for rec in self:
            if rec.location_set == 'manual' and rec.city and rec.api_key:
                try:
                    url = f'https://api.openweathermap.org/data/2.5/weather?q={rec.city}&appid={rec.api_key}'
                    response = requests.get(url, timeout=10)
                    city_check = response.json()
                    if city_check.get('cod') != 200:
                        raise ValidationError(_(city_check.get('message', 'Invalid city or API key.')))
                except Exception as e:
                    raise ValidationError(_(f'Error validating city: {str(e)}'))