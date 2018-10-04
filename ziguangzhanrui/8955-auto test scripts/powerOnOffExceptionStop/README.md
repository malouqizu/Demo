## Preconditions

1. Python 3 environment
2. PySerial installed (pip install pyserial)

## How to use

1. comm/at.py (*deprecated*)
   - customize the specific AT communication COMPORT (line 11: COMPORT = 'COM16')
2. cmd_01.py
   - new a test case script according to this template
   python cmd_01.py
   - run the created case script
3. audio, call, general, gprs, networkService, phonebook, sim, tcpip
   - sub modules
4. runTest.py
   - new a test suite
   python runTest.py
   - run the creted test suite and generate a corresponding HTML report

## USB Relay

To use USB relay, it is needed to start the `relayserver` beforehand.
Python script will communicate with `relayserver` through socket, and
`relayserver` is the *real* program to control USB relay.

## Multiple instances

When running multiple instances, diffrent COM port and relay channel will
be used, and output to different log files. The recommended method is set
by environment variables. Refer to `AtConfig`.

* `AT_TEST_COM`: COM port
* `AT_TEST_RELAY_CHANNEL`: relay channel
* `AT_TEST_LOG_FILE`: log file name

## Run one test case

Example to run test cases:

```
# run test cases in one file
C:\Python36-32\python.exe -m unittest -v stabilitytest.CustomerDemand

# run test cases in one class
C:\Python36-32\python.exe -m unittest -v stabilitytest.CustomerDemand.CustomerBuildInConnect

# run one test case
C:\Python36-32\python.exe -m unittest -v stabilitytest.CustomerDemand.CustomerBuildInConnect.test_supershort

```