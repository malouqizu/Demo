Preconditions:
1. Python 3 environment
2. PySerial installed (pip install pyserial)

How to use:
1. comm/at.py 
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

Any issues pls. feel free to contact jinxie@rdamicro.com