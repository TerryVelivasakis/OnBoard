from flask import Blueprint, request, jsonify
from services.user_info import generate_upn, get_groups

user_bp = Blueprint("user", __name__)

@user_bp.route("/create_user_document", methods=["POST"])
def create_user_document():
    data = request.json
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    role = data.get("role")
    department = data.get("department")

    # Generate UPN and get group data
    upn = generate_upn(first_name, last_name, role)
    group_data = get_groups(department, role)

    # Prepare the response JSON object
    user_document = {
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
        "department": department,
        "supervisor": data.get("supervisor"),
        "job_title": data.get("job_title"),
        "start_date": data.get("start_date"),
        "notes": data.get("notes"),
        "upn": upn,
        "groups": group_data.get("groups"),
        "shared_mailboxes": group_data.get("shared_mailboxes"),
        "distribution_groups": group_data.get("distribution_groups"),
        "calendar_access": group_data.get("calendar_access"),
    }

    return jsonify(user_document)
