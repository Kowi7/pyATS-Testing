from pyats import aetest

class MyTest(aetest.Testcase):
    @aetest.test
    def test1(self):
        assert True

if __name__ == '__main__':
    aetest.main()
