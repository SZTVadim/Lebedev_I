from playwright.sync_api import Page, expect
from time import sleep


def test_form_qa_practice(page: Page):
    page.goto("https://www.qa-practice.com/forms/practice-form")
    first_name = page.locator("[placeholder='First Name']")
    first_name.fill("Igor")
    expect(first_name).to_have_value("Igor")

    last_name = page.locator("[placeholder='Last Name']")
    last_name.fill("Lebedev")
    expect(last_name).to_have_value("Lebedev")

    email = page.locator("[placeholder='name@example.com']")
    email.fill("name@example.com")
    expect(email).to_have_value("name@example.com")

    gender = page.locator("#gender_0")
    gender.click()
    expect(gender).to_be_checked()

    mobile = page.locator("[placeholder='Mobile Number']")
    mobile.fill("9993213212")
    expect(mobile).to_have_value("9993213212")

    date_of_birth = page.locator(".border-left-0")
    date_of_birth.click()
    calendar = page.locator(".datepicker.gj-unselectable")
    expect(calendar).to_be_visible()

    choice_date = page.locator("#dateOfBirthInput")
    choice_date.fill("08 Oct 1997")
    expect(choice_date).to_have_value("08 Oct 1997")

    subject = page.locator("[placeholder='Type to search subjects...']")
    subject.fill("Test Test")
    expect(subject).to_have_value("Test Test")

    hobbies = page.locator("#hobbies_0")
    hobbies.click()
    expect(hobbies).to_be_checked()

    current_address = page.locator("#currentAddress")
    current_address.fill("742 Evergreen Terrace Springfield, IL 62704 USA")
    expect(current_address).to_have_value("742 Evergreen Terrace Springfield, IL 62704 USA")

    state = page.locator(".custom-dropdown-control").nth(0)
    state.click()
    choice_state = page.locator("[data-value='NCR']")
    expect(choice_state).to_be_visible()
    choice_state = page.locator("[data-value='NCR']")
    choice_state.click()
    expect(state).to_contain_text("NCR")

    city = page.locator(".custom-dropdown-control").nth(1)
    city.click()
    choice_city = page.locator("[data-value='Noida']")
    expect(choice_city).to_be_visible()
    choice_city.click()
    expect(city).to_contain_text("Noida")

    submit = page.locator("#submit-id-submit")
    submit.click()
    result_popap = page.locator("#resultsModalLabel")
    expect(result_popap).to_be_visible()
    sleep(4)
