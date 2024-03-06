import time

from behave import given, then, when


@then('User will click search button')
def click_on_search_button(context):
    time.sleep(5)
    context.app.apply_job.click_search_button()


@then("User will find job by name {text}")
def find_job(context, text):
    context.app.apply_job.find_job_by_name(text)


@then("User will enter a new email {email}")
def enter_a_new_email(context, email):
    context.app.apply_job.enter_a_new_email(email)


@then("User will enter a new Phone number {number}")
def enter_phone_number(context, number):
    context.app.apply_job.enter_phone_number(number)
    time.sleep(2)


@then("User will Upload Resume")
def upload_resume(context):
    context.app.apply_job.upload_resume()


@then("User will upload Video Instruction")
def upload_video(context):
    context.app.apply_job.upload_video()


@then("User will Upload a cover Letter")
def upload_cover_letter(context):
    context.app.apply_job.upload_cover_letter()


@then("User will click Submit Application button")
def click_submit_application_button(context):
    context.app.apply_job.click_submit_application_button()


@then("User will select BT Resume")
def select_BT_resume(context):
    context.app.apply_job.select_BT_resume()


@then("User will Click Upload Resume checkbox")
def click_uploaded_resume_checkbox(context):
    context.app.apply_job.click_uploaded_resume_checkbox()


# @then("User will select Uploaded Resume {text}")
# def select_uploaded_resume(context, text):
#     context.app.apply_job.select_uploaded_resume(text)

# @then("User will select Uploaded Resume")
# def select_uploaded_resume(context):
#     context.app.apply_job.select_uploaded_resume()


@then("User will select file {text}")
def select_uploaded_resume(context, text):
    context.app.apply_job.select_uploaded_resume(text)


@then("User will click cover letter checkbox")
def click_cover_letter_checkbox(context):
    context.app.apply_job.click_cover_letter_checkbox()


@then("user will select cover letter")
def select_cover_letter(context):
    context.app.apply_job.select_cover_letter()


@then("User will click Video Introduction checkbox")
def click_video_introduction_checkbox(context):
    context.app.apply_job.click_video_introduction_checkbox()


@then("User will select Video Introduction")
def select_video_introduction(context):
    context.app.apply_job.select_video_introduction()


@then("User will see an error message {text}")
def check_error_message(context, text):
    context.app.apply_job.check_error_message(context, text)


@then("User will be navigates to the congratulations page")
def verify_congratulations_message(context):
    context.app.apply_job.verify_congratulations_message(context)