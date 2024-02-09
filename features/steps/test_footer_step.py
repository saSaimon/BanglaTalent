from behave import given, then, when


# @given('FooterLogo is present')
# def FooterLogo_should_present(context):
#     context.app.footer_page.FooterLogo_present()

@given('Verify Company is present')
def Verify_company_present(context):
    context.app.footer_page.Company_present(context)


# @then('Verify Contact is present')
# def contact_should_present(context):
#     context.app.footer_page.contact(context)
#
#
@then('Verify Legal is present')
def Verify_legal_present(context):
    context.app.footer_page.Legal_present(context)


#
#
# @then('Verify About Us is present')
# def AboutUs(context):
#     context.app.footer_page.AboutUs(context)
@then("Verify ContactHeading is present")
def verify_ContactHeading_present(context):
    context.app.footer_page.ContactHeading_present(context)


# @then("Verify Legal is present")
# def verify_Legal_present(context):
#     context.app.footer_page.Legal_present(context)
@then("Click on AboutUs link")
def click_on_about_us(context):
    context.app.footer_page.Click_AboutUs()


@then("Click on Jobs link")
def click_on_jobs(context):
    context.app.footer_page.Click_Jobs()


@then("Click on Help link")
def click_on_help(context):
    context.app.footer_page.Click_Help()


@then("Click on Contact link")
def click_on_contact(context):
    context.app.footer_page.Click_contact()


@then("Click on FAQ link")
def click_on_FAQ(context):
    context.app.footer_page.Click_FAQ()


@then("Click on Privacy link")
def click_on_Privacy(context):
   context.app.footer_page.Click_Privacy()


@then("Click on Disclaimer link")
def click_on_disclaimer(context):
    context.app.footer_page.Click_Disclaimer()


@then("Click on GDPR link")
def click_on_GDPR(context):
    context.app.footer_page.Click_GDPR()
