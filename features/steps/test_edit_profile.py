import time

from behave import given, then, when


@then('User will click Profile icon')
def click_on_profile_icon(context):
    context.app.apply_job.click_on_profile_icon()


@then("User will Navigate to the Profile section")
def click_profile_name(context):
    context.app.apply_job.click_profile_name()


@then("User will click profile edit icon")
def click_edit_profile(context):
    context.app.edit_profile_for_candidate.click_edit_profile()


@then("User will edit FirstName {firstName}")
def edit_first_name(context, firstName):
    context.app.edit_profile_for_candidate.edit_first_name(firstName)


@then("User will edit LastName {lastName}")
def edit_last_name(context, lastName):
    context.app.edit_profile_for_candidate.edit_last_name(lastName)


@then("User will edit Designation {designation}")
def edit_designation(context, designation):
    context.app.edit_profile_for_candidate.edit_designation(designation)


@then("User will edit phone Number {phoneNumber}")
def edit_phone_number(context, phoneNumber):
    context.app.edit_profile_for_candidate.edit_phone_number(phoneNumber)


@then("User will edit country {countryName}")
def edit_country(context, countryName):
    context.app.edit_profile_for_candidate.edit_country(countryName)


@then("User will Edit City {city}")
def edit_city(context, city):
    context.app.edit_profile_for_candidate.edit_city(city)


@then("User will edit Zip code {zipCode}")
def edit_zip_code(context, zipCode):
    context.app.edit_profile_for_candidate.edit_zip_code(zipCode)


@then("User will edit linkedIn link {link}")
def edit_link(context, link):
    context.app.edit_profile_for_candidate.edit_link(link)


@then("User will Change Profile Picture")
def edit_profile_picture(context):
    context.app.edit_profile_for_candidate.edit_profile_picture()


@then("User will Click Save Changes Button")
def click_submit_button(context):
    context.app.edit_profile_for_candidate.click_submit_button()