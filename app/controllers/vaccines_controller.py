from flask import request, current_app, jsonify
from app.models.vaccine_cards_model import VaccineCardModel
from http import HTTPStatus
from datetime import datetime, timedelta
from app.exc.wrong_key_received import WrongKeyReceived
from sqlalchemy.exc import IntegrityError, DataError
from app.services.quantity_keys import quantity_keys

keys_names = ["cpf", "name", "vaccine_name", "health_unit_name"]

def create_vaccine_card():
    data = request.get_json()

    data = quantity_keys(data, keys_names)
    try:
        for key in keys_names:
            if type(data[key]) != str:
                return jsonify({"message": "Os valores devem ser passados em string"}), HTTPStatus.BAD_REQUEST

        new_vaccine = VaccineCardModel(**data)
        
        if new_vaccine.cpf.isdigit() == False:
            return jsonify({"message": "Passar apenas valores numéricos no CPF!"}), HTTPStatus.BAD_REQUEST
        if len(new_vaccine.cpf) != 11:
            return jsonify({"message": "O CPF deve conter 11 digitos!"}), HTTPStatus.BAD_REQUEST

        new_vaccine.cpf = new_vaccine.cpf
        new_vaccine.name = new_vaccine.name.title()
        new_vaccine.vaccine_name = new_vaccine.vaccine_name.title()
        new_vaccine.health_unit_name = new_vaccine.health_unit_name.title()
        new_vaccine.first_shot_date = datetime.utcnow()
        new_vaccine.second_shot_date = datetime.utcnow() + timedelta(days=90)
        
        current_app.db.session.add(new_vaccine)
        current_app.db.session.commit()

        return jsonify(new_vaccine), HTTPStatus.CREATED
        
    except (AttributeError, KeyError):
        error = WrongKeyReceived(data)
        return jsonify(error.miss_keys), HTTPStatus.BAD_REQUEST
    except IntegrityError:
        return jsonify({"message": "CPF já cadastrado!"}), HTTPStatus.CONFLICT

def read_vaccine():
    
    vaccines_list = current_app.db.session.query(VaccineCardModel).all()

    return jsonify(vaccines_list), HTTPStatus.OK