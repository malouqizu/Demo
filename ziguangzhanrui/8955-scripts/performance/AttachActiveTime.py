import time
import unittest
from comm.atchat import atChat
from comm.atlogger import atLogger

class AttachActive(unittest.TestCase):
    name="AttachActive"

    @classmethod
    def setUpClass(cls):
        atLogger.case_start(cls.name)
        atChat.com_open()

    def test_attachactive(self):
        avgtime = 0
        maxtime = 0
        mintime = 1000
        sumtime = 0
        successcnt = 0
        testround = 100
        for i in range(testround):
            atLogger.log_timed('Test Round: %s --------' % str(i + 1))
            atChat.send_command('AT+CGATT=0', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send_command('AT+CGATT=1', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            attachtime = endtime - starttime
            atChat.send_command('AT+CGACT=0', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send_command('AT+CGACT=1', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            activetime = endtime - starttime
            successcnt += 1
            sumtime += (attachtime + activetime)
            avgtime = sumtime / successcnt
            if (activetime + attachtime) > maxtime:
                maxtime = (attachtime + activetime)
            if (activetime + attachtime) < mintime:
                mintime = (attachtime + activetime)
            atLogger.log_timed('Time cost; %ss' % str(attachtime + activetime))

        atLogger.log_timed('Total test round: %s' % str(testround))
        atLogger.log_timed('Success count: %s' % str(successcnt))
        atLogger.log_timed('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        atLogger.log_timed('Average time cost of attach and active: %ss' % str(avgtime))
        atLogger.log_timed('Max time cost of attach and active: %ss' % str(maxtime))
        atLogger.log_timed('Min time cost of attach and active: %ss\n' % str(mintime))
        self.assertTrue(successcnt == testround)

    def test_attach(self):
        avgtime = 0
        maxtime = 0
        mintime = 1000
        sumtime = 0
        successcnt = 0
        testround = 100
        for i in range(testround):
            atLogger.log_timed('Test Round: %s --------' % str(i + 1))
            atChat.send_command('AT+CGATT=0', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send_command('AT+CGATT=1', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            attachtime = endtime - starttime
            successcnt += 1
            sumtime += attachtime
            avgtime = sumtime / successcnt
            if attachtime > maxtime:
                maxtime = attachtime
            if attachtime < mintime:
                mintime = attachtime
            atLogger.log_timed('Time cost; %ss' % str(attachtime))

        atLogger.log_timed('Total test round: %s' % str(testround))
        atLogger.log_timed('Success count: %s' % str(successcnt))
        atLogger.log_timed('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        atLogger.log_timed('Average time cost of attach: %ss' % str(avgtime))
        atLogger.log_timed('Max time cost of attach: %ss' % str(maxtime))
        atLogger.log_timed('Min time cost of attach: %ss\n' % str(mintime))
        self.assertTrue(successcnt == testround)

    def test_detach(self):
        avgtime = 0
        maxtime = 0
        mintime = 1000
        sumtime = 0
        successcnt = 0
        testround = 100
        for i in range(testround):
            atLogger.log_timed('Test Round: %s --------' % str(i + 1))
            atChat.send_command('AT+CGATT=1', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send_command('AT+CGATT=0', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            detachtime = endtime - starttime
            successcnt += 1
            sumtime += detachtime
            avgtime = sumtime / successcnt
            if detachtime > maxtime:
                maxtime = detachtime
            if detachtime < mintime:
                mintime = detachtime
            atLogger.log_timed('Time cost; %ss' % str(detachtime))

        atLogger.log_timed('Total test round: %s' % str(testround))
        atLogger.log_timed('Success count: %s' % str(successcnt))
        atLogger.log_timed('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        atLogger.log_timed('Average time cost of detach: %ss' % str(avgtime))
        atLogger.log_timed('Max time cost of detach: %ss' % str(maxtime))
        atLogger.log_timed('Min time cost of detach: %ss\n' % str(mintime))
        self.assertTrue(successcnt == testround)

    def test_active(self):
        avgtime = 0
        maxtime = 0
        mintime = 1000
        sumtime = 0
        successcnt = 0
        testround = 100
        self.assertTrue(atChat.send_command('AT+CGATT=1', 40.0))
        self.assertTrue(atChat.has('OK'))

        for i in range(testround):
            atLogger.log_timed('Test Round: %s --------' % str(i + 1))
            atChat.send_command('AT+CGACT=0', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send_command('AT+CGACT=1', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            activetime = endtime - starttime
            successcnt += 1
            sumtime += activetime
            avgtime = sumtime / successcnt
            if activetime > maxtime:
                maxtime = activetime
            if activetime < mintime:
                mintime = activetime
            atLogger.log_timed('Time cost; %ss' % str(activetime))

        atLogger.log_timed('Total test round: %s' % str(testround))
        atLogger.log_timed('Success count: %s' % str(successcnt))
        atLogger.log_timed('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        atLogger.log_timed('Average time cost of active: %ss' % str(avgtime))
        atLogger.log_timed('Max time cost of active: %ss' % str(maxtime))
        atLogger.log_timed('Min time cost of active: %ss\n' % str(mintime))
        self.assertTrue(successcnt == testround)

    def test_deactivation(self):
        avgtime = 0
        maxtime = 0
        mintime = 1000
        sumtime = 0
        successcnt = 0
        testround = 100
        self.assertTrue(atChat.send_command('AT+CGATT=1', 40.0))
        self.assertTrue(atChat.has('OK'))

        for i in range(testround):
            atLogger.log_timed('Test Round: %s --------' % str(i + 1))
            atChat.send_command('AT+CGACT=1', 40.0)
            if not atChat.has('OK'):
                continue
            starttime = time.time()
            atChat.send_command('AT+CGACT=0', 40.0)
            endtime = time.time()
            if not atChat.has('OK'):
                continue
            deactivationtime = endtime - starttime
            successcnt += 1
            sumtime += deactivationtime
            avgtime = sumtime / successcnt
            if deactivationtime > maxtime:
                maxtime = deactivationtime
            if deactivationtime < mintime:
                mintime = deactivationtime
            atLogger.log_timed('Time cost; %ss' % str(deactivationtime))

        atLogger.log_timed('Total test round: %s' % str(testround))
        atLogger.log_timed('Success count: %s' % str(successcnt))
        atLogger.log_timed('FPY: %s' % (str(successcnt / testround * 100) + '%'))
        atLogger.log_timed('Average time cost of deactivation: %ss' % str(avgtime))
        atLogger.log_timed('Max time cost of deactivation: %ss' % str(maxtime))
        atLogger.log_timed('Min time cost of deactivation: %ss\n' % str(mintime))
        self.assertTrue(successcnt == testround)

    @classmethod
    def tearDownClass(cls):
        atChat.com_close()
        atLogger.case_end(cls.name)

if __name__=="__main__":
    case_test_attachactive=AttachActive("test_attachactive")
    case_test_attach=AttachActive("test_attach")
    case_test_detach=AttachActive("test_detach")
    case_test_active=AttachActive("test_active")
    case_test_deactivation=AttachActive("test_deactivation")

    suite=unittest.TestSuite()
    suite.addTest(case_test_attachactive)

    runner=unittest.TextTestRunner()
    runner.run(suite)



