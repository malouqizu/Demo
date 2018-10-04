:: cmd build (vs2010)
@ECHO OFF

call "%VS100COMNTOOLS%..\..\VC\vcvarsall.bat" x86 || goto failed

echo "Build ......"

pushd echoserver
mkdir build
pushd build
cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Release || goto failed
cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Release || goto failed
ninja || goto failed
ninja install || goto failed
popd
popd

pushd relayserver
mkdir build
pushd build
cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Release || goto failed
cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Release || goto failed
ninja || goto failed
ninja install || goto failed
popd
popd

exit /B 0

:failed
exit /B %ERRORLEVEL%
