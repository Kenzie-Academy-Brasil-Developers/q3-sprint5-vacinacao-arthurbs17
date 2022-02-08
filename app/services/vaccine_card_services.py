from datetime import datetime, timedelta

def vaccine_card_treatment_string(data: dict):
    data.cpf = data.cpf
    data.name = data.name.title()
    data.vaccine_name = data.vaccine_name.title()
    data.health_unit_name = data.health_unit_name.title()
    data.first_shot_date = datetime.utcnow()
    data.second_shot_date = datetime.utcnow() + timedelta(days=90)