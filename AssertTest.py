class Test:
    def assert_equals(input, output):
        if str(input) == str(output):
            print("Test Passed!")
            return 0
        print("Test Failed!!!")
        print(str(input) + " should be " + str(output))
        return 0
