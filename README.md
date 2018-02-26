# ShiptInterviewAssesment

Test 1. test_click_on_signup_button_valid_credntials
Steps: Go to www.shipt.com , click on “SignUp” button and enter valid “email-id” and “zipcode”, click Go
Expected: Validate after click "Go" button it should navigate to next page 

Test 2. test_click_on_signup_button_invalid_zipcode
Steps: Go to www.shipt.com , click on “SignUp” button and enter valid “email-id” and invalid “zipcode” with different lengths, click Go
Expected: Validate message "Please enter valid ZipCOde"

Test 3. test_click_on_signup_button_registered_emailid
Steps: Go to www.shipt.com , click on “SignUp” button and enter already registered “email-id” and valid “zipcode” and click Go
Expected: Validate message "We noticed there is an account with that email. Please Login."
