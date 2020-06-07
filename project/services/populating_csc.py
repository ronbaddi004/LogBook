import json
import os

from django.db.utils import IntegrityError

from services.models import BaseCountry, BaseState, BaseCity


cur_path = os.path.dirname(__file__)

new_path_country = '/assets/countries.json'

new_path_state = '/assets/states.json'

new_path_city = '/assets/cities.json'


def populating_countries():
    """Populating Countries"""
    data = None

    with open(cur_path + new_path_country) as file:

        data = json.load(file)

    country_list = []

    if BaseCountry.objects.all().count() == 0:

        for country_data in data:

            country_list.append(BaseCountry(id=country_data['id'], phone_code=country_data['phonecode'], name=country_data['name']))

    BaseCountry.objects.bulk_create(country_list)


def populating_states():
    """Population States"""
    data = None

    with open(cur_path + new_path_state) as f:

        data = json.load(f)

    try:

        state_list = []

        if BaseState.objects.all().count() == 0:

            for state_data in data:

                state_list.append(BaseState(id=state_data['id'], my_country_id=state_data['country_id'], name=state_data['name']))

        BaseState.objects.bulk_create(state_list)

    except IntegrityError as exc:

        BaseState.objects.all().delete()


def populating_cities():
    """Population Cities"""
    data = None

    with open(cur_path + new_path_city) as f:

        data = json.load(f)

    try:

        # city_list = []

        if BaseCity.objects.all().count() == 0:

            for city_data in data:

                print(city_data['id'])

                # city_list.append(BaseCity(id=city_data['id'], my_state_id=city_data['state_id'], name=city_data['name']))

                BaseCity.objects.create(id=city_data['id'], my_state_id=city_data['state_id'], name=city_data['name'])

        # BaseCity.objects.bulk_create(city_list)

    except IntegrityError as exc:

        import pdb; pdb.set_trace()

        BaseCity.objects.all().delete()
