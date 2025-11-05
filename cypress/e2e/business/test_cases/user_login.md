## TC001 - Valid User Login

**Objective:** Verify that an existing user can successfully log in.

**Steps**
1. Navigate to the homepage
2. Click "Sign in"
3. Enter a valid email and password
4. Click "Sign in"

**Expected Result:**
- Login is successful
- Homepage is 

---

## TC002 - Invalid User Login

**Objective:** Verify that an existing user can't successfully log in using invalid data.

**Steps**
1. Navigate to the homepage
2. Click "Sign in"
3. Enter an invalid email or/and password
4. Click "Sign in"

**Expected Result:**
- A warning message "Please fill out this field." appears
- User is not logged in
- The log in form is visible

---

## TC003 - Password recovery

**Objective:** Verify that an existing user can recovery password.

**Steps**
1. Navigate to the homepage
2. Click "Sign in"
3. Click "Forgot your password?"
4. Enter valid email
5. Click "Send reset link"
6. Check your inbox and click the reset link
7. Enter new valid password
8. Click "Change password"
9. Log in using new password

**Expected Result:**
- A confirmation message "Reset link sent to your email address"
- Message with reset link visible in inbox
- User can log in using new password