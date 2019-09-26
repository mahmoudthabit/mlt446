#from other_code.services import DATA_1_1, DATA_1_2, DATA_1_3
# mlt446

# test 1
DATA_1_1 = {
    "username": "abc123",
    "password": "password",
}

DATA_1_2 = DATA_1_1

DATA_1_3 = {
    "username": "xyz789",
    "password": "password",
}

def username_pass_check(data1, data2):
    if (data1 == data2):
        return 1
    else: 
        return 0



# test 2
DATA_2_1 = {
    "type": "instructor",
}

DATA_2_2 = DATA_2_1

DATA_2_3 = {
    "type": "TA",
}

def user_type_comp(data1, data2):
    if (data1 == data2):
        return 1
    else: 
        return 0


# test 3
SYSTEM_ADMIN_ID_1 = "abc123"
SYSTEM_ADMIN_ID_2 = "xyz123"

def admin_id_check(admin_id):
    if (SYSTEM_ADMIN_ID_1 == admin_id):
        return true
    else: 
        return false
    
# test 4
# i dont know how to use dates as a type in python
DUE_DATE_ASSIGNMENT_1 = "9/1/2019"

def check_due_date():
    return DUE_DATE_ASSIGNMENT_1
    
# test 5 
SID_1 = "abc123"
GRADE_1 = 90
SID_2 = "xyz123"
GRADE_2 = 80

def grad_check(student_id):
    if (SID_1 == student_id):
        return GRADE_1
    elif (SID_2 == student_id):
        return GRADE_2
    else: 
        return 0














# test 1 pass
def test_pass_1():
    """
    this will test if DATA_1_1 is equal to DATA_1_2
    """
    print("\nRunning test_pass_1...")
    assert username_pass_check (DATA_1_1,DATA_1_2) == 1
    
# test 1 fail   
def test_fail_1():
    """
    this will test if DATA_1_1 is equal to DATA_1_3
    """
    print("\nRunning test_fail_1...")
    assert username_pass_check (DATA_1_1,DATA_1_3) == 1
    

# test 2 pass
def test_pass_2():
    """
    this will test if DATA_2_1 is equal to DATA_2_2
    """
    print("\nRunning test_pass_2...")
    assert user_type_comp(DATA_2_1,DATA_2_2) == 1
    
# test 2 fail   
def test_fail_2():
    """
    this will test if DATA_2_1 is equal to DATA_2_3
    """
    print("\nRunning test_fail_2...")
    assert user_type_comp(DATA_2_1,DATA_2_3) == 1
    
    
    
# test 3 pass
def test_pass_3():
    """
    this will test if SYSTEM_ADMIN_ID_1 valid
    """
    print("\nRunning test_pass_3...")
    assert admin_id_check(SYSTEM_ADMIN_ID_1) == true
    
# test 3 fail   
def test_fail_3():
    """
    this will test if SYSTEM_ADMIN_ID_2 valid    
    """
    print("\nRunning test_fail_3...")
    assert admin_id_check(SYSTEM_ADMIN_ID_2) == true
    

# test 4 pass
def test_pass_4():
    """
    it will get due_date
    """
    print("\nRunning test_pass_4...")
    assert check_due_date() == DUE_DATE_ASSIGNMENT_1
    
# test 4 fail   
def test_fail_4():
    """
    it will get due_date    
    """
    print("\nRunning test_fail_4...")
    assert check_due_date() == DUE_DATE_ASSIGNMENT_1
    
    
# test 5 pass
def test_pass_5():
    """
    function will retrun grade of student based on SID
    """
    print("\nRunning test_pass_5...")
    assert grad_check(SID_1) == GRADE_1
    
# test 5 fail   
def test_fail_5():
    """
    function will retrun grade of student based on SID
    """
    print("\nRunning test_fail_5...")
    assert grad_check(SID_2) != GRADE_2  
    
    
    