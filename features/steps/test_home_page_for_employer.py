import time

from behave import given, then, when


@then('Verify the present of Post A Job button')
def verify_post_a_job_present(context):
    context.app.employer_home_page.verify_post_a_job_button_present(context)


@then("Click on the Post A Job button")
def click_post_a_job_button(context):
    context.app.employer_home_page.click_post_a_job_button()


@then("Verify the present of search icon")
def verify_search_icon_present(context):
    context.app.employer_home_page.verify_search_icon_present()


@then("Click on the search icon")
def click_search_icon(context):
    context.app.employer_home_page.click_search_icon()


@then("Verify the present of messenger icon")
def verify_messenger_icon_present(context):
    context.app.employer_home_page.verify_messenger_icon_present()


@then("click on the messenger icon")
def click_messenger_icon(context):
    context.app.employer_home_page.click_messenger_icon()


@then("Verify the present of calender icon")
def verify_schedule_icon_present(context):
    context.app.employer_home_page.verify_schedule_icon_present()


@then("Click on the Calender icon")
def click_schedule_icon(context):
    context.app.employer_home_page.click_schedule_icon()


@then("Verify the present of Notification icon")
def verify_notification_icon_present(context):
    context.app.employer_home_page.verify_notification_icon_present()


@then("Verify the present of setting icon")
def verify_setting_icon_present(context):
    context.app.employer_home_page.verify_setting_icon_present()


@then("Click on the setting icon")
def click_setting_icon(context):
    context.app.employer_home_page.click_setting_icon()


@then("Back to the home Page")
def back_to_home_page(context):
    context.app.employer_home_page.back_to_home_page()


@then("Verify Search Candidate Here element is present")
def verify_search_candidates_here_text(context):
    context.app.employer_home_page.verify_search_candidates_here_text(context)


@then('Verify Job Listing element is present')
def job_listing_present(context):
    context.app.employer_home_page.verify_job_listing_present(context)


@then("Verify View All link for job listing is present")
def verify_view_all_for_job_text_present(context):
    context.app.employer_home_page.verify_view_all_for_job_text_present(context)


@then("click on View link For job listing")
def click_view_all_for_job(context):
    context.app.employer_home_page.click_view_all_for_job()


@then("Verify Inbox text is present")
def verify_inbox_text(context):
    context.app.employer_home_page.verify_inbox_text(context)


@then("Verify View all link for inbox is present")
def verify_view_all_for_messenger_present(context):
    context.app.employer_home_page.verify_view_all_for_messenger_present(context)


@then("Click on the View All link for inbox")
def click_view_all_for_messenger(context):
    context.app.employer_home_page.click_view_all_for_messenger()


@then("Verify Calender text is present")
def verify_calender_text_present(context):
    context.app.employer_home_page.verify_calender_text_present(context)



