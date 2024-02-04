import time

from behave import given, then, when


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


@when('User click Find a job first option')
def click_find_a_job_first(context):
    context.app.landing_page.click_find_a_job()


@then('Verify there are available some vacancies')
def verify_vacancies(context):
    context.app.landing_page.check_available_vacancies()


@when('User will input keywords: {text}')
def input_keywords(context, text):
    context.app.landing_page.input_keywords(text)


@when('User will input location: {text}')
def user_input_location(context, text):
    context.app.landing_page.input_location(text)


@when('User will select by location: {text}')
def user_will_select_location(context, text):
    context.app.landing_page.select_location_by_name_matched(text)


@when('User will click search button')
def click_search_button(context):
    context.app.landing_page.click_search()


@then('Verify there are job carts with this search')
def verify_job_carts_present(context):
    context.app.landing_page.verify_job_carts_return(context)


@when('Input Salary range: {text}')
def input_salary_range(context, text):
    context.app.landing_page.input_salary_range(text)


@when('Select job cart by name: {name}')
def select_job_cart(context, name):
    context.app.landing_page.select_job_by_name_matched(name)


@then('Verify Apply Job button is present')
def verify_apply_job_button(context):
    context.app.landing_page.verify_apply_job_button(context)


@when('User will click apply job button')
def click_apply_job_button(context):
    context.app.landing_page.click_apply_job_button()



@when('User will click yes button')
def click_yes_button(context):
    context.app.landing_page.click_yes_button()


@then('Verify pop up sign in window')
def verify_sign_ing_window_pop_up(context):
    context.app.landing_page.verify_sign_in_pop_up(context)


@when('User will click no button')
def click_no_button(context):
    context.app.landing_page.click_no_button()


@then('Verify user returns to apply page')
def verify_return_apply_page(context):
    context.app.landing_page.verify_apply_job_button(context)