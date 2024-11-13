'''
clean and prepare user information for use in the application
functions:
    sanitize_name(name) - remove any non-alphabetic characters from the name
    generate_upn(first_name, last_name, role) - generate a UPN based on the first name, last name, and role

'''

import re

"""
This Module handles the group data for different departments and roles.

Functions:
    - get_groups: takes role and department and returns the groups, shared mailboxes, and distribution groups for that role and department.

"""

dept_based_groups = {
    "Events Team": {
        "Staff": {
            "groups": ["Events", "SWX_events"],
            "shared_mailboxes": ["events@sofwerx.org", "swx_scheduler@sofwerx.org"]
        },
        "Intern": {
            "groups": ["Events_Intern", "SWX_Events"],
            "shared_mailboxes": []
        }
    },
    "Foundry": {
        "Staff": {
            "groups": ["Foundry", "SWX_Foundry"],
            "shared_mailboxes": ["foundry@sofwerx.org"]
        },
        "Intern": {
            "groups": ["Foundry_Interns", "SWX_Foundry"],
            "shared_mailboxes": []
        }
    },
    "Head Shed": {
        "Staff": {
            "groups": ["CFO-CLO", "Headshed", "Leadership", "SWX_BusinessAdmins", "SWX_PMs"],
            "shared_mailboxes": ["leadership@sofwerx.org"]
        }
    },
    "Marketing": {
        "Staff": {
            "groups": ["Marketing", "SWX_Marketing", "SWX_Media"],
            "shared_mailboxes": ["marketing@sofwerx.org"]
        },
        "Intern": {
            "groups": ["Marketing_Interns", "SWX_Marketing", "SWX_Media"],
            "shared_mailboxes": []
        }
    },
    "Market Research": {
        "Staff": {
            "groups": ["SWX_MR", "SWX_PMs", "T2-STEMAdmin", "SWX_T2-STEMAdmin"],
            "shared_mailboxes": ["t2.stem_admin@sofwerx.org"]
        },
        "Intern": {
            "groups": ["SWX_MR", "MarketResearch_Interns"],
            "shared_mailboxes": []
        }
    },
    "Nerd Herd": {
        "Staff": {
            "groups": ["NerdHerd", "SWX_NerdHerd"],
            "shared_mailboxes": ["nerdherd@sofwerx.org", "sysadmin@sofwerx.org"]
        },
        "Intern": {
            "groups": ["NerdHerd_Interns", "SWX_NerdHerd"],
            "shared_mailboxes": []
        }
    },
    "Business Admins": {
        "Staff": {
            "groups": ["BusinessAdmins", "SWX_BusinessAdmins", "SWX_PMs"],
            "shared_mailboxes": ["billing@sofwerx.org", "businessadmin@sofwerx.org"]
        },
        "Intern": {
            "groups": ["BusinessAdmin_Interns", "SWX_BusinessAdmins", "CFO-CLO"],
            "shared_mailboxes": []
        }
    },
    "Project Managers": {
        "Staff": {
            "groups": ["PMs", "SWX_PMs"],
            "shared_mailboxes": ["swx_pm@sofwerx.org"]
        },
        "Intern": {
            "groups": ["PMs_Interns"],
            "shared_mailboxes": []
        }
    }
}

role_based_groups = {
    "Staff":{
            "groups": ["Staff", "SWX_Staff"],
            "distribution_groups": ["SOFWERX_STAFF_ONLY"]
        },
    "Intern":{
            "groups": ["Interns","SWX_Interns"],
            "distribution_groups": [],
        },
    "usf":{
            "groups": ["Student Hiring", "SWX_Interns"],
            "distribution_groups": [],
        },
    "OtherUsers":{
            "groups": ["OtherUsers"],
            "distribution_groups": [],
        }
}

def get_groups(department, role):
    """
    Returns the groups, shared mailboxes, distribution groups, and calendar access for a given department and role.

    Args:
        department (str): The department of the user.
        role (str): The role of the user.

    Returns:
        dict: A dictionary containing the groups, shared mailboxes, distribution groups, and calendar access for the given department and role.
    """
    groups = set()
    shared_mailboxes = set()
    distribution_groups = set()
    calendar_access = "Reviewer"  # Default to None if no access required

    # Normalize role to lowercase for case-insensitive comparison

    # Add department-based groups and shared mailboxes
    if department in dept_based_groups:
        if role in dept_based_groups[department]:
            groups.update(dept_based_groups[department][role].get("groups", []))
            shared_mailboxes.update(dept_based_groups[department][role].get("shared_mailboxes", []))
    
    # Add role-based groups and distribution groups
    if role in role_based_groups:
        groups.update(role_based_groups[role].get("groups", []))
        distribution_groups.update(role_based_groups[role].get("distribution_groups", []))
        
        # Set calendar access based on role
        if role == "Staff":
            calendar_access = "Editor"

    # Add common groups (SWX_Trainual)
    groups.add("SWX_Trainual")
    # Add common distribution group (SWX_All)
    distribution_groups.add("SWX_All")

    # Convert sets to lists for easier use and return
    return {
        "groups": list(groups),
        "shared_mailboxes": list(shared_mailboxes),
        "distribution_groups": list(distribution_groups),
        "calendar_access": calendar_access  # None if no calendar access required
    }

def generate_upn(first_name, last_name, role):
    # Replace spaces and hyphens with dots, remove other non-alphabetic characters, and lowercase
    clean_fname = re.sub(r'[^a-zA-Z.]', '', first_name.strip().replace(" ", ".").replace("-", ".")).lower()
    clean_lname = re.sub(r'[^a-zA-Z.]', '', last_name.strip().replace(" ", ".").replace("-", ".")).lower()
    
    # Define role-specific extensions
    role_extensions = {
        "staff": "",       # No extension for staff
        "intern": ".intern",
        "volunteer": ".vol",
        "contractor": ".ctr",
        "ewi": ".ewi",
        "usf": ".usf"
    }
    
    # Get the appropriate extension or default to ".role" if not found
    role_extension = role_extensions.get(role.lower(), f".{role.lower()}")

    # Generate the UPN based on role
    return f"{clean_fname}.{clean_lname}{role_extension}@sofwerx.org"