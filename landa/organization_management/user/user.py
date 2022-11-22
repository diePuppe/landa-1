from frappe.permissions import add_user_permission

from landa.overrides import get_default_company
from landa.organization_management.doctype.member_function.member_function import apply_active_member_functions


def on_update(doc, event=None):
	if (not doc.enabled) or (doc.name in ("Administrator", "Guest")):
		return

	if doc.organization and doc.has_value_changed("organization"):
		add_user_permission("Organization", doc.organization, doc.name, ignore_permissions=True)
		add_user_permission("Company", get_default_company(doc.organization), doc.name, ignore_permissions=True)

	if doc.landa_member and doc.has_value_changed("landa_member"):
		# Restrict LANDA Member to itself and it's Organization
		add_user_permission("LANDA Member", doc.landa_member, doc.name, ignore_permissions=True)
		apply_active_member_functions({"member": doc.landa_member})
