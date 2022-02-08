from flask import Blueprint

from app.controllers import vaccines_controller

bp_vaccines = Blueprint("bp_vaccines", __name__, url_prefix="/vaccinations")

bp_vaccines.post("")(vaccines_controller.create_vaccine_card)