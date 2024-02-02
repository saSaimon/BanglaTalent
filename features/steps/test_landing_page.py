import time

from behave import given, then


@given('Logo is present')
def logo_should_present(context):
    context.app.landing_page.logo_present()


@then('Verify Find a job is present')
def find_a_job_upper(context):
    context.app.landing_page.find_a_job_upper(context)


@then('Verify Post a job is present')
def post_a_job_upper(context):
    context.app.landing_page.post_a_job_upper(context)


@then('Verify About us job present')
def about_us(context):
    context.app.landing_page.about_us(context)


@then('Verify Find a job is present in lower')
def find_a_job_lower(context):
    context.app.landing_page.find_a_job_lower(context)


@then('Verify Post a job lower present')
def post_a_job_lower(context):
    context.app.landing_page.post_a_job_lower(context)


@then('Verify Search Bar is present')
def search_bar_present(context):
    context.app.landing_page.search_bar_is_present()


@then('Verify Job Carts are present')
def job_carts_present(context):
    context.app.landing_page.job_carts_are_present(context)


@then('Verify Top pick Carts are present')
def top_pick_carts(context):
    context.app.landing_page.top_pic_carts_are_present(context)


@then('Verify Success Stories slides are present')
def success_stories(context):
    context.app.landing_page.success_story_slides_are_present(context)
