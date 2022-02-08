from flask import request, current_app, jsonify
from app.models.vaccine_cards_model import VaccineCardModel
from http import HTTPStatus
from datetime import datetime, timedelta

def create_vaccine_card():
    data = request.get_json()

    try:
        new_vaccine = VaccineCardModel(**data)
        
        if new_vaccine.cpf.isdigit() == False:
            return jsonify({"message": "Passar apenas valores numéricos!"}), HTTPStatus.BAD_REQUEST

        values = [value for value in data.values()]
        for value in values:
            if type(value) in values != str:
                return jsonify({"message": "Os valores devem ser passados em string"}), HTTPStatus.BAD_REQUEST

        new_vaccine.cpf = new_vaccine.cpf
        new_vaccine.name = new_vaccine.name.title()
        new_vaccine.vaccine_name = new_vaccine.vaccine_name.title()
        new_vaccine.health_unit_name = new_vaccine.health_unit_name.title()
        new_vaccine.first_shot_date = datetime.utcnow()
        new_vaccine.second_shot_date = datetime.utcnow() + timedelta(days=90)
        
        current_app.db.session.add(new_vaccine)
        current_app.db.session.commit()

        return jsonify(new_vaccine), HTTPStatus.CREATED
        
    except KeyError:
        return {"message": "Chave errada!"}