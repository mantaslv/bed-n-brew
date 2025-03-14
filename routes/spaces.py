from lib.database_connection import get_flask_database_connection
from flask_login import login_required, current_user
from flask import render_template, Blueprint, redirect, request
from lib.spaces.space_repo import SpaceRepo
from forms.space_form import SpaceForm
from lib.spaces.space import Space

spaces = Blueprint('spaces', __name__)

@spaces.route("/", methods=["GET"])
def get_spaces():
    connection = get_flask_database_connection()
    spaces_repo = SpaceRepo(connection)
    spaces = spaces_repo.all()
    return render_template("spaces/list_of_spaces.html", spaces=spaces)

@spaces.route("/<id>", methods=["GET"])
def get_single_space(id):
    connection = get_flask_database_connection()
    space_repo = SpaceRepo(connection)
    space, host = space_repo.find_by_id(id)
    return render_template("spaces/single_space.html", space=space, host=host)

@spaces.route("/new", methods=["GET", "POST"])
@login_required
def create_space():
    connection = get_flask_database_connection()
    spaces_repo = SpaceRepo(connection)
    form = SpaceForm()
    if form.validate_on_submit():
        new_space = Space(
            None,
            form.property_name.data,
            form.location.data,
            form.beds.data,
            form.property_type.data,
            float(form.price_per_night.data),
            form.description.data,
            form.image_url.data,
            form.rating.data,
            form.availability.data,
            None,
            current_user.id,
        )
        spaces_repo.create(new_space)
        return redirect("/")
    return render_template("spaces/new_space.html", form=form)

@spaces.route('/spaces/search')
def search_spaces():
    connection = get_flask_database_connection(app)
    location = request.args.get('location', '')
    property_type = request.args.get('property_type', '')

    query = "SELECT * FROM spaces WHERE True"
    params = []
    
    if location:
        query += " AND location ILIKE %s"
        params.append(f"%{location}%")
    
    if property_type:
        query += " AND property_type = %s"
        params.append(property_type)
    spaces = connection.execute(query, params)
    return render_template('spaces/list_of_spaces.html', spaces=spaces)