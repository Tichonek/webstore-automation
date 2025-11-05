## TC001 - Valid User Registration

**Objective:** Verify that a new user can successfully register.

**Steps**
1. Navigate to the homepage
2. Click "Sign in"
3. Click "No account? Create one here"
4. Fill in the registration form with valid data
5. Click "Save"

**Expected Result:**
- The account is created successfully
- The user is automatically logged in

---

## TC002 - Invalid User Registration

**Objective:** Verify that a new user can't successfully register using invalid data.

**Steps**
1. Navigate to the homepage
2. Click "Sign in"
3. Click "No account? Create one here"
4. Fill in the registration form with one or more invalid data
5. Click "Save"

**Expected Result:**
- A warning message "Please fill out this field." appears
- The account is not created
- The registartion form is visible